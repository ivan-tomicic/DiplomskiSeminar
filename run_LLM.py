import json

from langchain.chains.llm import LLMChain
from langchain_community.llms import CTransformers

from emmezeta import call_emmezeta_api
from emmezeta_utils import color_mappings
from utils import prompt_template




def validate_json(parsed_json):
    parsed_json_copy = parsed_json.copy()
    valid_keys = ['fetchSize', 'width', 'height', 'colors', 'cost', 'sortField', 'sortDir']
    for key in parsed_json.keys():
        if key not in valid_keys:
            parsed_json_copy.pop(key)

    if 'fetchSize' in parsed_json.keys():
        if not isinstance(parsed_json['fetchSize'], int) or parsed_json['fetchSize'] <= 0:
            parsed_json_copy['fetchSize'] = 12

    if 'sortDir' in parsed_json.keys():
        if parsed_json['sortDir'].lower() == 'asc':
            parsed_json_copy['sortDir'] = 'ASC'
        elif parsed_json['sortDir'].lower() == 'desc':
            parsed_json_copy['sortDir'] = 'DESC'
        else:
            parsed_json_copy.pop('sortDir')

    if 'sortField' in parsed_json.keys():
        if parsed_json['sortField'].lower() not in ['name', 'popular', 'price']:
            parsed_json_copy.pop('sortField')

    if 'sortField' in parsed_json.keys() and 'sortDir' not in parsed_json.keys():
        parsed_json_copy.pop('sortField')
    elif 'sortDir' in parsed_json.keys() and 'sortField' not in parsed_json.keys():
        parsed_json_copy.pop('sortDir')

    if 'colors' in parsed_json.keys():
        parsed_json_copy['colors'] = [color_mappings[color] for color in parsed_json['colors'] if
                                      color.lower() in color_mappings.keys()]

    if 'width' in parsed_json.keys():
        width = parsed_json['width']
        if width.startswith('<'):
            width = '0-' + width[1:]
        if width.startswith('>'):
            width = width[1:] + '-10000'

        width = width.split('-')
        if len(width) != 2 or not width[0].isdigit() or not width[1].isdigit():
            parsed_json_copy.pop('width')
        else:
            parsed_json_copy['width'] = width[0] + '-' + width[1]

    if 'cost' in parsed_json.keys():
        cost = parsed_json['cost']
        if cost.startswith('<'):
            cost = '0-' + cost[1:]
        if cost.startswith('>'):
            cost = cost[1:] + '-100000'

        cost = cost.split('-')
        if len(cost) != 2 or not cost[0].isdigit() or not cost[1].isdigit():
            parsed_json_copy.pop('cost')
        else:
            parsed_json_copy['price'] = cost[0] + '-' + cost[1]

    if 'height' in parsed_json.keys():
        height = parsed_json['height']
        if height.startswith('<'):
            height = '0-' + height[1:]
        if height.startswith('>'):
            height = height[1:] + '-10000'

        height = height.split('-')
        if len(height) != 2 or not height[0].isdigit() or not height[1].isdigit():
            parsed_json_copy.pop('height')
        else:
            parsed_json_copy['height'] = height[0] + '-' + height[1]

    return parsed_json_copy


def print_products(products):
    for product in products:
        print("Name:", product["name"])
        print("Picture:", product["gallery"][0]["large_image_url"])
        print("Days to delivery:", product["days_to_delivery"], " days")
        print("Price:", product["prices"][0]["amount"], product["prices"][0]["currency_symbol"])
        print()

def get_response(formatted_input, llmchain):
    output = llmchain.invoke(formatted_input)
    output_json = output['text'].strip()
    output_json = output_json[output_json.find('{'):output_json.find('}') + 1]

    try:
        parsed_json = json.loads(output_json)
    except json.JSONDecodeError:
        parsed_json = None

    if parsed_json is not None:
        validated_json = validate_json(parsed_json)
        api_response = call_emmezeta_api(validated_json)
    else:
        validated_json = None
        api_response = None

    return validated_json, parsed_json, api_response


def run_chat_in_console():
    print("Welcome to the LLM interface. Type 'exit' to quit.")
    config = {
        'max_new_tokens': 256,
        'repetition_penalty': 1.1,
        'context_length': 4000,
        'temperature': 0.01,
        'gpu_layers': 25
    }
    llm = CTransformers(
        model='TheBloke/Mistral-7B-Instruct-v0.2-GGUF',
        model_file='mistral-7b-instruct-v0.2.Q5_K_M.gguf',
        model_type='mistral',
        gpu_layers=25,
        config=config
    )
    llmchain = LLMChain(llm=llm, prompt=prompt_template)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        formatted_input = prompt_template.format(input=user_input)
        validated_json, parsed_json, api_response = get_response(formatted_input, llmchain)

        print("Json that LLM Parsed:", json.dumps(parsed_json, indent=4))
        print("Validated JSON that was actually used in filtering:", json.dumps(validated_json, indent=4))
        print_products(api_response["data"]["products"]["items"])

def initialize_llmchain():
    config = {
        'max_new_tokens': 256,
        'repetition_penalty': 1.1,
        'context_length': 4000,
        'temperature': 0.01,
        'gpu_layers': 25
    }
    llm = CTransformers(
        model='TheBloke/Mistral-7B-Instruct-v0.2-GGUF',
        model_file='mistral-7b-instruct-v0.2.Q5_K_M.gguf',
        model_type='mistral',
        gpu_layers=25,
        config=config
    )
    return LLMChain(llm=llm, prompt=prompt_template)


"""
I have a program that takes in a natural language query like "Fetch me the top 5 popular sofas that are at least 220 cm wide and are red in color" and transforms it into a JSON


{
    "fetchSize": 5,
    "width": ">220",
    "colors": ["red"],
    "sortField": "popular",
    "sortDir": "desc"
}

would you consider this to be Named Entity Recognition or Natural Language Processing or maybe Named Entity Extraction or something else?

"""
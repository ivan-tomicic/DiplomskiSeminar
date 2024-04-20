from langchain.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate

list_of_models = [
    {
        "model_id": "TheBloke/zephyr-7B-beta-GGUF",
        "model_basename": "zephyr-7b-beta.Q5_K_M.gguf",
        "storedInProject": False,
        "type": "mistral"
    },
    {
        "model_id": "TheBloke/zephyr-7B-alpha-GGUF",
        "model_basename": "zephyr-7b-alpha.Q5_K_M.gguf",
        "storedInProject": False,
        "type": "mistral"
    },
    {
        "model_id": "TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
        "model_basename": "mistral-7b-instruct-v0.2.Q5_K_M.gguf",
        "storedInProject": False,
        "type": "mistral"
    },
    {
        "model_id": "TheBloke/Llama-2-7B-Chat-GGUF",
        "model_basename": "llama-2-7b-chat.Q5_K_M.gguf",
        "storedInProject": False,
        "type": "llama"
    },
    {
        "model_id": "TheBloke/OpenHermes-2.5-Mistral-7B-GGUF",
        "model_basename": "openhermes-2.5-mistral-7b.Q5_K_M.gguf",
        "storedInProject": False,
        "type": "mistral"
    },
    {
        "model_id": None,
        "model_basename": "Meta-Llama-3-8B-Instruct.Q5_K_M.gguf",
        "storedInProject": True,
        "type": None
    },
    {
        "model_id": "TheBloke/Mistral-7B-OpenOrca-GGUF",
        "model_basename": "mistral-7b-openorca.Q5_K_M.gguf",
        "storedInProject": False,
        "type": "mistral"
    },
    {
        "model_id": None,
        "model_basename": "Meta-Llama-3-8B.Q5_K_M.gguf",
        "storedInProject": True,
        "type": None
    }
]


prefix_ = """Your job is to generate query parameters that are present in the question in JSON format.
Make sure you to only return the JSON and say nothing else. For example, don't say:
"Here are the query parameters present in the question".
Possible sort fields are "name", "price" and "popular".
Output should include only filters that are specified in the query. Here are some examples:"""

example_prompt = PromptTemplate(
    input_variables=["question", "answer"], template="""Natural Language Query: {question}\nJSON: \n{answer}"""
)
examples = [
    {
        "question": "Give me the 5 cheapest sofas that are between 200 and 250 cm wide, at maximum 130 cm tall and blue or gray color.",
        "answer": "{{\n\"fetchSize\": 5,\n \"width\": \"200-250\",\n \"height\": \"<130\",\n \"colors\": [\"blue\", \"gray\"],\n \"sortField\": \"price\",\n \"sortDir\": \"asc\"\n}}",
    },
    {
        "question": "I want 5 most popular sofas at maximum 220 cm wide. Cost should be less than 1000 euros.",
        "answer": "{{\n\"fetchSize\": 5,\n \"cost\": \"<1000\",\n \"width\": \"<220\",\n \"sortField\": \"popular\",\n \"sortDir\": \"desc\"\n}}",
    },
    {
        "question": "I want 10 sofas that aren't narrower than 205 cm. Cost should be between 600 and 800.",
        "answer": "{{\n\"fetchSize\": 10,\n \"cost\": \"600-800\",\n \"width\": \">205\"\n}}",
    },
    {
        "question": "I want the cheapest blue or red sofa.",
        "answer": "{{\n\"fetchSize\": 1,\n \"colors\": [\"blue\", \"red\"],\n \"sortField\": \"price\",\n \"sortDir\": \"asc\"\n}}",
    }
]
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Now give me the JSON for this:\nNatural Language Query: {input}\nJSON: \n",
    prefix=prefix_,
    input_variables=["input"],
)
print("Prompt Template: ", prompt_template)


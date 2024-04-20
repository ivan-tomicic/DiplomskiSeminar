import json
import datetime

from langchain.chains.llm import LLMChain
from langchain_community.llms import CTransformers
from llama_cpp import Llama

from utils import list_of_models, prompt_template
from test_data import test_data


def compare_jsons(actual_json, expected_json):
    matching_fields = 0

    for key in expected_json:
        if key in actual_json:
            if isinstance(expected_json[key], list):
                if set(actual_json[key]) == set(expected_json[key]):
                    matching_fields += 1
            else:
                if actual_json[key] == expected_json[key]:
                    matching_fields += 1

    return matching_fields


def test_models(models, test_data, prompt_template):
    results = {}

    for model in models:
        model_id = model["model_basename"]
        stored_in_project = model["storedInProject"]
        results[model_id] = []
        llmchain = None

        if not stored_in_project:
            config = {
                'max_new_tokens': 256,
                'repetition_penalty': 1.1,
                'context_length': 4000,
                'temperature': 0.01,
                'gpu_layers': 25
            }
            llm = CTransformers(
                model=model['model_id'],
                model_file=model['model_basename'],
                model_type=model['type'],
                gpu_layers=25,
                config=config
            )
            llmchain = LLMChain(llm=llm, prompt=prompt_template)
        else:
            llmchain = Llama(
                model_path="./models/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf",
                n_gpu_layers=25,  # Uncomment to use GPU acceleration
                # seed=1337, # Uncomment to set a specific seed
                n_ctx=4000,  # Uncomment to increase the context window
            )

        for test in test_data:
            formatted_input = prompt_template.format(input=test["question"])
            try:
                if not stored_in_project:
                    output = llmchain.invoke(formatted_input)
                    output_json = output['text'].strip()
                else:
                    output = llmchain(
                        formatted_input,  # Prompt
                        max_tokens=256,
                        # Generate up to 32 tokens, set to None to generate up to the end of the context window
                        # stop=["Q:", "\n"],  # Stop generating just before the model would generate a new question
                        # echo=True  # Echo the prompt back in the output
                    )
                    output_json = output['choices'][0]['text'].strip()

                output_json = output_json[output_json.find('{'):output_json.find('}') + 1]

                try:
                    parsed_json = json.loads(output_json)
                    results[model_id].append({
                        "question_id": test["id"],
                        "actualJSON": parsed_json,
                        "unparseableJSON": False,
                        "numberOfFields": len(test["correctJSON"]),
                        "matchingFields": compare_jsons(parsed_json, test["correctJSON"]),
                        "error": None
                    })
                    print(f"Classified input >>{test['question']}<< as >>{output_json}<<, number of matching fields: {compare_jsons(parsed_json, test['correctJSON'])}<<.")
                except json.JSONDecodeError:
                    results[model_id].append({
                        "question_id": test["id"],
                        "actualJSON": None,
                        "unparseableJSON": True,
                        "numberOfFields": len(test["correctJSON"]),
                        "matchingFields": 0,
                        "error": "JSON is not parseable"
                    })
                    print(f"Classified input >>{test['question']}<< as >>{output_json}<<, but it is not parseable.")

            except Exception as e:
                print(f"Error processing model {model_id}: {e}")
                results[model_id].append({
                    "question_id": test["id"],
                    "actualJSON": None,
                    "unparseableJSON": True,
                    "numberOfFields": len(test["correctJSON"]),
                    "matchingFields": 0,
                    "error": str(e)
                })

    return results


results_ = test_models(list_of_models, test_data, prompt_template)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"results_{timestamp}.json"
with open(output_file, "w") as file:
    json.dump(results_, file, indent=4)
print(f"Results saved to {output_file}")

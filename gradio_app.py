import json
import gradio as gr

from utils import prompt_template
from run_LLM import get_response, initialize_llmchain

llm_instance = initialize_llmchain()

def print_products(products):
    product_details = []
    for product in products:
        details = {
            "name": product["name"],
            "image_url": product["gallery"][0]["large_image_url"],
            "days_to_delivery": product["days_to_delivery"],
            "price": f'{product["prices"][0]["amount"]} {product["prices"][0]["currency_symbol"]}'
        }
        product_details.append(details)
    return product_details

def chatbot(user_input):
    formatted_input = prompt_template.format(input=user_input)
    validated_json, parsed_json, api_response = get_response(formatted_input, llm_instance)

    print("Parsed JSON:\n", json.dumps(parsed_json, indent=4))
    print("Validated JSON:\n", json.dumps(validated_json, indent=4))

    if parsed_json is None:
        return {"error": "JSON parsing failed. Please try again."}

    response_json = {
        "parsed_json": parsed_json,
        "validated_json": validated_json,
        "products": print_products(api_response["data"]["products"]["items"])
    }
    return response_json

def display_response(response_json):
    if "error" in response_json:
        return response_json["error"]
    message = ""
    for product in response_json["products"]:
        message += f"Name: {product['name']}\n"
        message += f"Days to delivery: {product['days_to_delivery']} days\n"
        message += f"Price: {product['price']}\n\n"
    return message

def get_images(response_json):
    if "error" in response_json:
        return []
    return [(product["image_url"], product["name"]) for product in response_json["products"]]

with gr.Blocks() as demo:
    with gr.Row():
        user_input = gr.Textbox(label="You:")
        output_text = gr.Textbox(label="Response", lines=10)
        image_output = gr.Gallery(label="Product Images")


    def interact(user_input):
        response_json = chatbot(user_input)
        return display_response(response_json), get_images(response_json)

    user_input.submit(interact, inputs=user_input, outputs=[output_text, image_output])


demo.launch()

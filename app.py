import os
import openai
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

# Get OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

# Initialize conversation context
context = [
    {'role': 'system', 'content': "You are a negotiation bot."},
    {'role': 'assistant', 'content': "Welcome! The listed price for the product is $100."}
]

product_price = 100  # Starting product price
min_price = 70  # Minimum acceptable price
discount_step = 5  # Discount increment

# Extract price from user input
def extract_price(user_input):
    import re
    match = re.search(r"\$\s?(\d+(\.\d{1,2})?)|(\d+(\.\d{1,2})?)", user_input)
    if match:
        return float(match.group().replace('$', '').strip())
    return None

# Check if user has accepted the deal
def is_acceptance(user_input):
    acceptance_phrases = ["i'll take it", "deal", "sure", "okay", "yes", "i agree"]
    return any(phrase in user_input.lower() for phrase in acceptance_phrases)

# OpenAI API call to get chatbot response
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

# API endpoint to start a negotiation
@app.route('/start', methods=['GET'])
def start_negotiation():
    global context, product_price
    context = [
        {'role': 'system', 'content': "You are a negotiation bot."},
        {'role': 'assistant', 'content': "Welcome! The listed price for the product is $100."}
    ]
    product_price = 100
    return jsonify({"message": "Negotiation started!", "price": 100})

# API endpoint to handle offers
@app.route('/offer', methods=['POST'])
def handle_offer():
    global context, product_price, min_price, discount_step
    user_input = request.json.get('offer', '')

    # Add user's offer to conversation
    context.append({'role': 'user', 'content': user_input})

    offer_price = extract_price(user_input)
    if is_acceptance(user_input):
        response = f"Great! You've agreed to purchase at ${product_price}. Thank you!"
    elif offer_price:
        if offer_price >= min_price and offer_price < product_price:
            product_price = max(offer_price + discount_step, min_price)
            response = f"I can offer the product for ${product_price}. Do we have a deal?"
        elif offer_price < min_price:
            response = f"Sorry, the lowest I can go is ${min_price}."
        else:
            response = f"Perfect! The product is yours for ${offer_price}."
    else:
        response = "Please provide a valid price or response."

    # Add bot's response to the conversation
    context.append({'role': 'assistant', 'content': response})

    return jsonify({"message": response, "price": product_price})

if __name__ == "__main__":
    app.run(debug=True)

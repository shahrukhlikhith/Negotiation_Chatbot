# Negotiation Chatbot API

## Project Overview

This project is a **Negotiation Chatbot API** that simulates a negotiation process between a customer and a supplier using OpenAI's GPT model. The chatbot allows the customer to negotiate the price of a product by making offers, and the bot responds by either accepting, rejecting, or proposing a counteroffer. The chatbot has built-in pricing logic and can adjust offers based on user input.

The project includes two main API endpoints for initiating a negotiation and submitting offers, and integrates OpenAI's language model to handle conversational logic.

## Features

- **Basic conversation flow**: The chatbot initiates a negotiation with a listed price and handles user offers.
- **Pricing logic**: Offers are adjusted based on user input and predefined price ranges.
- **Model integration**: OpenAI's GPT model is used to generate negotiation responses.
- **Sentiment analysis (optional)**: Not implemented in this version but can be extended for sentiment-based price adjustments.

## Tech Stack

- **Flask**: Python-based micro-framework to handle API routing.
- **OpenAI GPT Model**: Language model for generating conversation.
- **Postman/cURL**: For testing the API.
- **dotenv**: Used to manage environment variables (OpenAI API key).

## API Endpoints

### 1. `/start` (GET)
Initiates the negotiation process and provides the listed price for the product.

- **Request**:
  ```bash
  GET /start
  
- **Response**:
  ```json
  {
    "message": "Negotiation started!",
    "price": 100
  }
### 2. `/offer` (POST)
Handles the user's offer and returns the chatbot's response, either accepting, rejecting, or making a counteroffer.

- **Request:**

  ```bash
  POST /offer
  Content-Type: application/json
  Body: {"offer": "I'd like to buy it for $80"}
- **Response:**

  ```json
  {
    "message": "I can offer the product for $85.0. Do we have a deal?",
    "price": 85.0
  }

## OpenAI Integration
The chatbot uses OpenAI's GPT model to handle conversational logic. Here's how it works:

1. A user sends an offer via the `/offer` endpoint.
2. The chatbot processes the offer and uses the OpenAI GPT API to generate a negotiation response.
3. The response is returned to the user, either accepting the offer, proposing a counteroffer, or rejecting it.
The model is integrated into the code using OpenAI's Python SDK, which allows for easy interaction with their GPT models.

## Setup Instructions
To set up and run the negotiation chatbot API locally, follow these steps:

## Setup Instructions

To set up and run the negotiation chatbot API locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd negotiation-chatbot
2. **Create a virtual environment (optional):**:
   ```bash
   git clone <your-repo-url>
   cd negotiation-chatbot
3. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt

4. **Set up environment variables:** Create a .env file in the project directory with the following content::
   ```makefile
   OPENAI_API_KEY=your-openai-api-key

5. **Run the Flask app:**:
   ```bash
   python app.py

6. **Test the API using Postman or cURL:**:
- For `/start`: `GET http://127.0.0.1:5000/start`
- For `/offer`: `POST http://127.0.0.1:5000/offer` with body
   ```json
   {
  "offer": "I would like to buy it for $80"
  }

   
## Demo
You can follow this example to test the negotiation process:

1. **Start Negotiation:** Call the `/start` endpoint to initiate the negotiation and get the listed price of the product.

- **Request:**

  ```bash

  GET http://127.0.0.1:5000/start
- **Response:**

  ```json

  {
    "message": "Negotiation started!",
    "price": 100
  }
2. **Make an Offer**: Submit an offer using the /offer endpoint. For example, a customer might offer $80 for the product.

- **Request**:

  ```bash

  POST http://127.0.0.1:5000/offer
  Content-Type: application/json
  Body: {"offer": "I would like to buy it for $80"}
- **Response**:

  ```json

  {
    "message": "I can offer the product for $85.0. Do we have a deal?",
    "price": 85.0
  }
3. **Finalize**: You can make additional offers or accept the bot’s counteroffer by repeating the process.

## Future Enhancements
- Sentiment Analysis: The chatbot can be enhanced to offer better deals to polite or positive customers.
- Dynamic Pricing: The price range and discount logic could be made more dynamic and data-driven.

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
### 1. `/offer` (POST)
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

1. A user sends an offer via the /offer endpoint.
2. The chatbot processes the offer and uses the OpenAI GPT API to generate a negotiation response.
3. The response is returned to the user, either accepting the offer, proposing a counteroffer, or rejecting it.
The model is integrated into the code using OpenAI's Python SDK, which allows for easy interaction with their GPT models.

## Setup Instructions
To set up and run the negotiation chatbot API locally, follow these steps:

**1. Clone the repository:**

  ```bash

    git clone <your-repo-url>
    cd negotiation-chatbot

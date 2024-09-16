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
  {
    "message": "Negotiation started!",
    "price": 100
  }

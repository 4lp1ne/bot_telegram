# Telegram GPT-4 Bot

A simple Telegram bot powered by OpenAI's GPT-4. This bot allows users to interact with an AI assistant directly from Telegram. The bot listens to messages sent to it via Telegram, processes them using OpenAI's GPT-4 model, and responds with intelligent, conversational replies.

## Features

- **GPT-4 Powered**: Uses OpenAI's GPT-4 model for generating responses.
- **Telegram Bot Integration**: Easily communicate with the AI assistant via Telegram.
- **Local Development Support**: Run the bot locally and test with `ngrok` for webhook setup.

## Requirements

- **Python 3.7+**
- A **Telegram bot token** (from [BotFather](https://core.telegram.org/bots#botfather))
- An **OpenAI API key** (from [OpenAI](https://platform.openai.com/account/api-keys))
- **ngrok** (optional, for local development to expose your server to the internet)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-gpt4-bot.git
cd telegram-gpt4-bot
2. Set Up a Virtual Environment
Create and activate a virtual environment:

For Linux/Mac:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
For Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Install the required dependencies from requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the project root and add your Telegram bot token and OpenAI API key:

bash
Copy code
TELEGRAM_TOKEN=your-telegram-bot-token
OPENAI_API_KEY=your-openai-api-key
Replace your-telegram-bot-token and your-openai-api-key with your actual credentials.

5. Run the Bot
Start the bot by running the following command:

bash
Copy code
python bot_t_gpt.py
6. (Optional) Set Up ngrok for Local Development
To expose your bot to the internet for Telegram webhooks during local development, use ngrok:

Install ngrok.
Run ngrok to expose your local Flask/Quart server:
bash
Copy code
ngrok http 5000
Copy the https:// forwarding URL provided by ngrok.
Set the webhook with the following command (replace <ngrok_url> and <your_telegram_token>):
bash
Copy code
curl -F "url=https://<ngrok_url>/<your_telegram_token>" https://api.telegram.org/bot<your_telegram_token>/setWebhook
This will connect your local server to Telegram, enabling real-time message processing.

Usage
Start a Chat with Your Bot: Search for your bot on Telegram using its username.
Send a Message: Type a message, and the bot will respond using OpenAI's GPT-4 model.
Files
bot_t_gpt.py: The main bot logic integrating Telegram with OpenAI's GPT-4.
requirements.txt: The Python dependencies required to run the project.
.env: (User-generated) Store your API keys and tokens securely in this file (ensure it’s in your .gitignore file).
Project Workflow
Message from User: The bot receives a message through the Telegram API.
Process the Message: The bot sends the message to OpenAI's GPT-4 for processing.
Response: GPT-4 generates a response, which is then sent back to the user via Telegram.
License
This project is licensed under the MIT License. Feel free to contribute or fork the repository for personal use!

Contributing
Feel free to open issues or submit pull requests. Contributions are welcome to improve the bot or add new features.

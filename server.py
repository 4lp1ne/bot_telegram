from quart import Quart, request
import telegram
import openai
import os

app = Quart(__name__)

# Load environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Telegram bot and OpenAI API
bot = telegram.Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# Function to send a message back to Telegram chat
async def send_message(chat_id, text):
    try:
        print(f"Sending message to chat_id {chat_id}: {text}")
        await bot.send_message(chat_id=chat_id, text=text)
    except telegram.error.TelegramError as e:
        print(f"Failed to send message: {e}")

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
async def respond():
    try:
        update = telegram.Update.de_json(await request.get_json(), bot)
        chat_id = update.message.chat.id
        message = update.message.text
        print(f"Received message: {message} from chat_id: {chat_id}")

        # Call OpenAI API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        # Extract GPT-4's reply
        reply = response['choices'][0]['message']['content']
        print(f"GPT-4 reply: {reply}")

        # Send GPT-4 reply back to Telegram
        await send_message(chat_id, reply)
        return "ok", 200

    except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error", 500

@app.route('/')
async def index():
    return "Bot is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

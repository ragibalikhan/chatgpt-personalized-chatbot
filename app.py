import logging
import telebot
from telebot import types
import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR-OPENAI-API'

# Dictionary to map agents to their prompts
AGENT_PROMPTS = {}

# Read the prompts from data.txt and populate the AGENT_PROMPTS dictionary
with open('data.txt', 'r') as file:
    for line in file:
        agent, prompt = line.strip().split(':')
        AGENT_PROMPTS[agent] = prompt

# Dictionary to map agent names to command keywords
AGENT_COMMANDS = {
    'default_agent': '/default',
    'sales_manager': '/sales',
    'connector': '/connector'
}

# Create a telebot instance
bot = telebot.TeleBot("YOUR-TELEGRAM-TOKEN")

# Function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Get the user's message
    user_message = message.text

    # Get the agent for the user
    agent = get_agent_for_user(message.from_user.id)

    # Construct the prompt with the agent's message and user's message
    prompt = AGENT_PROMPTS[agent] + '\n\nUser: ' + user_message

    # Call the OpenAI Chat API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=None
    )

    # Extract the generated response from the API response
    bot_response = response.choices[0].text.strip()

    # Send the response back to the user
    bot.reply_to(message, bot_response)

# Function to determine the agent based on user ID
def get_agent_for_user(user_id):
    # Convert user_id to string
    user_id_str = str(user_id)

    # You can implement your own logic here to assign agents to users
    # For example, you can assign a sales manager agent to users with IDs starting with 'S'
    # and a connector agent to users with IDs starting with 'C'
    if user_id_str.startswith('S'):
        return 'sales_manager'
    elif user_id_str.startswith('C'):
        return 'connector'
    else:
        return 'default_agent'

# Function to handle the agent command
@bot.message_handler(commands=['agent'])
def switch_agent(message):
    command = message.text.split()[1].lower()

    for agent, cmd in AGENT_COMMANDS.items():
        if command == cmd:
            # Assign the selected agent to the user
            user_id = message.from_user.id
            # Store the agent in user_data
            bot.user_data[user_id] = agent
            bot.reply_to(message, f"You are now chatting with the {agent} agent.")
            return

    bot.reply_to(message, "Invalid command. Please use a valid agent command.")

@bot.message_handler(commands=['start'])
def start(message):
    # Welcome message when the bot starts
    bot.reply_to(message, "Welcome to ConnectFluence! How can I assist you today?")

def main():
    # Set up the logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # Start the bot
    bot.polling()

if __name__ == '__main__':
    main()

# Telegram Business Personalized Chat-Bot

This is a Telegram chat-bot designed for a business that provides personalized responses to users based on their needs. The chat-bot is built using the OpenAI API and the Telebot library.
Test the telegram bot on [ConnectFluence](https://t.me/ConnectFluencebot).

## Features

- Multiple agents: The chat-bot supports multiple agents, each specialized in a specific role or department within the business.
- Agent selection: Users can switch between different agents by using command keywords.
- Personalized prompts: Each agent has its own prompt that is sent to the OpenAI API along with the user's message to generate a tailored response.
- Integration with Telegram: The chat-bot is integrated with the Telegram messaging platform, allowing users to interact with the bot through the Telegram app.

## Setup and Configuration

To set up the chat-bot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain an API key from OpenAI and replace `'YOUR-OPENAI-API'` in the code with your API key.
4. Configure the prompts for each agent by editing the `data.txt` file. Each line should follow the format `agent_name:prompt_text`.
5. Set up a Telegram bot by following the instructions provided by the [Telegram Bot API](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
6. Replace `'YOUR-TELEGRAM-TOKEN'` in the code with your Telegram bot token.
7. Customize the agent commands and their corresponding keywords in the `AGENT_COMMANDS` dictionary if desired.
8. Run the Python script using `python main.py`.

## Usage

Once the chat-bot is set up and running, users can interact with it through the Telegram app. The chat-bot will respond based on the selected agent's prompt and the user's messages.

- To switch agents, use the `/agent` command followed by the desired agent's command keyword.
- To start a conversation, send a message to the chat-bot.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


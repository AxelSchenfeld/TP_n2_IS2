# ChatGPT Interaction Module

This Python project provides a module for interacting with the ChatGPT model through the OpenAI API. It enables users to send queries and receive responses in a conversation-like format. The program includes a command-line interface that activates a conversation mode, where the user can interact with the model, review, and edit previous queries.

## Features

- **Conversation Mode**: Activate the conversation mode by passing the `--convers` argument when running the program. The program will continuously process user input and provide responses.
- **Query Handling**: The user can input queries, and the program sends them to the ChatGPT model for processing. The model’s response is printed and stored for future reference.
- **Last Query Editing**: Users can edit and resend their last query by pressing the "Up Arrow" key on the keyboard.
- **Error Handling**: The program catches exceptions and displays helpful error messages if something goes wrong during the process.

## How to Run

To start the program, use the following command:

```bash
python your_script.py --convers
```

If you don't want to activate conversation mode, simply run:

```bash
python your_script.py
```

## Requirements

- Python 3.x
- OpenAI Python package (`openai`)
  
Make sure to replace the API key in the script with your own OpenAI API key.

## Usage

- The program will enter conversation mode, where you can input queries.
- You can edit the last query using the "Up Arrow" key, and it will be processed again.
- If an error occurs, it will be displayed as an error message.

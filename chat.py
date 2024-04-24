'''This module provides functions to interact with the chatGPT model.'''
import argparse # Importing the argparse library
from openai import OpenAI # Importing the openai library

# OpenAI client initialization

client=OpenAI(api_key=None) # Replace None with the API Key

# Definition of context and user variables
context = "You are a professional astronomer"
usertask = "learn"
userquery = "-"


last_conversation = [] # Variable to store the last query and response

def process_query(query):
    '''Function to process the query'''
    try:
        # Query processing
        if query.strip(): # Removes leading and trailing characters.
            print(f"You: {query}")
            # Calling the OpenAI model with the last query made
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {
                        "role": "system",
                        "content": context, 
                    },
                    {
                        "role": "user",
                        "content": usertask, # I left user task empty because I'm not sure what should go there
                    },
                    {
                        "role": "user",
                        "content": query # Mainly using the query
                    }
                ],
                temperature=1,
                max_tokens=150, # to limit tokens and save on the paid version I have.
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            # Getting response
            chatgpt_response = response.choices[0].message.content # Captures the response
            print(f"chatGPT: {chatgpt_response}") # Prints it out
            # Adding the query and response to the buffer
            last_conversation.append((query, chatgpt_response)) # Added to the list

    except Exception as e: # Requested exceptions declared in "e" for ease
        print(f"Error processing query: {e}") # Shown on the screen.


def handle_keyboard_events():
    '''Handle keyboard events using readline'''
    while True:
        input_data = input("")
        if input_data == "\x1b[A":  # "cursor Up"
            last_query = input("Enter your query (edit the last query): ")
            process_query(last_query) # Call process_query again
        else:
            last_query = input_data
            process_query(input_data)


def conversation_mode():
    '''Function to process conversation mode'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--convers", action="store_true", help="Conversation mode")
    args = parser.parse_args()

    if args.convers:
        print("Conversation mode activated. Press Ctrl + C to exit.")
        handle_keyboard_events()
    else:
        print("The '--convers' argument is not present. Ignoring conversation mode.")


try: # Execute the program
    conversation_mode()
except KeyboardInterrupt: # An easily testable exception
    print("\nProgram execution has been interrupted.")
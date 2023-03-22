from imessage_reader import fetch_data
from chat_functionality import *
from config import *
import subprocess


# Apple Script to send imessage 'message' to recipient 'phone_numer'
def send_imessage(phone_number, message):
    subprocess.run(["osascript", script_path, phone_number, message])


# Checks who (you or recipient) sent the last text message in a conversation
def check_last(message_list):
    message = message_list[-1]
    if message[5] == 0:
        return True
    return False


# Gets the last text message sent in a conversation
def get_last(message_list):
    return message_list[-1][1]


# Primarily composed of a while loop that constantly runs waits for texts until you press 'Ctrl-C'
def text_bot(
    phone_number,
    conversation=[{"role": "system", "content": "You are a helpful assistant."}],
):
    while True:
        # Indicates when you were the last one to text in a conversation. It is waiting for a response from the recipient
        print("Waiting...")
        while True:
            # Fetches conversation all of your imessages
            fd = fetch_data.FetchData()
            messages = fd.get_messages()

            # Creates a new list that only contains the messages between you and the specified recipient
            message_list = [text for text in messages if text[0] == phone_number]

            # Checks to see who sent the last message. If it was you, then it keeps running through the while loop. If it was your recipient, then it breaks out of the while loop and attempts to send the message
            if check_last(message_list):
                print(f"Text: {get_last(message_list)}\n")
                break

        # Uses the 'completed_assistant' function to get how ChatGPT would respond to the person's text message
        new_message = completed_assistant(get_last(message_list), conversation)
        print(f"Response: {new_message}")

        if require_approval:
            check = input(
                "Press the 'Enter' key to continue sending ('Ctr-C to abort):"
            )

        # Uses the apple script to send the message to the phone number you provided
        send_imessage(phone_number, new_message)
        print("Message sent")


# Get the conversation history between you and the recipient. Give ChatGPT this information so it can respond to texts within the context of the conversation history.
def get_history(phone_number):
    fd = fetch_data.FetchData()
    messages = fd.get_messages()
    message_list = [text for text in messages if text[0] == phone_number]
    message_quant = len(message_list)
    # Change the 'content' in the conversation in order to give ChatGPT a basis of how it should be responding to texts
    conversation = [
        {
            "role": "system",
            "content": "You are texting someone you know.",
            "role": "user",
            "content": "You are to pretend that you are texting a person on your phone, the following conversation is are previous text messages. You only resond in a maximum of 5 sentences. Never acknowlegde that you are an AI.",
        }
    ]
    # Because of ChatGPT's limit on the amount of content you upload, this only retrieves the last 200 text messages sent between you and a recipient
    if message_quant <= 200:
        for message in message_list:
            if message[-1]:
                conversation.append({"role": "user", "content": message[1]})
            else:
                conversation.append({"role": "assistant", "content": message[1]})
        if check_last(message_list):
            conversation.pop(-1)
        return conversation
    # if the conversation history between you and the recipient is less than 200, then it just uploads the entire thing
    else:
        for message in message_list[-200::]:
            if message[-1]:
                conversation.append({"role": "user", "content": message[1]})
            else:
                conversation.append({"role": "assistant", "content": message[1]})
        if check_last(message_list):
            conversation.pop(-1)
        return conversation


# Gets the conversation history between you and the recipient
convo_hist = get_history(phone_number)

# Starts running the program using the conversation history
text_bot(phone_number, convo_hist)

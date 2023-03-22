from imessage_reader import fetch_data
from chat_functionality import *
import subprocess

# Paste the phone number you want to text with here as a string!
phone_number = "+123456789"


def send_imessage(phone_number, message):
    script_path = "/Path/to/directory/send_iMessage.scpt"
    subprocess.run(["osascript", script_path, phone_number, message])


def check_last(message_list):
    message = message_list[-1]
    if message[5] == 0:
        return True
    return False


def get_last(message_list):
    return message_list[-1][1]


def text_bot(
    phone_number,
    conversation=[{"role": "system", "content": "You are a helpful assistant."}],
):
    while True:
        print("Waiting...")
        while True:
            fd = fetch_data.FetchData()
            messages = fd.get_messages()

            message_list = [text for text in messages if text[0] == phone_number]

            if check_last(message_list):
                print(f"Text: {get_last(message_list)}\n")
                break
        new_message = completed_assistant(get_last(message_list), conversation)
        print(f"Response: {new_message}")

        # Remove the line below if you don't want to check the message before sending
        check = input("Press the 'Enter' key to continue sending:")

        send_imessage(phone_number, new_message)
        print("Message sent")


def get_history(phone_number):
    fd = fetch_data.FetchData()
    messages = fd.get_messages()
    message_list = [text for text in messages if text[0] == phone_number]
    message_quant = len(message_list)
    conversation = [
        {
            "role": "system",
            "content": "You are texting someone you know.",
            "role": "user",
            "content": "You are to pretend that you are texting a person on your phone, the following conversation is are previous text messages. You only resond in a maximum of 5 sentences. Never acknowlegde that you are an AI.",
        }
    ]
    if message_quant <= 200:
        for message in message_list:
            if message[-1]:
                conversation.append({"role": "user", "content": message[1]})
            else:
                conversation.append({"role": "assistant", "content": message[1]})
        if check_last(message_list):
            conversation.pop(-1)
        return conversation
    else:
        for message in message_list[-200::]:
            if message[-1]:
                conversation.append({"role": "user", "content": message[1]})
            else:
                conversation.append({"role": "assistant", "content": message[1]})
        if check_last(message_list):
            conversation.pop(-1)
        return conversation


convo_hist = get_history(phone_number)
text_bot(phone_number, convo_hist)

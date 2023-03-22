import openai

openai.api_key = "Paste your api key here as a string!"

# Add a path to the directory where send_imessage.scpt is stored. This is most likely in the same directory as the rest of the downloaded files
script_path = "/Path/to/directory/send_iMessage.scpt"

# Change to False if you want the program to automatically send text messages without you looking it over
require_approval = True

# Paste the phone number you want to text with here as a string!
phone_number = "+123456789"

# Text Bot GPT

# Before Using:
Open Terminal
Run:

'pip install imessage-reader'

'pip install openai'

Go into System Settings on your mac, under 'Privacy & Security', press on 'Full Disk Access' and enable Terminal.
^ This allows the program to read and respond to your imessage conversations

# Usage
Go into text-bot-GPT.py and define the 'phone_numer' variable as the number you want to text.
Example, this would text the number '+123456789': phone_number = '+123456789'

Go into chat_functionality.py and on line 3 paste your OpenAI API key in the designated spot. This program requires an OpenAI API key in order to work. If you do not have a key, you can make an account and/or get a key here: https://auth0.openai.com/u/signup/identifier?state=hKFo2SBDdGt4b2tMS2VHRzU4SXhNd1lZZHJxR0xsS0F5Wk53QqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE56aWJ3cWJ1NEZLb05HSHdoMnpBZzk5SVAwcGs4b2ZJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q

Run python3 text-bot-GPT.py in your terminal in order to start the program.

# Notes
Before sending any messages, the program will output the text that was sent to you, as well as the response that the program is about to send.
If you are okay with the resposne, just press enter. Otherwise press 'Ctrl-C' to stop the program and NOT send the message.
^ This warning can be removed by deleting line 50 in text-bot-gpt.py

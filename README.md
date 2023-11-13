# Text Bot GPT
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a text bot for imessage that was inspired by South Park's 'Deep Learning' episode. The program was made to continuously run so that it is constantly checking whether or not it needs to respond to a text message. If the specified number texts you, it will automatically feed the text message into OpenAI's ChatGPT API and come up with a response to the text. This text will then be sent to the phone number you specified. 

There are options to configure this program such as removing the 'Approval' required before sending automatically sending responses. I added many comments throughout the code in case you are curious about what is going on. Also, in the comments I make note of some changes in functionality you can make.

This project is still heavily under development, so expect there to be updates and changes in the coming days.

If you like my work please consider donating:

<a href="https://www.buymeacoffee.com/seaborg1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Getting Started

These are some basic instructions to help you get started.

### Prerequisites

What you need to install:

* [imessage-reader](https://pypi.org/project/imessage-reader/) - python lib for working with imessage
* [OpenAI API](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBDdGt4b2tMS2VHRzU4SXhNd1lZZHJxR0xsS0F5Wk53QqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE56aWJ3cWJ1NEZLb05HSHdoMnpBZzk5SVAwcGs4b2ZJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) - ChatGPT API

Follow this [link](https://www.alfredapp.com/help/troubleshooting/indexing/terminal-full-disk-access/) to enable full disk access for Terminal. This allows the program to access your chat.db in order to read and respond to text messages.

### Installing

A step by step series of examples that tell you how to get a development env running

Install OpenAI API (After Obtaining an API key from the website)

```
pip install openai
```

Install imessage-reader

```
pip install imessage-reader
```

### Usage

Before using the program, open the file 'config.py' and paste your OpenAI API key on the designated location (This never changes). Then paste the phone number you want to text with at the designated location (This you may change often depending on who you want to text). You also need to specify the path to the send_iMessage.scpt file that was downloaded (This is most likely located in the same directory as the other files you downloaded). For Example: script_path = "/Users/name/Desktop/text-bot-GPT/send_iMessage.scpt"

To run the program simply open your Terminal and go to the directory in which the files are located.

Then run:

```
python3 text-bot-GPT.py
```
This starts the program using your provided configuration. The program will say 'waiting' if you were the last to text in a conversation. Otherwise it will print out a person's text, print out ChatGPT's response, and await your approval before sending.

## Built With

* [imessage-reader](https://pypi.org/project/imessage-reader/) - python lib for working with imessage
* [OpenAI API](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBDdGt4b2tMS2VHRzU4SXhNd1lZZHJxR0xsS0F5Wk53QqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE56aWJ3cWJ1NEZLb05HSHdoMnpBZzk5SVAwcGs4b2ZJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) - ChatGPT API
* [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html) - Used for sending iMessages

## Contributing

Please read [CONTRIBUTING.md](https://github.com/seaborg1/text-bot-GPT/blob/main/CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests to us. Follow the general guidelines outlined in the link. 

## Author

**Franco (Seaborg1)** 

## License

This project is licensed under the GNU v.3 General Public License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Shoutout to [niffitycode](https://pypi.org/user/niftycode/) - Author of imessage-reader
* [OpenAI](https://openai.com/)
* [South Park](https://southpark.cc.com/episodes/8byci4/south-park-deep-learning-season-26-ep-4) - For the inspiration
* Shoutout to [PurpleBooth](https://gist.github.com/PurpleBooth) - for putting this README template together

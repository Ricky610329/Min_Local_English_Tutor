import argparse
from ollama import chat
from sound import generate_sound
import atexit
import re
import json

def clear_wav_files():
    import os
    if os.path.exists("output.wav"):
        os.remove("output.wav")

atexit.register(clear_wav_files)

def prase_output(response):
    # remove unwanted characters
    # *, #, @
    response = re.sub(r'[*#@]', '', response)

    # remove emojis
    response = re.sub(r'[^\x00-\x7F]+', '', response)

    return response


def save_conversation(conversation, filename='message.json'):
    with open(filename, 'w') as f:
        json.dump(conversation, f, indent=4)
    
def load_conversation(filename='message.json'):
    with open(filename, 'r') as f:
        conversation = json.load(f)
    return conversation


class chatbot:
    def __init__(self, message=None):
        self.characteristics = {
            'name': 'Emma',
            'age': 25,
            'Profession': "English Teacher",
            'task': "you are about to start a normal conversation with user, feel easy and sometimes give minimum suggestion to user of what he/she said (about improving eEglish)\n",
            'note': "It's about letting user to talk more"
        }

        # minimum and little is a good word
        if message is None:
            self.message = [{'role': 'system', 'content': 'you are' + str(self.characteristics)}]
        else:
            self.message = message
        self.model = 'gemma3:12b'

    def chat(self, mesg):
        self.message.append({'role': 'user', 'content': mesg})
        response = chat(
            model=self.model,
            messages=self.message
        )
        self.message.append({'role': 'assistant', 'content': response['message']['content']})
        return response['message']['content']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the chatbot with a specified conversation file.")
    parser.add_argument('-l', type=str, default='message.json', help='The conversation file to load from.')
    parser.add_argument('-s', type=str, default='message.json', help='The conversation file to save to.')
    args = parser.parse_args()

    load_file = args.l
    save_file = args.s

    # Load conversation if the file exists
    try:
        mesg = load_conversation(load_file)
        english_tutor = chatbot(mesg)
    except FileNotFoundError:
        english_tutor = chatbot()


    while True:
        mesg = input('\n>>>')
        if mesg == '/quit' or mesg == '/exit':
            break

        response = english_tutor.chat(mesg)
        print("\nEmma:\n", response, "\n")
        generate_sound(prase_output(response))

    
    save_conversation(english_tutor.message, save_file)
    clear_wav_files()
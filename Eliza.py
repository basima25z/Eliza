import re

def eliza_prompt():
    print('Hello, my name is Eliza, your therapist. What is your name?')
    name = input('> ')
    print(name)


if __name__=="__main__":
    eliza_prompt()
import re

def eliza_prompt():
    # print('Hello, my name is Eliza, your therapist. What is your name?')
    name = input('> ')
    # print(name)

    #sentance_to_search='My name is cassie'
    pattern = re.compile(r'[Mm]y name is (\w+)')

    matches = pattern.sub(r'Hi \1, how are you?', name)
    print(matches)


if __name__=="__main__":
    eliza_prompt()
import re

def eliza_prompt():
    # print('Hello, my name is Eliza, your therapist. What is your name?')
    name = input('> ')
    # match_object = re.match(r'[Mm]y name is (\w+)', name)
    # print(match_object.group(0))

    #TODOS
    # Get input --> see if it matches any sentances 
    # Once matches --> return a response 
    #keep cycling
    #  



    # print(name)

    #sentance_to_search='My name is cassie'
    pattern = re.compile(r'[Mm]y name is (\w+)')
    matches = pattern.sub(r'Hi \1, how are you?', name)
    print(matches)


    # match = re.match(r'[Mm]y name is (\w+)', name)
    # print(match.groups())

    #put into list
    #put corresponding into another list
    #for loop thru list --> when match is found --> note which index
    # go thru the second list of response to that same index 
    #print response


   # match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org') 
    # match_object = re.match(r'[Mm]y name is (\w+)', 'my name is basima')
    # print(match_object.group(1)) 

    #lets= regex.match(input).group()
    #print(lets)



#Hello_resp = [r"Hello \1, how are you?"]
#regex=[(re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling?")]

# def prompt():
#     print('Hello, my name is Eliza, your therapist. What is your name?')
#     name = input('> ')

#     if re.match(r"[Mm]y name is (\w+)", name):
#         print(re.sub(r"[Mm]y name is (\w+"), Hello_resp, name)
#     # for match, response in regex:
#     #     if match.match(name):
#     #         response = match.sub(r'Hi \1, how are you?', name)


#     # if re.search(r"[Mm]y name is (\w+)", name):
#     #     matches = re.sub(r'Hi \1, how are you?', name)
#     #     print(matches)

regex=[(re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling?")]
        

def eliza():
    print('Hello, my name is Eliza, your therapist. What is your name?')
    userInput =''
    
    while userInput != "exit":
        userInput=input(">>>")
    
        print(responses(userInput))

def responses(userInput):
    for key,value in regex:
        match = key.match(userInput).group(1)
        if key.search(userInput):
            value = value.replace(r'\1',match)
            print(match)
        
        return value





if __name__=="__main__":
    eliza()
import re

def eliza_prompt():
    # print('Hello, my name is Eliza, your therapist. What is your name?')
    name = input('> ')
    # match_object = re.match(r'[Mm]y name is (\w+)', name)
    match_object = re.match(r"[Ii] am feeling  (?:happy)", name )
    print(match_object.group(1))

    #TODOS
    # Get input --> see if it matches any sentances 
    # Once matches --> return a response 
    #keep cycling
    #  



    # print(name)

    #sentance_to_search='My name is cassie'
    # pattern = re.compile(r'[Mm]y name is (\w+)')
    # matches = pattern.sub(r'Hi \1, how are you?', name)
    # print(matches)


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

regex=[
    (re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling?"),
    (re.compile(r"[Ii] feel ([\w\s]+)"), r"How often do you feel \0?"),
    (re.compile(r"[Ii] am feeling (?:happy)"), r"Glad to hear! how did that happen?"),
    (re.compile(r"[[\w\s]+very often"), r"why do you feel that way often?"),
    (re.compile(r"(.*) brother (.*) "), r"Tell me about your brother.")
    ]
        

def eliza():
    # print('Hello, my name is Eliza, your therapist. What is your name?')
    # userInput =''
    
    # while userInput != "exit":
    #     userInput=input(">>>")
    
    #     print(responses(userInput))
    print('My name is Eliza, your personal therapist, What is your name?')
    s = ''
    while s != 'exit':
        try:
            s = input('>>> ')
        except EOFError:
            s = 'exit'
        print(responses(s))

        while s[-1] in '!.':
            s = s[:-1]

def responses(userInput):
    for key,value in regex:
        #match = key.match(userInput).group(1)
        if key.search(userInput):#match:
            if key.match(userInput).groups():
                match = key.match(userInput).group(1)
                print(match)
                response = value.replace(r'\0',match)
            #elif key.match(userInput).group(0):
                #response = value
            else:
                response=value
            
            return response
        #else:
            #print("no match")
            #return value
    
            # else:
            #     print("no group")



            #match = key.match(userInput).group(1)

            
            #response = value.replace(r'\0',match)
            #print(match)
        # else:
        # #     match= key.match(userInput).group(2)
        # #     print(match)
        
            


if __name__=="__main__":
    eliza()
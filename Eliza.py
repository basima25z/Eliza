import re

# def eliza_prompt():
#     # print('Hello, my name is Eliza, your therapist. What is your name?')
#     name = input('> ')
#     # match_object = re.match(r'[Mm]y name is (\w+)', name)
#     match_object = re.match(r"[Ii] am feeling  (?:happy)", name )
#     print(match_object.group(1))

#     #TODOS
#     # Get input --> see if it matches any sentances 
#     # Once matches --> return a response 
#     #keep cycling
#     #  



#     # print(name)

#     #sentance_to_search='My name is cassie'
#     # pattern = re.compile(r'[Mm]y name is (\w+)')
#     # matches = pattern.sub(r'Hi \1, how are you?', name)
#     # print(matches)


#     # match = re.match(r'[Mm]y name is (\w+)', name)
#     # print(match.groups())

#     #put into list
#     #put corresponding into another list
#     #for loop thru list --> when match is found --> note which index
#     # go thru the second list of response to that same index 
#     #print response


#    # match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org') 
#     # match_object = re.match(r'[Mm]y name is (\w+)', 'my name is basima')
#     # print(match_object.group(1)) 

#     #lets= regex.match(input).group()
#     #print(lets)



# #Hello_resp = [r"Hello \1, how are you?"]
# #regex=[(re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling?")]

# # def prompt():
# #     print('Hello, my name is Eliza, your therapist. What is your name?')
# #     name = input('> ')

# #     if re.match(r"[Mm]y name is (\w+)", name):
# #         print(re.sub(r"[Mm]y name is (\w+"), Hello_resp, name)
# #     # for match, response in regex:
# #     #     if match.match(name):
# #     #         response = match.sub(r'Hi \1, how are you?', name)


# #     # if re.search(r"[Mm]y name is (\w+)", name):
# #     #     matches = re.sub(r'Hi \1, how are you?', name)
# #     #     print(matches)

# regex=[
#     (re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling today?"),
#     (re.compile(r"[Ii] feel ([\w\s]+)"), r"Do you feel \0 often?"),
#     (re.compile(r"[Yy]es"), r"Can you please elaborate?"),
#     (re.compile(r"[Ii] am feeling (?:happy)"), r"Glad to hear! how did that happen?"),
#     (re.compile(r"[Ii] went to (?:the) ([\w\s]+)"), r"What did you do there?")
#     ]

regex=[
    (re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling today?"),
    (re.compile(r"[Ii] feel ([\w\s]+)"), r"Do you feel \0 often?"),
    (re.compile(r"sad|happy|worried|anxious|nervous|tired|normal|angry"), r"Do you feel that way often?"),
    (re.compile(r"[Yy]es"), r"Can you please elaborate?"),
    (re.compile(r"[Nn]o"), r"Can you please elaborate?"),
    (re.compile(r"[Nn]o (.*)"), r"Can you please elaborate?"),
    (re.compile(r"[Yy]es (.*)"), r"Can you please elaborate?"),
    (re.compile(r"[Ii] wish (.*)"), r"Why do you wish that?"),
    (re.compile(r"[Ii] am (.*)"), r"Why do you think you are \0?"),
    (re.compile(r"[Ii] want ([\w\s]+)"), r"Why do you want \0?"),
    (re.compile(r"[Ii] have (.*)"), r"I appreciate you telling me you have \0, what will you do next?"),
    (re.compile(r"[Ii] don't (.*)"), r"Why don't you \0?"),
    (re.compile(r"[Ii] do not (.*)"), r"Why do you not \0?"),
    (re.compile(r"[Ii] think (.*)"), r"Why do you think \0?"),
    (re.compile(r"[Ii] went (.*)"), r"How was \0?"),
    (re.compile(r"[Ii]t was (.*)"), r"Why was it \0?"), #
    (re.compile(r"[Ii] went to (?:the) ([\w\s]+)"), r"What did you do there?"),
    (re.compile(r"[Bb]ecause (.*)"), r"Well, why did you \0?"),
    (re.compile(r"(.*) friend (.*)"), r"Can you tell me more about your friend?"),
    (re.compile(r"(.*) brother (.*)"), r"Can you tell me more about your brother?"),
    (re.compile(r"(.*) sister (.*)"), r"Can you tell me more about your sister?"),
    (re.compile(r"(.*) mom (.*)"), r"Can you tell me more about your mom?"),
    (re.compile(r"(.*) dad (.*)"), r"Can you tell me more about your dad?"),
    (re.compile(r"(.*) maybe (.*) "), r"Are you not sure?"),
    (re.compile(r"[Ii] can't (.*)"), r"Why can't you \0?"),
    (re.compile(r"[Ii] cannot (.*)"), r"Why can you not \0?"),
    (re.compile(r"(.*?) sorry (.*?)"), r"Why are you saying sorry?"),
    (re.compile(r"[Ii] hate (.*)"), r"Why do you hate \0?"),
    (re.compile(r"[Ii] love (.*)" ), r"Why do you love \0?"),
    (re.compile(r"[Ii]\'?m (.*)"), r"Why do you think you're \0?"),
    (re.compile(r"[Hh]ello (.*)"), r"Hello, how are you today?"),
    (re.compile(r"(.*)"), r"Tell me more about this"),
    (re.compile(r"[Hh]e (.*)"), r"Why is he \0?"),
    (re.compile(r"[Ss]he (.*)"), r"Why is she \0?"),
    (re.compile(r"[Ii]t is (.*)"), r"Why is that \0?"),
    (re.compile(r"[Ii]t\'?s (.*)"), r"Why is that its \0?")
    ]
        

def eliza():
    print('My name is Eliza, your personal therapist, what is your name?')
    s = ''
    while s != 'exit':
        try:
            s = input('>>> ')
        except EOFError:
            s = 'exit'
        print(responses(s))

def responses(userInput):
    for key,value in regex:
        #match = key.match(userInput).group(1)
        if key.match(userInput):#if key.search(userInput):#match
            if key.match(userInput).groups(): #groups
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
        
            

#eliza()

if __name__=="__main__":
    eliza()
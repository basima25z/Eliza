#####################################
# Basima Zafar
# NLP Program 1
# 2/16/21
# V00825375
#####################################
import re


#####################################
# The problem being solved is creating a personal therapist for someone online. This is similar to contact support via a
# chatbot for a company, but instead this is for personal needs and conversation.
# The way this works is by word spotting, this means creating generic phrases like "I went x" and having Eliza respond with 
# well "why did you go to x". 
######################################

######################################
# EXAMPLE 1
# Eliza: Hi, my name is Eliza, what is your name?
# >>> My name is bas
# Eliza: Hi bas, how are you feeling today?
# >>> I feel sad
# Eliza: Do you feel sad often?
# >>> Yes
# Eliza: Can you please elobarate?
# >>> I have cancer
# Eliza: I appreciate you telling me you have cancer, what will you do next?
# >>> I want to go to the beach
# Eliza: Why do you want to go to the beach?
# >>> exit
# Eliza: Have a nice day

#EXAMPLE 2
# Eliza: Eliza: Hi, my name is Eliza, what is your name?
# >>> My name is Sam
# Eliza: Hi Sam, how are you feeling today?
# >>> worried 
# Eliza: Do you feel that way often?
# >>> yes
# Eliza: Can you please elobaroate?
# >>> I don't have a car
# Eliza: Why don't you have a car?
# >>> I think I am bad at saving
# Eliza: Why do you think you are bad at saving?
# >>> I think money is hard to save
# Eliza: Why do you think money is hard to save?
# >>> My dad never taught me the importance
# Eliza: Can you tell me more about your dad?
# >> exit
# Eliza: Have a nice day!
####################################################



# Regex listed below, most of them have [] with the first letter to account for the first letter of each sentance being 
# either uppercase or lowercase
# (.*): any whitespace or character as long as it's not a new line
# If the user do not enter any generic phrase, the last statement which is (.*) will encompass everything and Eliza will
# repsond with "Tell me more about this"
######################################
regex=[
    (re.compile(r"[Mm]y name is (\w+)"), r"Hi \0, how are you feeling today?"),
    (re.compile(r"[Ii] feel ([\w\s]+)"), r"Do you feel \0 often?"),
    (re.compile(r"[Ss]ad|[Hh]appy|[Ww]orried|[Aa]nxious|[Nn]ervous|[Tt]ired|[Nn]ormal|[Aa]ngry"), r"Do you feel that way often?"),
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
    (re.compile(r"[Ii] think [Ii] am (.*)"), r"Why do you think you are \0?"),
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
    (re.compile(r"[Hh]e (.*)"), r"Why is he \0?"),
    (re.compile(r"[Ss]he (.*)"), r"Why is she \0?"),
    (re.compile(r"[Ii]t is (.*)"), r"Why is that \0?"),
    (re.compile(r"[Ii]t\'?s (.*)"), r"Why is that its \0?"),
    (re.compile(r"[Ii] will (.*)"), r"When will you \0?"),
    (re.compile(r"[Ee]xit"), r"Have a nice day!"),
    (re.compile(r"(.*)"), r"Tell me more about this.")
    ]


#################################
# Function called eliza()
# First ouputs introduction prompt which the user will respond to
# s which is type string is empty, when s is not equal to exit will continue to get input from user
# When exit is entered --> exits program 
# calls method response which will generate responses from Eliza
###############################
        
def eliza():
    print('My name is Eliza, your personal therapist, what is your name?')
    s = ''
    while s != 'exit':
        try:
            s = input('>>> ')
        except EOFError:
            s = 'exit'
            

        print('Eliza: ' + responses(s))

##############################
# Function called repsponses
# Paramter: accepts a string
# Uses a for loop to traverse through dictionary
# key is what the input should match (regex), value is what eliza responds
# if the key(regex) matches the userInput, check if the key matches the groups, if so
# set it to the variable match
# if there is a match, then replace the \0 with the match found
# if there isn't a match, then respond with the value already stored there (no replacing)
##############################

def responses(userInput):
    for key,value in regex:
        if key.match(userInput):
            if key.match(userInput).groups(): 
                match = key.match(userInput).group(1)
                response = value.replace(r'\0',match)
            else:
                response=value
            
            return response

    

if __name__=="__main__":
    eliza()
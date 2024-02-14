import re
#1a. match regular expression regardless of single or plural
patternpluralsingle = r"Rats?"

textpluralsingle = "Rats"

singleplural = re.search(patternpluralsingle, textpluralsingle)

print(singleplural)

#1b. any number of a's followed by one exclamation mark

paternAa = r"[aA]*!$"

textAa = "aaAaaaa!"

aa = re.search(paternAa, textAa)

print (aa)

#1c. matches if any words exist to stop it [list of words(a, the, is , in,  for, where, when, to, at)]

patternStopWords = r".*a|the|is|in|for|where|when|to|at"

textStopWords = "some old man is in for a treat when I get to see him"

stopWords = re.search(patternStopWords, textStopWords)

print(stopWords)

#2 ELIZA Bot create an interface that accepts input and return an output based on input, using sub regex
def Eliza():   
    print("\n Hi I'm ELIZA your AI Therapy Bot!!! Tell me how you are feeling ;) (type in 'exit' to leave or .help for more options)")
    interface = True
    while(interface == True):
            x = input("Me: ")
            if (x.lower() == 'exit'):
                print("goodbye")
                interface = False
            elif (x.lower() == '.help'):
                print("These are your options to Type or you can tell me how you are feeling \nexit -- end program\n.angermode -- Real life Bot")
            elif(x.lower() == '.angermode'):
                print("ZALIE: ELIZA is Gone...It's time to have fun")
            else:
                response_to_question = responseprompt(x)
                print("ELIZA: "+ response_to_question)

#created a response prompt to apply to my Eliza Function
def responseprompt(response):
    
    compiler = re.compile(".*", re.IGNORECASE)
    patterns = [
        (r".*[Ii]’[Mm] (depressed|sad).*",  "I AM SORRY TO HEAR YOU ARE DEPRESSED OR SAD"),
        (r".*[Ii] [Aa][Mm] (depressed|sad).*", "WHY DO YOU THINK YOU ARE DEPRESSED OR SAD"),
        (r".*all", "IN WHAT WAY?"),
        (r".*always.*", "CAN YOU THINK OF A SPECIFIC EXAMPLE?")
    ]
    for pattern, solution in patterns:
        response = re.sub(pattern, solution, response)  
    return response


#run the program
full_interface = True

while full_interface == True:
     Eliza()


        
            
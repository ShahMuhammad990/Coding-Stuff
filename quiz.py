import random

#It will produce random word .
# And will return TUPPLE which has the property to return more than two words.
# i.e word and its defination.
def get_def_and_pop(word_list, word_dict):
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = word_dict.get(word)
    return word, definition

# It will split the rawstring in the word and its defination. and then return both of them.
def get_word_and_definition(rawstring):
   word, definition = rawstring.split(',', 1)
   return word, definition

# It will read from the given file and will store in the wd_list.
fh = open("Vocabulary_list.csv","r")
wd_list = fh.readlines()


# we are going to remove first element from list .
wd_list.pop(0)

# Now we have to make the list without duplications by writing in another file that is given as a 
# parameter and passing it through set. A set is list in python which donot allow duplicates in a list.
wd_set = set(wd_list)
fh = open("Vocabulary_set.csv","w")
fh.writelines(wd_set)


#Here we are getting definations and word and making a dictionary of definations of the word.
word_dict = dict()
for rawstring in wd_set:
    word,definition = get_word_and_definition(rawstring)
    word_dict[word] = definition #This is a list which will store the definations of the word.
    

#As for as we want to run.
while True:
	#we make choice list and run the loop 4 times
	#we are getting definations of the words and adding them to the choices' list.
	#and then shuffle the choices randomly with the function shuffle.
	
    wd_list = list(word_dict)
    choice_list= []
    for x in range(4):
        word,definition = get_def_and_pop(wd_list,word_dict)
        choice_list.append(definition)
    random.shuffle(choice_list) 
	
	#we are printing the choices and also ask user to put the correct choice.
	# If the choice is correct then it will display the correct! 
	# By entering 0 , user will exit the programe.
    print(word)
    print("-----------")
    for idx,choice in enumerate(choice_list):
        print(idx+1,choice)
    choice = int(input("1,2,3,or 4; 0 to exit"))
    if choice_list[choice-1] == definition:
         print("Correct:\n")
    elif choice == 0:
       exit(0)
    else:
          print("Incorrect\n")
    
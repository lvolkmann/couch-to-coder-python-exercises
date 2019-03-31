"""
Write a program by the following:
1.	Define a function that accepts a string and prints every other word
2.	Define a function that accepts a string and translates it into pig latin
3.	If time, implement them into a main loop
"""

def iCantHearYou(words: str)->str:
    """Accepts a string and returns every other word back"""
    word_list = words.split()
    every_other_word = ""
    every_other = False
    for word in word_list:
        if every_other == True:
            every_other_word += (word + " ")
            every_other = False
        else:
            every_other = True
    print("WHAT DID YOU SAY??? I ONLY HEARD:",  every_other_word)

def igLatinPay(words: str)->str:
    """Accepts a string and returns it translated into Pig Latin"""
    word_list = words.split()
    translation = ""
    for word in word_list:
        first_letter = word[0]
        the_rest = word[1:]
        translation += (the_rest + first_letter + "ay ")
    return translation

def get_input():
    """Gets user choice of 1 2 or 3"""
    while True:
        choice = int(input("What do you want from me?"))
        if choice in range(1,4):
            return choice
        print("WRONG")

menu = "Hello Earthlings!\nI have two friends for you!\n1.Old Man Jones\n2.MiddleSchool Roman\n3.No one. There is no one for me\n"


while True:
    print(menu)
    choice = get_input()
    if choice == 1:
        iCantHearYou(input("WHAT?"))
    elif choice == 2:
        print(igLatinPay(input("ellohay")))
    else:
        print("You're right. There is no one for you")    
        break
    print()
    
            
    

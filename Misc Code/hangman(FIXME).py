import urllib.request as url
import random as rand

def parse_words(data):

    words = []
    
    for line in data:
        line = line.decode("utf-8")
        if line[0] == "<":
            continue
        end = line.find("<P>")
        word = line[:end].strip().upper()
        if word.isalpha():
            words.extend(word.split())
            
    return words

def display_guesses_left(guesses_remaining):
    
    print("<3 " * guesses_remaining)
    print("You have:", guesses_remaining)

def display_guessed(guessed):
    
    print("You have already guessed:", guessed)

#Fix the following functions
def display_word(word, visible_key):
    """Displays correctly guessed character and _ otherwise"""

    pass

def check_word(word, guess, visible_key):
    """Checks if guess is correct, updates visibility tracker accordingly, and returns bool
    Return True if correct and False otherwise"""

    pass

def get_guess(guessed):

    """Gets guess and implements appropriate error handling
    Char must be 1 character long
    Char cannot have been guessed before
    Char must be a letter
    Return uppercase version of guessed"""

    pass
    
def check_win(visible_key):

    """Check for win; Returns a bool"""

    pass

def hangman(word_lst):
    
    #FIXME: Get random word

    word = None

    #FIXME: Initialize means of
    #tracking characters to display

    visible = None

    #Guesses
    guesses_remaining = 10
    guessed = []

    #Win Condition
    win = False

    #Main Loop
    while guesses_remaining > 0 and not win:

        #Won't display first time
        if len(guessed) > 0:
            display_guessed(guessed)
        
        display_guesses_left(guesses_remaining)
        display_word(word, visible)
        guess = get_guess(guessed)
        hit = check_word(word, guess, visible)
        
        if hit:
            print("Way to go!")
        else:
            print("Nope!")
            guessed.append(guess)
            guesses_remaining -= 1
            
        win = check_win(visible)
        print()

    if win:
        print("You win! The word was:" , word)
    else:
        print("You are bad at this. The word was:", word)


word_site = url.urlopen("http://members.optusnet.com.au/charles57/Creative/Techniques/random_words.htm")
data = word_site.readlines()
word_lst = parse_words(data)

hangman(word_lst)



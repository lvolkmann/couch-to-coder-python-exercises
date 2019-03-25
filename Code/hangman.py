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

def display_word(word, visible_key):

    for i in range(len(word)):
        letter = word[i]
        state = visible_key[i]
        if state:
            print(letter, end=" ")
        else:
            print("_", end=" ")

def check_word(word, guess, visible_key):

    i=0
    correct = False
    for letter in word:
        if letter == guess:
            visible_key[i] = True
            correct = True
        i += 1
    return correct

def get_guess(guessed):

    while True:
        try:
            guess = input("Guess a letter").upper()
            if guess in guessed:
                raise ValueError(guess)
            if not guess.isalpha():
                raise TypeError
            if len(guess) != 1:
                raise Exception
            return guess
        
        except ValueError as ex:
            print("You've already guessed:", ex)
        except TypeError:
            print("You must choose a letter!")
        except:
            print("Try again")

def display_guesses_left(guesses_remaining):
    print("<3 " * guesses_remaining)
    print("You have:", guesses_remaining)

def display_guessed(guessed):
    print("You have already guessed:", guessed)
    
def check_win(visible_key):

    for state in visible_key:
        if state == False:
            return False
    return True


def hangman(word_lst):
    word = rand.choice(word_lst)

    visible = []
    for i in range(len(word)):
        visible.append(False)
    
    guesses_remaining = 10
    guessed = []

    win = False

    while guesses_remaining > 0 and not win:

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



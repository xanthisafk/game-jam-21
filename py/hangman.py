import random

h1 = """  +---+
    |
    |
    |
   ==="""

h2 = """  +---+
 0  |
    |
    |
   ==="""

h3 = """  +---+
 0  |
 |  |
    |
   ==="""

h4 = """  +---+
 0  |
/|  |
    |
   ==="""

h5 = """  +---+
 0  |
/|\ |
    |
   ==="""

h6 = """  +---+
 0  |
/|\ |
/   |
   ==="""

h7 = """  +---+
 0  |
/|\ |
/\  |
   ==="""

hangmen = [h1, h2, h3, h4, h5, h6, h7]

words = ["story", "penny", "peace", "south", "witch", "sense", "chaos", "blank", "valid", "rough", "chief", "relax", "fraud", "drain", "onion", "donor", "stock", "sword", "begin", "scene", "dirty", "fence", "panic", "orbit", "refer",
         "score", "gloom", "swell", "smart", "brink", "arise", "cabin", "heart", "debut", "alarm", "ferry", "lunch", "utter", "faint", "ready", "slump", "chair", "serve", "frank", "awful", "moral", "terms", "state", "style", "adopt"]

word = random.choice(words)

tries = 6
correct = '_'*len(word)
incorrect = ''
found = []


def gameloop():
    global word
    global tries
    global found
    global correct
    global incorrect

    correct = "_" * len(word)

    while tries != 0:
        render(missed=incorrect,correct=correct)
        guesser()
        rt = checker()
        tries -= 1
        if rt in ['win','lose']:
            break
    con(rt)


def render(missed, correct):
    global hangmen

    display = correct

    miss = ''

    for i in missed:
        miss += f'{i}, '

    miss = miss[:-2]

    if correct != None:
        screen = f"H A N G M A N\n{hangmen[len(missed)]}\n{display}\nMissed words: {miss}"

    else:
        screen = f"H A N G M A N\n{hangmen[len(missed)]}\n{display}\nMissed words: {miss}"

    print(screen)


def guesser():
    global word
    global correct
    global incorrect
    global found

    while True:
        guess = input("Guess a character: ")
        if guess in found:
            print("You already guessed that.")
        elif guess == '':
            print("You need to guess something...")
        elif guess in '1234567890':
            print("It does not contain a number")
        else:
            found.append(guess)
            break


    if guess in word:
        correct += guess
    else:
        incorrect += guess


def checker():
    global correct
    global word
    global tries
    global found

    temp = "_"*len(word)
    temp = list(temp)
    
    for i in range(len(word)):
        if word[i] in correct:
            temp[i] = word[i]
            found.append(i)
    


    temp = "".join(temp)

    correct = temp

    if correct == word:
        return "win"
    elif tries == 0:
        return "lose"

def con(condition):
    global word
    global tries
    if condition == 'win':
        print(f"Congratulations! You win!! 🎊 The word was {word}")
        return
    elif condition == 'lose':
        print(f'Sorry you lose')
    elif tries == 0:
        print("Out of tries. sorry 😥")

def reset():
    global word
    global tries
    global words
    global correct
    global incorrect
    global found

    word = random.choice(words)
    tries = 6
    correct = incorrect = ''
    found = []

def play():
    gameloop()

if __name__ == '__main__':
    play()
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice == 'yes' or choice == 'y':
            reset()
            play()
        else:
            break

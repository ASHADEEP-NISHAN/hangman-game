import random as r
word_list=[
    "cat", "dog", "elephant", "lion", "tiger", "giraffe", "zebra", "monkey", "kangaroo", "dolphin",
    "apple", "banana", "orange", "grape", "strawberry", "watermelon", "pear", "kiwi", "mango", "pineapple",
    "sparrow", "eagle", "hawk", "robin", "pigeon", "parrot", "owl", "crow", "duck", "swan",
    "rabbit", "hamster", "guinea pig", "squirrel", "ferret", "chinchilla", "rat", "mouse", "gerbil", "hedgehog",
    "peacock", "flamingo", "penguin", "ostrich", "emu", "turkey", "chicken", "goose", "quail", "pheasant",
    "strawberry", "blueberry", "raspberry", "blackberry", "cranberry", "cherry", "plum", "apricot", "peach", "fig",
    "giraffe", "hippo", "rhino", "crocodile", "alligator", "snake", "lizard", "turtle", "tortoise", "gecko",
    "wolf", "fox", "coyote", "hyena", "jackal", "lynx", "panther", "cougar", "bobcat", "cheetah",
    "elephant", "rhinoceros", "hippopotamus", "buffalo", "gorilla", "orangutan", "chimpanzee", "bonobo", "lemur", "koala",
    "jellyfish", "octopus", "starfish", "clam", "lobster", "shrimp", "crab", "squid", "nautilus", "coral",
    "koala", "kangaroo", "wombat", "platypus", "wallaby", "possum", "echidna", "cassowary", "quokka", "numbat",
    "ladybug", "butterfly", "dragonfly", "ant", "bee", "wasp", "moth", "grasshopper", "cricket", "spider"

]

hangman_stages = [
    """
       _________
      |         |
                |
                |
                |
                |
    """,
    """
       _________
      |         |
      O         |
                |
                |
                |
    """,
    """
       _________
      |         |
      O         |
      |         |
                |
                |
    """,
    """
       _________
      |         |
      O         |
     /|         |
                |
                |
    """,
    """
       _________
      |         |
      O         |
     /|\\       |
                |
                |
    """,
    """
       _________
      |         |
      O         |
     /|\\       |
     /          |
                |
    """,
    """
       _________
      |         |
      O         |
     /|\\       |
     / \\       |
                |
    """
]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
word=r.choice(word_list)
# print(word)
l=len(word)
display=[]
for i in range(l):
   display+="_"
print(display)
# while not word
split=list(word)
chance=7
s=0
while display != split and chance >0:

    if chance > 0:
        letter_guess = input("\nguess a letter").lower()

        if letter_guess not in word:
            print("wrong guess")
            print(hangman_stages[s])


            chance = chance - 1
            s=s+1
        else:
            for j in range(l):
                letter = word[j]
                if letter == letter_guess:
                    display[j] = letter
            print(display)
if chance == 0:
    print("\nyou lose")
    print("THE WORD IS:",word)
else:
    print("\ncongratulations you guess the word")
    print("THE WORD IS:", word)


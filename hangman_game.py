import random as r
word_list=['apple','mango','orange']
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
else:
    print("\ncongratulations you guess the word")



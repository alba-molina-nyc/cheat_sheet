"""

1. ask the user for a word, 
2. translate that word into Ubbi Dubbi. 
This is a slightly different task than we had with Pig Latin, because we need to operate on a letter-by-letter basis. 
We can’t simply analyze the word and produce out- put based on the entire word. 

Moreover, we have to avoid getting ourselves into an infinite loop, in which we try to add ub before the u in ub.
The solution is to iterate over each character in word, adding it to a list, output. If the current character is a vowel, then we add ub before the letter. Otherwise, we just add the letter. At the end of the program, we join and then print the letters together. This time, we don’t join the letters together with a space character (''), but rather with an empty string (''). This means that the resulting string will consist of the letters joined together with nothing between them—or, as we often call such collections, a word.


elephant, you’ll output ubelubephubant
"""
def ubbi_dubbi():
    word = input("enter an English word that you'd like translated to ubi dubi here: ")
    ubbi_dubbi_translator = []
    ub = 'ub'
    print(ub)

    while word != None: 
        for w in word:
            if w in 'aeiou':
                vowel_ubbi = ub + w
                ubbi_dubbi_translator.append(vowel_ubbi)
                print(ubbi_dubbi_translator)
                continue
            elif w not in 'aeiou':
                ubbi_dubbi_translator.append(w)
                print(ubbi_dubbi_translator)
                continue
        break

ubbi_dubbi()
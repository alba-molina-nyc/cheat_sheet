"""

1. ask the user for a word, 
2. translate that word into Ubbi Dubbi. 
This is a slightly different task than we had with Pig Latin, because we need to operate on a letter-by-letter basis. 
We can’t simply analyze the word and produce out- put based on the entire word. 

Moreover, we have to avoid getting ourselves into an infinite loop, in which we try to add ub before the u in ub.
The solution is to iterate over each character in word, adding it to a list, output. If the current character is a vowel, then we add ub before the letter. Otherwise, we just add the letter. At the end of the program, we join and then print the letters together. This time, we don’t join the letters together with a space character (''), but rather with an empty string (''). This means that the resulting string will consist of the letters joined together with nothing between them—or, as we often call such collections, a word.


elephant, you’ll output ubelubephubant
"""


def real_ubbi_dubbi():
    word = input('please enter here a word to translate to Ubbi Dubbi: ')
    ubbi_dubbi_word = ''
    vowels = "aeiou"


    for w in word:
            if w not in vowels:
                ubbi_dubbi_word = ubbi_dubbi_word + w
                print(ubbi_dubbi_word)
            else:
                for v in vowels: 
                    if v in word:  
                        ubbi_dubbi_word = ubbi_dubbi_word + 'ub' + w
                        print(ubbi_dubbi_word)
                        break


    

real_ubbi_dubbi()


# print(dir(str))



# person enters a word through word
# translation to ubbi dubbi = before every vowel add "ub"  ubbi_dubbi_word.append(w)
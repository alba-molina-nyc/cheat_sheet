# write a function pig_latin
# if word begins with vowel (a,e,i,o,u -> add way to end of word)
# if word begins with any other letter, take first letter and add it to the end of the word AND add 'ay'

# grab input from user 
# initialize variable to hold vowel
# initialize variable to hold consonant

# first off translate one word 
# then translate sentence 

def pig_latin():
    word = input("Enter an English sentence to translate it to pig latin: ")
    vowels = ["a", "e", "i", "o", "u"]
    for w in word:
        if w in word[:1] in vowels:
            vowel_word = word + "way"
            print(vowel_word, 'we are returning the vowel word')
            break
        elif w not in word[:1]:
            first_letter = word[0]
            consonant_word = word[1:] + first_letter + 'ay'
            print(consonant_word, 'we are returning the consonant word')
            break


# TODO: figure out which version is better the one above or the one down here
# def pig_latin():
#     word = input("Enter an English sentence to translate it to pig latin: ")
#     vowels = ["a", "e", "i", "o", "u"]
#     for w in word:
#         if w in word[:1] in vowels:
#             vowel_word = word + "way"
#             return vowel_word
#         elif w not in word[:1]:
#             first_letter = word[0]
#             consonant_word = word[1:] + first_letter + 'ay'
#             return consonant_word

# pig_latin()

    

    

   

            
            
           

            
            

pig_latin()

#My new Language
'''

'''
def translate(phrase):
    place_holder = "g"
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
           translation = translation + place_holder
        else:
           translation = translation+ letter
    return translation;
               
phrase = input("Enter the phrase: ")    

print(translate(phrase))     
    
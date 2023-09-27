##################################################
# Name: Andrew Cerqui
# Collaborators: got help trouble shooting with chat GPT
# Estimated time spent (hr): 1.5
##################################################

def to_obenglobish(word):
    obenglobish_word = ""
    vowels = "aeiou"

    for i in range(len(word)):
        # Checks if the current letter is a vowel
        if word[i] in vowels:
            # If the first letter is a vowel it adds ob to beginning
            if i == 0:
                obenglobish_word += "ob"
            # Adds ob before vowel as long as the previous letter is not a vowel
            elif word[i - 1] not in vowels:
                obenglobish_word += "ob"
        # Checks if last character is E and then doest not add ob
        elif word[i] == 'e' and i == len(word) - 1:
            pass
        # Add the current character to the Obenglobish word
        obenglobish_word += word[i]

    return obenglobish_word







if __name__ == '__main__':
    # Some testing printouts for your use!
    print(f"to_obenglobish('english') gives {to_obenglobish('english')}.")
    print(f"to_obenglobish('gooiest') gives {to_obenglobish('gooiest')}.")
    print(f"to_obenglobish('amaze')   gives {to_obenglobish('amaze')}.")
    print(f"to_obenglobish('rot')     gives {to_obenglobish('rot')}.")

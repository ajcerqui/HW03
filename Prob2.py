#######################################
# Name: Andrew Cerqui
# Collaborators: NA
# Estimated time spent (hr): .75
#######################################

from english import ENGLISH_WORDS
##I had trouble downloading ENGLISH_WORDS

# Part A
def contains_repeated_letters(word):
    seen = set()
    for letter in word:
        if letter in seen:
            return True
        seen.add(letter)
    return False
##for each letter in the word it checks if the letter is seen again, if so it returns True, if not it returns false





# Part B
def longest_no_repeats():
    longest_word = ""
    for word in words:
        if not contains_repeated_letters(word) and len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Finds the longest word with where letters dont repeat and it stores it
result = longest_no_repeats()
print("Longest word with no repeated letters:", result)
#prints the longest word!!





if __name__ == '__main__':
    # Part A
    print(contains_repeated_letters("single"))
    print(contains_repeated_letters("repeating"))

    # Part B
    print(longest_no_repeats()) #Uncomment when you've finished Part B

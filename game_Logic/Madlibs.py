# Madlibs Game It is a word filling game. 
# where the user is prompted to enter different types of words (nouns, verbs, adjectives, etc.) 
# Those words are inserted into a pre-written story template to create a funny or interesting story.

print("Welcome to the Madlibs Game!")
print("Please enter the following words:")

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

# its better not to use profanity in the madlibs game as it is meant to be fun and suitable for all ages.

story = f"The {adjective} {noun} {verb} {adverb}."
print(story)
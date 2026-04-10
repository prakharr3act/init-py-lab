# Madlibs Game It is a word filling game. 
# where the user is prompted to enter different types of words (nouns, verbs, adjectives, etc.) and then those words are inserted into a pre-written story template to create a funny or interesting story.

print("Welcome to the Madlibs Game!")
print("Please enter the following words:")

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

story = f"The {adjective} {noun} {verb} {adverb}."
print(story)
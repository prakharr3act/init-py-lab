# if = do something if a condition is true
# else = do something if the condition is false

no_Of_Contributions = int(input("How many contributions have you made? "))
if no_Of_Contributions > 80:
    print("You are a top contributor")
    # elif (else if in other languages) = do something if the previous conditions were false and this condition is true
elif no_Of_Contributions > 50:
    print("You are a good contributor")
elif no_Of_Contributions > 20:
    print("You need to contribute more")
else:
    print("You have not contributed enough")

response =  input("What is your favorite programming language? ")
if response == 'python':
    print("Python is a great language")
elif response == 'java':
    print("Java is a great language")
else:
    print("That's a good language too!")
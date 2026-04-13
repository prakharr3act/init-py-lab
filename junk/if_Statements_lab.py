# if = do something if a condition is true
# else = do something if the condition is false

no_Of_Contributions = int(input("How many contributions have you made? "))
if no_Of_Contributions > 80:
    print("You are a top contributor")
    # elif (else if in other languages) = do something if the previous conditions were false and this condition is true
elif no_Of_Contributions > 50:
    print("You are a good contributor")
else:
    print("You need to contribute more")

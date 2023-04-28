print("Hello, welcome to my computer qize!")

plying = input("Do you want to play? ")
if plying.lower() != "yes":
    quit("Ok, Bay")
print("OK,  let's play :) ")
score = 0

answer = input("What represent: resistor? ")
if answer.lower() == "r" :
    print("Correct!")
    score += 1
else:
    print("Incorrect! :( )")

answer = input("What comes after A? ")
if answer.lower() == "a+":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :( )")

answer = input("What was the first answer you wrote? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :( )")

print("You got " + str(score) + " answers right!")
print("You got " + str((score/3)*100) + "%.")
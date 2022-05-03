print("welcome to my computer")

playing = input("Do you wnat to play?")

#print(playing)
if playing.lower() != "yes":
    quit()

print("okay! let's play :)")
score = 0
answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = +1
else: 
    print("Incorrect!")

answer = input("What does GPU Stand for? ")
if answer.lower() == "Graphic processing unit":
    print("Correct!")
    score = +1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "Random access memores":
    print("Correct!")
    score = +1
else: 
    print("Incorrect!")

answer = input("what does psu stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score = +1
else: 
    print("Incorrect!")
print("you got "  + str(score) +  " correct questions" )
print("you got "  + str((score / 4) * 100) +  "%" )
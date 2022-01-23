print("Welcome to my computer quiz! \n")

playing=input("Do You want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok, Let's Play :D \n")
score = 0
answer= input("What does CPU stand for?\n ")

if (answer.lower() == "central processing unit"):
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")
    print("The right answer is central processing unit")


answer= input("\nWhat does RAM stand for?\n ")
if (answer.lower() == "random access memory"):
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")
    print("The right answer is random access memory")


answer= input("\nWhat does GPU stand for?\n ")
if (answer.lower() == "graphics processing unit"):
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")
    print("The right answer is graphics processing unit")


answer= input("\nWhat does PSU stand for?\n ")
if (answer.lower() == "power supply unit"):
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")
    print("The right answer is power supply unit")

answer= input("\nWhat does bit stand for?\n ")
if (answer.lower() == "binary digit"):
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")
    print("The right answer is binary digit")

print("You got " + str(score) + " questions correct \n")
percentage = (score/5)*100
print("You got " + str(percentage) +'%' )

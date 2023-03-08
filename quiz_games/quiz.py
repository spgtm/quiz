from time import sleep
print("Welcome to the Quiz Game. Please choose the game type")
sleep(0.50)
print("1. MCQ Game")
sleep(0.50)
print("2. No MCQ")
sleep(0.60)
choice = input("Enter Your choice 1. or 2.")
ch_choice = int(choice)
score = 0

if (ch_choice ==1):
    print("What is the capital city of Nepal?")
    print("1.   Biratnagar")
    print("2.   Kathmandu")
    print("3.   Hetauda")
    choice = int(input("Enter correct answer 1,2 or 3: "))
    if(choice == 2):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is Kathmandu")


    print("Who is the first scientist of Nepal?")
    print("1.   Sudip Gautam")
    print("2.   Gyanendra Shumsher")
    print("3.   Gahendra Shumsher")
    choice = int(input("Enter correct answer 1,2 or 3: "))
    if(choice == 3):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is Gahendra Shumsher")


    print("What is the actual height of Mt. Everest?")
    print("1.   8848.86")
    print("2.   8848.68")
    print("3.   8848.87")
    choice = int(input("Enter correct answer 1,2 or 3: "))
    if(choice == 1):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is 8848.86")


    print("Which country won the world cup 2022")
    print("1.   Brazil")
    print("2.   France")
    print("3.   Argentina")
    choice = int(input("Enter correct answer 1,2 or 3: "))
    if(choice == 3):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is Argentina")

    if(score == 4):
        print("You score full marks 4 outof 4")
    if(score >=2 and score < 4):
        print(f"Congratulation You score ",score, "outof 4")
    if(score <2):
        print(f"Poor, ",score,"out of 4")

if(ch_choice == 2):
    choice = input("What is the capital city of Nepal? ")
    
    if(choice == "kathmandu"):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is kathmandu")


    choice =input("Who is the first scientist of Nepal? ")
    if(choice == "gahendra shumsher"):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is gahendra shumsher")


    choice =input("What is the actual height of Mt. Everest? ")
    if(choice == "8848.86"):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is 8848.86")


    choice = input("Which country won the world cup 2022")
    if(choice == "argentina"):
        score +=1
        print("Hurray! Correct")
    else:
        print("correct answer is argentina")


    if(score == 4):
        print("You score full marks 4 outof 4")
    if(score >=2 and score < 4):
        print(f"Congratulation You score ",score, "outof 4")
    if(score <2):
        print(f"Poor, ",score,"out of 4")
    sleep(1000)
  

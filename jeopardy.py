# Jeopardy Game
sel_cat=input("Welcome to Jeopardy! " '\n'
    "The categories are" '\n'
    "PROGRAMMING   JMU" '\n'
    "300           300" '\n'
    "Enter a catagory and value" '\n'
    '\n')
     
if sel_cat == "Programming 300" or "programming 300" or "PROGRAMMING 300":
    p300_ans=input("PROGRAMMING 300" '\n'
        "Question blah blah" '\n'
        '\n'
        "a. Python IDLE b. Sublime c. pytest " '\n'
        "Please enter a or b or c: ")
    if p300_ans == "a" or "A":
        print("Correct!")
    else:
        print("Wrong")
if sel_cat == "JMU 300" or "jmu 300":
    print("yay")



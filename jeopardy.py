
# Jeopardy Game
usr_ipt=input("Welcome to Jeopardy! " '\n'
      "The categories are" '\n'
              "PROGRAMMING   JMU" '\n'
              "300           300" '\n')

y=int(usr_ipt)
usr_ans=input("What text editor do we use? "
              "a. Python IDLE b. Sublime c. pytest "
              "Please enter a or b or c: ")
if y == "PROGRAMMING" :
    print("Wrong")
elif y <= 150 :
    print("ALIVE")
elif y > 150 :
    print("VAMPIRE")

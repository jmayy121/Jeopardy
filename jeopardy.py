# Jeopardy Game
import os
import time
import sys
clear = lambda: os.system('clear') #on Linux System

def programming_100():
    p100_ans=str(input("PROGRAMMING 100" '\n'
        "What programming language does Dr. Benton know the best?" '\n'
        '\n'
        "a. Python b. Sublime c. JavaScript " '\n'
        "Please enter a or b or c: "))
    if p100_ans == "c" or p100_ans == "C":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def programming_200():
    p200_ans=str(input("PROGRAMMING 200" '\n'
        "What is the title of the book we read for the first half of the semester?" '\n'
        '\n'
        "a. Code 4 Your Life b. CODE c. Coding 101 " '\n'
        "Please enter a or b or c: "))
    if p200_ans == "b" or p200_ans == "B":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def programming_300():
    p300_ans=str(input("PROGRAMMING 300" '\n'
        "What is Lance's favorite programming language?" '\n'
        '\n'
        "a. Python b. Java c. JavaScript " '\n'
        "Please enter a or b or c: "))
    if p300_ans == "a" or p300_ans == "A":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def jmu_100():
    jmu100_ans=str(input("JMU 100" '\n'
        "What gender has a majority at JMU?" '\n'
        '\n'
        "a. Male b. Female c. Other " '\n'
        "Please enter a or b or c: "))
    if jmu100_ans == "b" or jmu100_ans == "B":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def jmu_200():
    jmu200_ans=str(input("JMU 200" '\n'
        "Who is the President of JMU?" '\n'
        '\n'
        "a. Jonathan R. Alger b. Ronald E. Carrier c. Linwood H. Rose " '\n'
        "Please enter a or b or c: "))
    if jmu200_ans == "a" or jmu200_ans == "A":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def jmu_300():
    jmu300_ans=str(input("JMU 300" '\n'
        "When was JMU founded?" '\n'
        '\n'
        "a. 1908 b. 1899 c. 1912 " '\n'
        "Please enter a or b or c: "))
    if jmu300_ans == "a" or jmu300_ans == "A":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def isat_100():
    isat100_ans=str(input("ISAT 100" '\n'
        "What does ISAT stand for?" '\n'
        '\n'
        "a. Intergral Science and Technology b. Information Systems and Technology c. Integrated Science and Technology " '\n'
        "Please enter a or b or c: "))
    if isat100_ans == "c" or isat100_ans == "C":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def isat_200():
    isat200_ans=str(input("ISAT 200" '\n'
        "Who is the nicest guy in the world?" '\n'
        '\n'
        "a. Dr. Tony Chen b. Donald Trump c. Paul Henriksen " '\n'
        "Please enter a or b or c: "))
    if isat200_ans == "a" or isat200_ans == "A":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
def isat_300():
    isat300_ans=str(input("ISAT 300" '\n'
        "Who is the dean of ISAT?" '\n'
        '\n'
        "a. Paul Henriksen b. Dr. Bob Kolvoord c. Amanda Biesecker " '\n'
        "Please enter a or b or c: "))
    if isat300_ans == "b" or isat300_ans == "B":
        print("Correct!")
    else:
        print("Wrong")
    sys.stdout.flush()
    time.sleep(5)
    clear()
cat_p_100 = "100"
cat_p_200 = "200"
cat_p_300 = "300"
cat_j_100 = "100"
cat_j_200 = "200"
cat_j_300 = "300"
cat_i_100 = "100"
cat_i_200 = "200"
cat_i_300 = "300"
print("Welcome to Jeopardy!" '\n')
condition = True
while condition :
    sel_cat=str(input(
    "The categories are" '\n'
    "PROGRAMMING   JMU        ISAT" '\n'
    "   " + cat_p_100 +"        " + cat_j_100 +"        " + cat_i_100 +"        " '\n'
    "   " + cat_p_200 +"        " + cat_j_200 +"        " + cat_i_200 +"        " '\n'
    "   " + cat_p_300 +"        " + cat_j_300 +"        " + cat_i_300 +"        " '\n'
    "Enter a catagory and value" '\n'
    '\n'))
    clear()
    if sel_cat == "programming 100" or sel_cat == "Programming 100" or sel_cat == "PROGRAMMING 100":
        programming_100()
        cat_p_100 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "programming 200" or sel_cat == "Programming 200" or sel_cat == "PROGRAMMING 200":
        programming_200()
        cat_p_200 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "programming 300" or sel_cat == "Programming 300" or sel_cat == "PROGRAMMING 300":
        programming_300()
        cat_p_300 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "JMU 100" or sel_cat == "jmu 100":
        jmu_100()
        cat_j_100 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "JMU 200" or sel_cat == "jmu 200":
        jmu_200()
        cat_j_200 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "JMU 300" or sel_cat == "jmu 300":
        jmu_300()
        cat_j_300 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "ISAT 100" or sel_cat == "isat 100":
        isat_100()
        cat_i_100 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "ISAT 200" or sel_cat == "isat 200":
        isat_200()
        cat_i_200 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "ISAT 300" or sel_cat == "isat 300":
        isat_300()
        cat_i_300 = "   "
        if cat_p_100 == cat_p_200 == cat_p_300 == cat_j_100 == cat_j_200 == cat_j_300 == cat_i_100 == cat_i_200 == cat_i_300 == "   " :
            condition = False
    elif sel_cat == "exit" :
        sys.exit()
    else :
        print("Please Enter A Valid Catagory")
print("Game Over")





import random
pick = int(input("enter your choice? rock(1)  paper(2) and scissor(3)"))
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if pick == 1:
    print(f"your choice is rock \n {rock}")
elif pick == 2:
    print(f"your choice is paper \n {paper}")
elif pick == 3:
    print(f"tour choice is scissors \n {scissors}")
else:
    print("select appropriate choice..!")

if pick == 1 or pick == 2 or pick == 3:
    computer_random = random.randint(1,3)
    if computer_random == 1:
        print(f"computer choice is rock\n {rock}")
    elif computer_random == 2:
        print(f"computer choice is paper\n {paper}")
    else:
        print(f"computer choice is scissors\n {scissors}")
else:
    print("try again")

if computer_random == 1 and pick == 2:
    print("you win...!")
elif computer_random == 2 and pick == 3:
    print("you win...!")
elif computer_random == 3 and pick == 1:
    print("you win...!")
elif computer_random == 1 and pick == 3:
    print("computer win...!")
elif computer_random == 2 and pick == 1:
    print("computer win...!")
elif computer_random == 3 and pick == 2:
    print("computer win...!")
else:
    print("it's a draw..!")

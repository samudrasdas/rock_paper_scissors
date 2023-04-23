import random
exit=False
usr_point=0
system_point=0

#initializing list of choices
while exit==False:
    choice_list=["rock","paper","scisssor"]
    first_choice=random.choice(choice_list)
    print("Enter your choice: ")
    usr_input=input("Enter rock, paper,scissors or exit: ")

    if usr_input=="exit":
        exit=True
        print("Game ended")
        print("Points are-player point=",usr_point,"computer point=",system_point)
        if usr_point==0 and system_point==0:
            print("No one won the game ")
        elif usr_point==system_point:
            print("Its a tie!")
        elif usr_point>system_point:
            print("You won the game!!")
        else:
            print("computer won the game!!!")
    
    elif usr_input.lower()==first_choice:
        print("You are tie!") 

#when user input is rock
    elif usr_input.lower()=="rock":
        if first_choice=="scissors":
            print("Computer choice was ",first_choice)
            print("You got the point!")
            usr_point+=1
        elif first_choice=="paper":
            print("Computer choice was ",first_choice)
            print("computer got the point!")
            system_point+=1
        else:
            print("Its a tie")

#when user input is paper
    elif usr_input.lower()=="paper":
        if first_choice=="scissor":
            print("Computer choice was ",first_choice)
            print("computer got the point!")
            system_point+=1
        elif first_choice=="rock":
            print("Computer choice was ",first_choice)
            print("You got the point!")
            usr_point+=1
        else:
            print("Its a tie!")

#when user input is scissor
    elif usr_input.lower()=="scissor":
        if first_choice=="rock":
            print("Computer choice was ",first_choice)
            print("computer got the point!")
            system_point+=1
        elif first_choice=="paper":
            print("Computer choice was ",first_choice)
            print("You got the point!")
            usr_point+=1
        else:
            print("Its a tie!")
    else:
        print("Invalid input")
    







    

name=input("Ener your name : ").upper()
print("Welcome",name,"to this adventure !")

play=input("Are you ready for an exiciting adventure : Yes/No ").lower()
if(play=="no"):
    print("Okay !,see you next time . Bye  \n")
    quit()

print("Yoo !, Let's go ...\n ****** The Forest shadows ******")
print("GOAL: \n Escape the mysterious forest by making smart choices.You'll face wild beasts,  a river with threats,and an abandoned cave with secrets.")

user=input("You're on a dirt road deep in the forest. The path ends abruptly.Do you go left or right ? ").lower()
if(user=="left"):
    user=input("You walk into a dark forest. You hear growling.Do you climb a tree or run? ").lower()
    if(user=="climb"):
        print("You see a pack of wolves pass below. You're safe for now.")
        print("You survived by climbing")
        user=input("Now move forward or quit ? ").lower()
        if(user=="forward"):
            print("Yoo you got out of the forest safely ! But no tressure found :),better luck next time")
        else:
            quit()
    elif(user=="run"):
        print("You fall into a pit . Game over !")
    else:
        print("Wrong choice ! Better luck next time !")

elif(user=="right"):
    user=input("You see a river flowing rapidly.Do you want to swim across or build a raft ? ").lower()
    if(user=="swim"):
        print("Oops , there are crocodiles . Game over !")
    elif(user=="raft"):
        print("You cross safely and find a glowing cave.")
        user=input("See what's inside the cave or return back ? Press yes for cave and no for returning back ").lower()
        if(user=="yes"):
            print("Hurrayyy !You found the tressure !")
            print("Congratulations ! You won .")
        elif(user=="no"):
            print("You're Safe .Well played !")
        else:
            print("Wrong choice ! Better luck next time !")
    else:
        print("Wrong choice ! Better luck next time !")
    

else:
    print("Wrong choice ! Better luck next time !")

print("Played well !",name)

        

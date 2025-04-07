#【author】-------------
# Nanae Shimoi

#【theme】--------------
# text based adventure game

#【step】---------------
#(start)
#1,ask firs question
#2,player can choose 「LEFT」 or 「RIGHT」
#3,「LEFT」→ go to river tunnel
#4,「RIGHT」→go to mushroom runnel

#(level 2)
#5,「LEFT」→”Do you want to SWIM across or FOLLOW the riverbank?”
#6,「RIGHT」→”Do you want to EAT a mushroom or KEEP walking?”

#(level 3)
#7,「SWIM」→"Do you want to OPEN the chest or LEAVE it?"
#8,「EAT」→ "Do you want to WAIT for help or TRY to move?"

#【to do list】-------------
#(start)
#1,use”print("")”-------ask firs question

#(choice1)
#2,use"choice1= input("").strip().lowew(),if choice1 =="":print(""),elif choice1=="":print(""),else:print("")"

#(level 2)
#3,use"choice2 =input("").strip().lowew() ,if choice2 == "swim",print(""),elif choice2="",print(""),else:("")"

#(level 3)
#4,use"choice3= input("").strip().lowew(),if choice3 =="":print(""),elif choice3 =="":print(""),else:print("")"

#【assignment】-------------



print("You can find yourself in a dark cave with two tunnels ahead.")
choice1 = input ("Do you want to go LEFT or RIGHT?").strip().lower()
if choice1 == "left":
     print("You enter a tunnel that leads to an underground river.")
    
     choice2 = input("Do you want to SWIM across or FOLLOW the riverbank?").strip().lower()
     if choice2 == "swim":
          print("You swim across the river and find a treasure chest.")
          
          choice3 = input("Do you want to OPEN the chest or LEAVE it?").strip().lower()
          if choice3 == "open":
               print("Congratulations! You found a pile of gold and escaped the cave!")        
         
          elif choice3 == "leave":
               print("You walk away , but the cave collapses behind you. You are trapped forever!")
          
          else:
               print("Invalid choice. You wander aimlessly in the cave.")

     elif choice2 == "follow":
            print("Following the riverbank , you find an exit and escape the cave.")
   
     else:
          print("Invalid choice. You slip and fall into the river.")

elif choice1 == "right":
     print("You enter a tunnel filled with strange glowing mushroom.")

     choice2 = input("Do you want to EAT a mushroom or KEEP walking?").strip().lower()
     if choice2 == "eat":
          print("The mushroom makes you dizzy, and you faint.")

          choice3 = input("Doyou want to WAIT for help or TRY to move?").strip().lower()
          if choice3 == "wait":
               print("A mysterious figure helps you escape the cave. You are safe!")

          elif choice3 == "try":
               print("You stumble and fall mushroom effects overwhelm you.")
     elif choice2 == "keep":
           print("You keep waling and find as ancient artifact. You escape the cave!")
     else: 
          print("Invalid choice.You are lost in the glowing tunnel.")
else:
     print("Invalid choice.You remain at the cave enterance, paralyzed by indecision.")

     print("ご視聴ありがとうございます。")
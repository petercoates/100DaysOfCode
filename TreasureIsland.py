print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|            
''')
print("Welcome to Treasure Island!! \nYou are stranded on an island \n"
      "Your mission is to find the treasure. \n"
      "Goodluck!!!")
direction = input('You\'re at a crossroad and need to move, '
                  'enter what direction you want to go, "LEFT" or "RIGHT"?: \n').lower()
if direction == 'left':
    swimOrWait = input("You've made it to the lake!!!."
                       " Type 'SWIM' to swim across to land or "
                       "Type 'WAIT' to wait for a boat : \n").lower()
    if swimOrWait == 'wait':
        colour = input("Lovely! You made it an island unharmed!! \n"
                       "There is a house with three doors, One Red, One Blue or One Yellow."
                       " Which door colour do you wanna open?: \n").lower()
        if colour == 'yellow':
            print(''' You did it!!!!!!!! here is the treasure
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
            ''')
        elif colour == "blue":
            print("You were attacked by Snakes!!!. Game Over")

        elif colour == "red":
            print("Fire!!!!! Run. Game Over!")

        else:
            print("Wrong key entered. Game Over!!")
    else:
        print("You drowned. Game over!!!")

else:
    print("Wrong move. You fell off. Game Over!!!")

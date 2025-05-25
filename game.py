print(r'''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go?\n Type 'Left' or 'right'\n")

if choice1 == 'right':
    print("Fall into a hole. Game Over!")

if choice1 == 'left':
     choice2 = input("You've come to a lake. there is an island in the middle of the lake. \n Type 'wait' to wait for a boat. Type 'swim to swim across.'")
     if choice2 == 'swim':
         print("Attacked by a Great Shark. Game Over!")
     if choice2 == 'wait':
         choice3 = input("You arrive at the island unharmed. there is a house with 3 doors.\n one red, one yellow and one blue. Which color do you choose?")
         if choice3 == 'red':
             print("Burned by fire. Game over!")
         elif  choice3 == 'blue':
             print("Eaten by 100 beasts. Game Over!")
         elif  choice3 == 'yellow':
            print("Great Job! You found the Treasure! You Win!!!!")


else:
    print("You typed in the wrong input!");

# Rescue from the Ofendasaurus text-based Adventure game.

def game():
    print("Hi, welcome to the Rescue from the Ofendasaurus. Here you are and you are in a very tight situation as the ofendasaurus has caused destruction in the city. It is a green coloured, single-blue eyed, hairless, three-legged monstrous creature which is about 20 foot tall 😱. And, the bad news is, the creature is after you ! You must run to save your life and here you have two options, head towards the forest 🌲🌲🌲 or head towards a train tunnel 🚇. Make your choice fast.")

    user = input("What do you want to do ? (forest/tunnel): ")

    if user == "forest":
        print("Okay, let's head towards the forest but mind you, the Ofendasaurus is following you. He is faster than you ! You should find a place to hide as fast as possible, you have 2 options, head towards a cave or head cross a river.")
        user = input("Where do you want to go ? (cave/river): ")
        if user == "cave":
            print("Cave, oooooo... Let's head towards the cave. Oh no !!! There's a lion here. But wait wait wait... The lion's attention is attracted by the Ofendasaurus as the creature was outside and you were inside in the dark. Fortunately, the ofendasaurus got scared and ran away and you slipped silently out of the cave and survived !!! 🥳")

        elif user == "river":
            print("River, okay. Let's head towards the river ! The ofendasaurus is behind you aaannd... You made it !, you made it to the river !!! And he creature who had not taken bath forever as it hated water ran away and you survived !!! 🥳")

        else:
            print("Invalid Input !!! \n Sometimes, by mistake, you enter a wrong choice and also it costs you, so the ofendasaurus was behind you and it caught you. 😥")
            print("Well, do you want to try again and perform better ?")
            user = input("yes/no: ")
            if user == "yes":
                game()

            elif user == "no":
                print("Okay, no problem 😔 \n See you again 😀")

            else:
                print("😔😕")

    elif user == "tunnel":
        print("Train Tunnel !!! mmm.... okay, Let's go towards the tunnel, just one doubt that there should not be any train coming 😥. You made it to the tunnel and as the creature cannot go into the darkness, it is still outside. Wait... There is a sound of the horn of a train ! You are right in the middle of the tunnel and cannot run outside just in time to survive from the train, so you lie flat sideways along the walls of the tunnel hoping to survive aaannd... Wooaahh !!! You got saved, and guess what ! The ofendasaurus got hit by the train and it died, you managed to get out, ALIVE !!! 🥳")

    else:
        print("Invalid Input !!! \n Well, sometimes, by mistake, you enter a wrong choice and it costs you, so the ofendasaurus was behind you and it caught you. 😥")
        print("Well, do you want to try again and perform better ?")
        user = input("yes/no: ")
        if user == "yes":
            game()

        elif user == "no":
            print("Okay, no problem 😔 \n See you again 😀")

        else:
            print("😔😕")

# Running the program.
game()
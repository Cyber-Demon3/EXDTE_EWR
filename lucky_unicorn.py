import random

#this will print a welcoming message
print("Welcome to Lucky Unicorn. Get ready to test your luck.")

#this code asks the user to input an amount that they want to bet
bet = int(input("How much do you want to bet? "))

if bet > 150:
    print("You can't bet higher than 150, please run the program again.")

else:
    #this while loop allows the user to keep on playing
    keep_going=""
    while keep_going =="":
        
        print("")
        #this code picks a random animal from the list inside the sqaue brackets
        animals = ["Donkey", "Horse", "Zebra", "Unicorn", "Chicken", "T-Rex", "Donkey", "Horse", "Zebra", "Chicken", "Donkey", "Horse", "Zebra", "Unicorn", "Donkey", "Horse", "Zebra", "Horse" "Donkey", "Zebra"]
        animal = random.choice(animals)
        print(animal)
        print("")
        #all of the following if statements below are the different results that can happen

        if animal == "Unicorn":
            #unicorn is going to triple your money
            bet = bet * 3
            print("You won:")
            print(bet)
            print("")
        
        if animal == "Donkey":
            #donkey will end up havling you money
            bet = bet / 2
            print("Your money just got halved")
            print(bet)
            print("")
        
        if animal == "Zebra":
            #zebra is going to do nothing
            bet = bet
            print("Nothing got added to your bet")
            print(bet)
            print("")
        
        if animal == "Horse":
            #This will take away $50 from your bet
            bet = bet - 50
            print("You just lost 50 dollars off your bet")
            print(bet)
            print("")
        
        if animal == "Chicken":
            #chicken is going to take away your money and put you at $20
            bet = bet - bet
            bet = bet + 20
            print("You've been reset to 20 dollars")
            print(bet)
            print("")
        
        if animal == "T-Rex":
            #T-Rex is going to multiply your bet by 10
            bet = bet * 10
            print("JACKPOT!")
            print(bet)
            print("")

        if bet <= 0:
            keep_going = "no"
        if bet > 0:
            #this asks if the user would like to continue or stop by typing quit
            keep_going = input("Press enter to continue or type anything else to quit ")

#this will tell the user that the program has stopped
print("Game Over!")  

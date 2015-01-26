# Date: Jan26  
  
# Write a program named guess.py that plays the 'number guessing game'. The computer will choose a random number between 1 and 100, and ask the user to guess the number, giving them a hint if it's high or low. 

import random
computer = random.randint(1,100)
print computer # Used for debugging

name = raw_input("Hello! Can I get your name, please? ")
print
print "Here are the rules, %s. You need to guess a number between 1 and 100, and I will tell you how you're doing.\nReady to play? Just type in your guess below.\n" %name

guess = int(raw_input("First number? "))

count = 1
if count ==1 and guess == computer:
    print "Wow, first guess!"
else:
    while guess != computer:
        count += 1
        if guess < computer:
            print "You're too low. Try again"
        else:
            print "Your guess is too high. Try again" 
             
        guess = int(raw_input("New number? "))
    print "Finally,you guessed the number in", count, "tries."   

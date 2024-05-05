#Getting persons name
name = input("What's your name? ")

#Welcoming person to quiz and telling them the topic
print("Welcome to the quiz", name)
print("The quiz topic is general knowledge")

#Asking person the questions and telling them the answers
answer1 = input("What is Obama's last name? ")

if answer1 == "Obama":  
    print("That's correct, Obama is his last name, very good!")

else:
    print("That's incorrect, your silly")
    print("The correct answer is Obama")

answer2 = input("What costs more, a trip to space or a coffee from ponsonby? ")

if answer2 == "a coffee from ponsonby":
    print("That's correct, You obviously live in Auckland! ")

else:
    print("That's incorrect")
    print("The correct answer is a coffee from ponsonby, You obviously don't live in Auckland ")


answer3 = input("What is bigger the population of China or the population of road cones around Auckland?")

if answer3 == "the population of road cones around auckland":
    print("Very good that is absolutely correct!")

else:
    print("That incorrect")
    print("The correct answer is the population of road cones around auckland")

#Thank person for playing
print("Thank you for playing!")


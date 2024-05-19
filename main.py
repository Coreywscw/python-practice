play = "yes"
while play == "yes":
    score = 0
    QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"

    #Getting persons name
    name = input("What's your name? ")

    #Welcoming person to quiz and telling them the topic
    print("Welcome to the quiz", name)
    print("The quiz topic is general knowledge")
    while True:
        try:
            tries = int(input("How many attempts do you want at each question? 1-4 "))
            tries = int(tries)
            break
        except:
            print("That's not a number")
    #Asking person the questions and telling them the answers
    
    answer1 = input("What is Obama's last name? ").lower()

    if answer1 == "Obama".lower() :  
        print("That's correct, Obama is his last name, very good!")
        score += 1
    elif answer1 == "" :
        print("Not sure?")
    else:
        print("That's incorrect, your silly")
        print("The correct answer is Obama")
        
    answer2 = input("What costs more, a trip to space or a coffee from ponsonby? (answer space or coffee) ").lower()

    if answer2 == "Coffee".lower() :
        print("That's correct, You obviously live in Auckland! ")
        score += 1
    elif answer2 == "" :
        print ("Not sure?")

    else:
        print("That's incorrect")
        print("The correct answer is a coffee from ponsonby, You obviously don't live in Auckland ")


    answer3 = input("What is bigger the human population of China or the population of road cones around Auckland? (Answer Humans or Road cones) ").lower()

    if answer3 == "Road cones".lower() :
        print("Very good that is absolutely correct!")
        score += 1
    elif answer3 == "" :
        print("Not sure?")

    else:
        print("That's incorrect")
        print("The correct answer is the population of road cones around auckland")

    question = ("What is the strongest type of wood?")
    a = " Oak wood from minecraft"
    b = " Cedarwood"
    c = " Teakwood"
    d = " Australian Buloke "
    answer4 = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()

    if answer4 == d or answer4 == "d":
        print("That's correct! ")
        score += 1
    elif answer4 == "" :
        print ("Not sure?")
    elif answer4 != a and answer4 != "a" and answer4 != b and answer4 != "b" and answer4 != c and answer4 != "c" and answer4 != d and answer4 != "d" :
        print ("That wasn't an option! ")
    else:
        print("That's incorrect")
        print("The correct answer is d Australian Buloke")
    play = input(" Do you want to play again?").lower()
# Thank person for playing
print("Thank you for playing {}, your final score was {}".format(name, score))

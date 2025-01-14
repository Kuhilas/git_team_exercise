def main ():
    while True:
        print("Welcome to quiz appliaction!")
        choice = input("Would you like to play? y/n ")
        if choice in ("y", "yes", "Yes", "Y"):
            score = quiz_1()
            newgame = end(score)
            if newgame == 0:
                pass
            else:
                print("Thanks. bye!")
                break
                
        elif choice in ("n", "no", "No", "N"):
            print("Good bye!")
            break
        else: 
            pass

def quiz_1():
    score = 0
    print("Welcome to the quiz! Please give the answer in format yyyy, E.g: 1600")
    answers = [1300,1800,1800]
    q1 = "In which century did the Hundred Years' War between England and France begin?"
    q2 = "In which century did the American Civil War take place?"
    q3 = "In which century did the Napoleonic Wars occur?"
    questions = [q1,q2,q3]
    index = 0
    for question in questions:
        print(question)
        try:
            answer = int(input("Answer: "))
            if answer == answers[index]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
            index += 1
        except ValueError:
            print("Wrong format!")
    return score
  
def end(score):
    print(f"Your score was: {score} points")
    play_again = input("Do you want to play again? ")

    if play_again in ("y", "yes", "Yes", "Y"):
        return 0
    else:
        return 1
 
  
if __name__ == "__main__":
    main()

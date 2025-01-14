def end(score):
    print(f"Your score was: {score} points")
    play_again = input("Do you want to play again? ")

    if play_again in ("y", "yes", "Yes", "Y"):
        return 0
    else:
        return 1

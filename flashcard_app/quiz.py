
import random
from flashcard import Flashcard

def start_quiz(flashcards):
    score = 0
    for card in random.sample(flashcards, len(flashcards)):
        print("Q:", card.question)
        ans = input("Your answer: ")
        if ans.strip().lower() == card.answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! The answer was:", card.answer)
    print(f"Your final score: {score}/{len(flashcards)}")

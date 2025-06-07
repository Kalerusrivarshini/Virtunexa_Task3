
from flashcard import Flashcard
from quiz import start_quiz
from calculator import calculator
import json
import os

flashcards = []

def load_flashcards():
    global flashcards
    if os.path.exists("flashcards.json"):
        with open("flashcards.json", "r") as f:
            data = json.load(f)
            flashcards = [Flashcard(d['question'], d['answer']) for d in data]

def save_flashcards():
    with open("flashcards.json", "w") as f:
        json.dump([{'question': fc.question, 'answer': fc.answer} for fc in flashcards], f)

def main():
    load_flashcards()
    while True:
        print("\n1. Add Flashcard\n2. Start Quiz\n3. View Flashcards\n4. Calculator\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            q = input("Enter question: ")
            a = input("Enter answer: ")
            flashcards.append(Flashcard(q, a))
            save_flashcards()
        elif choice == "2":
            start_quiz(flashcards)
        elif choice == "3":
            for i, fc in enumerate(flashcards):
                print(f"{i+1}. Q: {fc.question} | A: {fc.answer}")
        elif choice == "4":
            calculator()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

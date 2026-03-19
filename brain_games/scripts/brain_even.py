import random

from brain_games.cli import welcome_user

ROUNDS = 3


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(ROUNDS):
        number = random.randint(1, 100)
        correct = "yes" if number % 2 == 0 else "no"
        print(f"Question: {number}")
        answer = input("Your answer: ")
        if answer != correct:
            print(
                f"'{answer}' is wrong answer. Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

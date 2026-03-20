import math
import random

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds_count = 3

    for _ in range(rounds_count):
        num1 = random.randint(1, 100)  # NOSONAR
        if num1 > 50:
            num2 = num1 - random.randint(1, 50)  # NOSONAR
        else:
            num2 = num1 + random.randint(1, 50)  # NOSONAR

        correct_answer = math.gcd(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

import random

import prompt


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 10)

    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = " ".join(progression)

    return question, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    rounds_count = 3

    for _ in range(rounds_count):
        question, correct_answer = generate_progression()

        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

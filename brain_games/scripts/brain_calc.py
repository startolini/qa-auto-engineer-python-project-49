import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    
    operations = ['+', '-', '*']
    rounds_count = 3
    
    for _ in range(rounds_count):
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        operation = random.choice(operations)
        
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:  # operation == '*'
            correct_answer = num1 * num2
        
        print(f'Question: {num1} {operation} {num2}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
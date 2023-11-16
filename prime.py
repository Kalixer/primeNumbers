def isprime(num):
    prime = True

    if num == 1:
        prime = False
    elif num == 2: 
        prime = True
    elif num % 2 == 0:
        prime = False
    else:
        i = num - 1
        while i > 1:
            if num % i == 0:
                prime = False
                break
            else:
                prime = True
            i -= 1
    return prime


if __name__ == '__main__':
    print('Welcome to prime numbers')
    user_choice = int(input(
'''
What do you want to do
1: Print prime numbers
2: Evaluate if a number is prime
'''))
    if user_choice == 1:
        print(
'''
You selected the 1st choice
It will be printed a list of prime numbers between a range you will choose
''')
        min_range = int(input('Select the min number: '))
        max_range = int(input('Select the max number: '))

        for i in range(min_range, max_range):
            primo = isprime(i)
            if primo == True:
                print(i)

    elif user_choice == 2:
        print('You selected the 2nd choice')
        number_chosen = int(input('Input the number to know if is prime: '))
        primo = isprime(number_chosen)
        if primo:
            print(f'The number {number_chosen} is prime')
        else:
            print(f'The number {number_chosen} is not prime')

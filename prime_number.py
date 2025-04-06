
def input_checker(user_input):
    try:
        return int(user_input)
    except:
        return user_input


def number_validation():

    while True:
        user_input = input('Please Enter a number: ')
        val = input_checker(user_input)
        if (isinstance(val, str)):
            print('Please a valid input a number!!!')
            continue
        if isinstance(val, int):
            if int(user_input) == 0 or int(user_input) == 1:
                print(user_input, "is not a prime number")
                continue
            else:
                return int(user_input)

        else:
            print('Invalid Input')
            continue


def prime_number_checker():
    number = number_validation()
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return print(f'{number}, is not a prime number')
            else:
                return print(f'{number}, is a prime number')


prime_number_checker()

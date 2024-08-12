
def get_int():
    while True:
        try:
            user_num = int(input("Please enter a positive integer: \n"))
            if user_num > 0:
                return user_num
            else:
                print("This program only accepts positive integers...")
        except ValueError:
            print("This program only accepts integers...")


def loop_break():
    while True:
        end_loop = input("Would you like to enter another number?(y/n) \n").lower()

        if end_loop == 'y' or end_loop == 'n':
            return end_loop
        else:
            print("Please respond with either y for yes or n for no.\n")


print("Learn your squares and cubes!")
while True:
    # calls user function to enter a positive integer input
    user_int = get_int()

    # setting up the table to show squared and cubed numbers
    print("Number    Squared     Cubed")
    print("=======   =======     ======")

    for i in range(1, user_int + 1):
        print(f"{i}   \t\t{i**2}\t\t\t{i**3}")

    # calls a validation function to make sure user only responds yes or no
    user_break = loop_break()
    if user_break == 'n':
        break


def get_int():
    while True:
        try:
            user_num = int(input("Please enter a positive integer for the range you would like to see: \n"))
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
        print(f"{i}", " "*(8-len(str(i))),
              f"{i**2}", " "*(10-len(str(i**2))),
              f"{i**3}")

    # multiplication table header
    print("This is a multiplication table for the range you chose!")
    print("\t", end="")
    for i in range(1, user_int + 1):
        print(f"{i}", " "*(3-len(str(i))), end="")
        if i == user_int:
            print()
    print("\t", end="")
    for i in range(1, user_int + 1):
        print("=", " "*(3-len(str(i))), end="")
        if i == user_int:
            print()

    # setting up format for each row
    multiply = 1
    while multiply != user_int + 1:

        print(f"{multiply} | ", end="")

        for i in range(1, user_int + 1):
            print(f"{i*multiply}", " "*(3-len(str(i*multiply))),
                  end="")

            if i == user_int:
                print()
        multiply += 1

    print()
    # calls a validation function to make sure user only responds yes or no
    user_break = loop_break()
    if user_break == 'n':
        break

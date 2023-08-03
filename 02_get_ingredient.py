# checks that users input is not blank

def not_blank(prompt, error):
    while True:
        response = input(prompt)
        if response == "":
            print(f"{error}. Please try again.")
        else:
            return response

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error messages

product_name = not_blank("What is the name of the recipe? ", "Sorry - "
                  "the product name can't be blank, please try again")

def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:

            print(error)

# main routine goes here
while True:
    print("press <xxx> when you have all your ingredients")

    print()

    #ask user if they want to end program
    again = input("What ingredients would you like to use?")

    # if the user presses <xxx> end the loop
    if again!="xxx":
        break

    print()

# asks user to decide yes or no
def yes_no(question):
    valid = False

    while not valid:

        response = input(question).lower()

        if response == "yes" or response == "y":

            return "yes"
        elif response == "n" or response == "no":

            return "no"
        else:

            print("Please answer yes / no")
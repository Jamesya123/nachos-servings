import math


# integer that is more than zero. Takes in custom error messages
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


# rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


# Main routine starts here
how_many = num_check("How many items?", "Can't be 0", int)
total = num_check("Total Costs?", "More than 0", float)
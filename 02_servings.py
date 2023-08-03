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


how_many = num_check("How many people are you making for? ",

                     "Please enter an amount that is more than 0", int)
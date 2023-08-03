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

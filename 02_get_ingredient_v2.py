import pandas


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
all_ingredient_unit = []
all_ingredient_amount = []
all_ingredient_price = []
all_ingredient_name = []
all_cost_per_unit = []
all_recipe_amount = []

recipe_dict = {
    "ingredient": all_ingredient_name,
    "ingredient unit": all_ingredient_unit,
    "ingredient amount": all_ingredient_amount,
    "ingredient price": all_ingredient_price,
    "unit cost": all_cost_per_unit,
    "recipe amount": all_recipe_amount
}

# Get product name

recipe_name = not_blank("What is the name of the recipe? ", "Sorry - "
                                                            "the product name can't be blank, please try again")

how_many = num_check("How many people are you making for? ",

                     "Please enter an amount that is more than 0", int)

print()

# all_cost_per_unit = ""
# ingredient_amount = ""
# cost_per_unit = ""
# ingredient_name = ""

while True:

    ingredient_name = not_blank("What is the name of the ingredients that you are using?",

                                "Your answer can't be blank")

    if ingredient_name == 'xxx' and len(all_ingredient_name) > 0:

        break

    elif ingredient_name == 'xxx':

        print("You must enter an ingredient name")

        continue

    ingredient_price = num_check("How much did you buy the ingredient for?",
                                 "please enter a valid number", float)

    print()

    ingredient_unit = input("Enter the unit of the ingredients: ")
    print()

    ingredient_amount = num_check("How much did you buy (in grams)?",

                                  "please enter a valid number", float)

    ingredient_name = input("Enter the name of the ingredient: ")
    print()

    recipe_amount = num_check(" Enter the recipe amount:",

                              "please enter a valid number", float)

    print()

    cost_per_unit = (ingredient_price / ingredient_amount * recipe_amount)

# add content to list!
all_ingredient_name.append(ingredient_name)
all_ingredient_unit.append(ingredient_unit)
all_ingredient_amount.append(ingredient_amount)
all_ingredient_price.append(ingredient_price)
all_cost_per_unit.append(cost_per_unit)
all_recipe_amount.append(recipe_amount)

# make the panda..
recipe_panda_frame = pandas.DataFrame(recipe_dict)

recipe_panda_frame['Recipe Cost'] = \
    recipe_panda_frame['unit cost'] / 1.15

print(recipe_panda_frame)

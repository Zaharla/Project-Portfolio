import requests # Importing the requests module to make API calls
import time # Importing the time module for loading effect

# Welcome message
print ( """
Welcome to the Recipe Generator!
Find delicious recipes based on the ingredients you have at home. 
Need to avoid allergens? We've got you!
Let's get cooking!!!
""")

# Function to suggest common ingredients
def suggest_ingredients ():
    """suggest common ingredients that are sometimes used in meals. """ # Use of docstring to explain the purpose of the function
    common_ingredients = ["chicken", "beef", "rice", "egg", "potato", "carrot", "milk", "bread", "spinach"]
    print ("\ncommon ingredients you might want to try: ")
    for ingredient in common_ingredients:
        print(f" * {ingredient}")

# Function to fetch recipes based on ingredients
def fetch_recipes(ingredients):
    """Fetch recipes using the ingredients provided by the user."""
    endpoint = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredients}" #API endpoint for filtering by ingredients
    response = requests.get (endpoint) #Making a call to the API

    if response.status_code !=200:
        print("Failed to fetch recipes. Please try again.")
        return [] #Return an empty list if the recipes are not found.

    # Convert the JSON response into a Python dictionary
    data = response.json ()
    meals = data.get ("meals", [])

    return meals # Return the lists of meals that are fetched from the API

# Function to fetch full recipe details
def fetch_recipe_details (meal_id):
    """Fetch full recipe details for a given meal ID."""
    details_endpoint = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    details_response = requests.get(details_endpoint)

    if details_response.status_code != 200:
        return None # If details cannot be fetched to return as none

    details = details_response.json().get ("meals", [])
    if not details :
        return None # Return as none if details are not available

    return details [0] # Return the first meal's details

#Function to filer meals based on allergen
def filter_allergen (meals, allergy) :
    """Filter out meals containing the allergen."""
    filtered_meals = [] # empty list to store filtered meals

    for meal in meals:
        meal_id = meal.get ("idMeal")
        if not meal_id:
            continue # skip this meal if there's no meal ID

        details = fetch_recipe_details(meal_id)
        if not details:
            continue # skip if no details are available

        ingredients_list = [
            details.get(f"strIngredient{i}", "").strip ()
            for i in range (1,21)
            if details.get(f"strIngredient{i}") # ensure valid ingredients
        ]

        # Check for allergens (case-insensitive search)
        contains_allergens = (
                 allergy and any(allergy.lower() in ingredient.lower() for ingredient in ingredients_list)
        )

        if not contains_allergens:
            filtered_meals.append({
                "name": details.get("strMeal", "Unknown"),
                "instructions": details.get("strInstructions", "No instructions available."),
                "ingredients": ingredients_list
            })

    return filtered_meals # return the list of filtered meals

# Function to display and save recipes to file
def display_and_save_recipes(filtered_meals):
    """Display the filtered recipes to the user and save them to a file."""
    with open("recipe_output.txt", "w", encoding="utf-8") as file: # set encoding to UTF-8 to fix EncodeError
            print("\nHere are your recipes! ")
            file.write("Here are your recipes! \n")
            for i, recipe in enumerate (filtered_meals [:10], start=1): # Limit to 10 recipes
                print (f"-Recipe {i}: {recipe ['name']}")
                print(f"Ingredients: {','.join(recipe['ingredients'])}")
                print(f"Instructions:\n{recipe['instructions']}\n")

                file.write(f"Recipe {i}: {recipe['name']}\n")
                file.write(f"Ingredients: {','.join(recipe['ingredients'])}\n")
                file.write(f"Instructions:\n{recipe['instructions']}\n")
# The main Loop
while True:
    # Ask for ingredients suggestions before searching
    suggest_ingredients()

    #Get user input. Strip () will remove extra spaces
    ingredients = input ("\n Enter ingredients (comma-separated): ").strip()
    allergy = input ("Enter an allergy to filter out (e.g., gluten, diary, nuts):").strip ()

    # Display loading effect while waiting for input
    print("Searching for recipes...please wait :)")
    time.sleep (1) # Adds a 1-second delay for the loading effect

    # fetch recipes based on ingredients
    meals = fetch_recipes(ingredients)

    if not meals:
        print("No recipes found with the given ingredients.")
    else:
        # filter recipes based on allergy
        filtered_meals = filter_allergen(meals, allergy)

        # display and save the recipes to a file
        display_and_save_recipes(filtered_meals)

    # Ask the user if they want to search again
    search_again = input ("\nDo you want to search for more recipes? (yes/no): "). strip().lower()
    if search_again != "yes":
        print("\n Thank you for using the Recipe Generator! Your results have been saved to a file for your review. Happy cooking!")
        break
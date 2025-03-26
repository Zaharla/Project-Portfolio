## Recipe Generator

### Overview  
The Recipe Generator is a Python application that helps users find recipes based on the ingredients they have at home. It also allows users to filter recipes by allergens. The app fetches data from an API and displays recipe details while saving the results to a file.  

### Features  

- **Ingredient-based Recipe Search:** Find recipes based on available ingredients.  
- **Allergen Filter:** Exclude recipes containing specified allergens (e.g., gluten, dairy, nuts).  
- **Save Results:** Saves filtered recipes to a text file for later reference.  

### Requirements  

- Python 3.x  
- `requests` module (install using `pip install requests`)  

### How to Use  

1. Run the script in a Python environment.  
2. Enter ingredients and allergens when prompted.  
3. The app fetches recipes, filters out allergens, and displays up to 10 recipes.  
4. Results are saved to `recipe_output.txt`.  

### Example  

Welcome to the Recipe Generator!
Enter ingredients: chicken, rice
Enter an allergy: dairy

Searching for recipes...

Here are your recipes:
- Recipe 1: Chicken Curry
Ingredients: chicken, rice, curry powder, coconut milk
Instructions: Cook chicken, add curry powder and coconut milk, simmer.

The results have been saved to a file.
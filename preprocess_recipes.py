import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_cookbook(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into recipes
    recipes = re.split(r'\n\s*\n', text)

    processed_recipes = []
    for recipe in recipes:
        # Check if the text chunk looks like a recipe
        if 'ingredients' in recipe.lower() and 'instructions' in recipe.lower():
            # Extract title
            title_match = re.match(r'(.+?)(?:\n|$)', recipe)
            title = title_match.group(1).strip() if title_match else "Untitled Recipe"

            # Extract ingredients
            ingredients_match = re.search(r'ingredients:(.*?)(?:instructions|$)', recipe, re.DOTALL | re.IGNORECASE)
            if ingredients_match:
                ingredients = ingredients_match.group(1).strip()
                ingredients = [item.strip() for item in re.findall(r'[-•]\s*(.+)', ingredients)]
            else:
                ingredients = []

            # Extract instructions
            instructions_match = re.search(r'instructions:(.*?)(?:\n\n|$)', recipe, re.DOTALL | re.IGNORECASE)
            if instructions_match:
                instructions = instructions_match.group(1).strip()
                instructions = [step.strip() for step in re.split(r'\d+\.|\n', instructions) if step.strip()]
            else:
                instructions = []

            # Combine important parts
            important_text = f"===RECIPE_START===\ntitle: {title.lower()}\n\ningredients:\n"
            important_text += "\n".join(f"- {ingredient.lower()}" for ingredient in ingredients) + "\n\ninstructions:\n"
            important_text += "\n".join(f"{i+1}. {step.lower()}" for i, step in enumerate(instructions))
            important_text += "\n===RECIPE_END===\n"

            # Remove stop words but keep numbers and measurements
            stop_words = set(stopwords.words('english')) - {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
            words = word_tokenize(important_text)
            important_words = [word.lower() for word in words if word.lower() not in stop_words or word.isdigit() or any(char.isdigit() for char in word)]

            processed_recipes.append(" ".join(important_words))

    # Write processed text to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n\n".join(processed_recipes))

if __name__ == "__main__":
    preprocess_cookbook('books/examplebook_extracted_text.txt', 'books/processed_recipes.txt')
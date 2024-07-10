import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_cookbook(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into recipes
    recipes = re.split(r'\n(?=\w+:)', text)

    processed_recipes = []
    for recipe in recipes:
        # Extract title
        title_match = re.match(r'(.+):', recipe)
        if title_match:
            title = title_match.group(1).strip()
        else:
            continue  # Skip if no title found

        # Extract ingredients
        ingredients_match = re.search(r'Ingredients:(.*?)(?:Instructions:|Directions:|Method:)', recipe, re.DOTALL)
        if ingredients_match:
            ingredients = ingredients_match.group(1).strip()
            ingredients = re.findall(r'-\s*(.+)', ingredients)
        else:
            ingredients = []

        # Extract instructions
        instructions_match = re.search(r'(?:Instructions:|Directions:|Method:)(.+)', recipe, re.DOTALL)
        if instructions_match:
            instructions = instructions_match.group(1).strip()
            instructions = [step.strip() for step in re.split(r'\d+\.', instructions) if step.strip()]
        else:
            instructions = []

        # Combine important parts
        important_text = f"{title}\n"
        important_text += "Ingredients:\n" + "\n".join(ingredients) + "\n"
        important_text += "Instructions:\n" + "\n".join(instructions)

        # Remove stop words and punctuation
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(important_text)
        important_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

        processed_recipes.append(" ".join(important_words))

    # Write processed text to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n\n".join(processed_recipes))

# Usage
preprocess_cookbook('books/examplebook_extracted_text.txt', 'books/processed_recipes.txt')
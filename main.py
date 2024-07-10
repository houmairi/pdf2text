import PyPDF2
import os
import nltk
import argparse
from preprocess_recipes import preprocess_cookbook

def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading necessary NLTK data...")
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("NLTK data downloaded successfully.")

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def process_pdf(pdf_path, output_file):
    try:
        text = extract_text_from_pdf(pdf_path)
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(text)
        print(f"Processed: {os.path.basename(pdf_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(pdf_path)}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from PDF and optionally preprocess it.")
    parser.add_argument("-p", "--preprocess", action="store_true", help="Preprocess the extracted text")
    args = parser.parse_args()

    pdf_path = "books/cookingbythebook.pdf"
    extracted_text_file = "books/extracted_text.txt"
    processed_recipes_file = "books/processed_recipes.txt"
    
    # Extract text from PDF
    process_pdf(pdf_path, extracted_text_file)
    print(f"Text extraction complete. Extracted text saved to {extracted_text_file}")

    if args.preprocess:
        # Ensure NLTK data is downloaded
        download_nltk_data()
        
        # Preprocess the extracted text
        preprocess_cookbook(extracted_text_file, processed_recipes_file)
        print(f"Preprocessing complete. Processed recipes saved to {processed_recipes_file}")
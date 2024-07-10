import PyPDF2
import os

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
            outfile.write(f"--- {os.path.basename(pdf_path)} ---\n")
            outfile.write(text)
        print(f"Processed: {os.path.basename(pdf_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(pdf_path)}: {str(e)}")

if __name__ == "__main__":
    pdf_path = "books/cookingbythebook.pdf"  # Use forward slashes
    output_file = "books/extracted_text.txt"  # Use forward slashes
    process_pdf(pdf_path, output_file)
    print(f"Text extraction complete. Output saved to {output_file}")
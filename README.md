# PDF Text Extractor and Recipe Preprocessor

This Python project extracts text from PDF files using the PyPDF2 library and preprocesses the extracted text to format recipe information.

## Features

- Extracts text from PDF files
- Preprocesses extracted text to format recipe information
- Saves both raw extracted text and processed recipe text
- Easy to use and modify for specific needs

## Requirements

- Python 3.6+
- PyPDF2 library
- NLTK library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/houmairi/pdf2text.git
   cd pdf2text
   ```

2. Create a virtual environment and activate it: (optional)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your PDF file in the `books` directory (or modify the `pdf_path` in the script).

2. Run the main script:
   ```
   python main.py
   ```

3. The extracted raw text will be saved in `books/extracted_text.txt`.
4. The processed recipe text will be saved in `books/processed_recipes.txt`.

## Example

In the `/books` directory, you can find examples of the script's output:
- `examplebook_extracted_text.txt`: Contains the raw extracted text from a sample cooking book PDF.
- `examplebook_processed_recipes.txt`: Contains the processed and formatted recipe information.

## Customization

You can modify the following in `main.py`:
- `pdf_path`: Change the input PDF file location
- `extracted_text_file`: Change the output location for raw extracted text
- `processed_recipes_file`: Change the output location for processed recipe text

You can also modify `preprocess_recipes.py` to adjust the recipe preprocessing logic according to your needs.

## Project Structure

- `main.py`: The main script that handles PDF text extraction and calls the preprocessing function
- `preprocess_recipes.py`: Contains the logic for preprocessing and formatting cooking recipe information
- `requirements.txt`: Lists all the Python dependencies for the project

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/houmairi/pdf2text/issues).
# PDF Text Extractor

This simple Python script extracts text from a PDF file using the PyPDF2 library.

## Features

- Extracts text from a single PDF file
- Saves the extracted text to a text file
- Easy to use and modify for specific needs

## Requirements

- Python 3.6+
- PyPDF2 library

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

2. Run the script:
   ```
   python main.py
   ```

3. The extracted text will be saved in `books/extracted_text.txt`.

## Example

In the `/books` directory, you can find an example of the script's output. The file `examplebook_extracted_text.txt` contains the extracted text from a sample cooking book PDF.

## Customization

You can modify the `pdf_path` and `output_file` variables in the `main.py` script to change the input and output file locations.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/houmairi/pdf2text/issues).

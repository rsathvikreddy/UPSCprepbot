import fitz  # PyMuPDF
import os

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to split text into chunks of 250 words
def split_text_into_chunks(text, chunk_size=250):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# Directory containing PDF files
pdf_directory = r"C:\Users\LENOVO\Downloads\vajiram"

# Output file path
output_file = "output.txt"

# Open output file in append mode
with open(output_file, "a", encoding="utf-8") as f:
    # Loop through PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            # Extract text from PDF
            pdf_text = extract_text_from_pdf(pdf_path)
            # Split text into chunks of 250 words
            text_chunks = split_text_into_chunks(pdf_text)
            # Write chunks to output file
            for chunk in text_chunks:
                f.write(chunk + "\n\n")

print("Text extraction and chunking completed. Output saved to:", output_file)

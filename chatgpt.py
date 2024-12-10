import json
from PyPDF2 import PdfReader

def read_pdf(file_path):
    """Read text from a PDF file and remove all newline characters."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    # Remove all newline characters
    text = text.replace('\n', ' ')
    return text

def extract_questions_and_answers(text):
    """Extract questions and answers from text based on 'Q:' and 'A:' markers."""
    lines = text.split(' ')
    qa_pairs = []
    question = None
    for line in lines:
        line = line.strip()
        if line.startswith('Q:'):
            question = line[2:].strip()  # Remove 'Q:' and strip whitespace
        elif line.startswith('A:') and question:
            answer = line[2:].strip()  # Remove 'A:' and strip whitespace
            qa_pairs.append({"question": question, "answer": answer})
            question = None  # Reset question for the next pair
    return qa_pairs

def save_to_jsonl(qa_pairs, output_file):
    """Save question-answer pairs to a JSONL file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for pair in qa_pairs:
            json.dump(pair, f, ensure_ascii=False)
            f.write('\n')

def main():
    # Input PDF file path
    pdf_file = "input.pdf"
    # Output JSONL file path
    output_file = "output.jsonl"

    # Read and process the PDF
    text = read_pdf(pdf_file)
    qa_pairs = extract_questions_and_answers(text)

    # Save to JSONL
    save_to_jsonl(qa_pairs, output_file)
    print(f"Question-answer pairs saved to {output_file}")

if __name__ == "__main__":
    main()

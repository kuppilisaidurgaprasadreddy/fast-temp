import sys
import json
from docx import Document

def clean(text):
    return text.strip()

def docx_to_dict(path):
    doc = Document(path)
    data = {}
    current_key = None

    for para in doc.paragraphs:
        text = clean(para.text)

        if not text:
            continue

        # CASE 1: Split only once (IMPORTANT FIX)
        if "\t" in text:
            key, value = text.split("\t", 1)

        elif "  " in text:
            key, value = text.split("  ", 1)  # ✅ split only once

        else:
            # CASE 2: Heading + multiline v-alue
            if len(text.split()) <= 3:
                current_key = text
                data[current_key] = ""
                continue
            else:
                if current_key:
                    data[current_key] += " " + text
                continue

        key = key.strip()
        value = value.strip()

        data[key] = value

    return data


def main():
    if len(sys.argv) < 2:
        print("Usage: python 1.py input.docx")
        sys.exit(1)

    data = docx_to_dict(sys.argv[1])

    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()  
from pydoc import text
book = 'books/frankenstein.txt'

def get_book_text(file):
    
    try:
        with open(book, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    
def count_words(text):
    words = text.split()
    
    return len(words)

def char_count(text):
    low_text = text.lower()
    char_counts = {}
    for char in low_text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts 

def sort_on(items):
    return items["num"]

def get_characters_stats(text):
    characters = []
    for char, count in char_count(text).items():
        characters.append({"char": char, "num": count})
    characters.sort(reverse=True, key=sort_on)
    return characters
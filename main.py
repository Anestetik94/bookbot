def get_book_text(file):
    
    try:
        with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def words_count(text):
    words = text.split()
    return len(words)



def main():
    
    book_text = get_book_text("frankenstein.txt")
    num_words = 0
    if "Error" in book_text:
        print(book_text)  # Print the error message if the file wasn't found
    else:
        word_count = count_words(book_text)
        print(f'{num_words} words found in the document')


if __name__ == "__main__":
    main()

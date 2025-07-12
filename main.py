import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

from stats import count_words, get_book_text, get_characters_stats, book


def main():
    
    book_text = get_book_text("frankenstein.txt")
    num_words = 0
    if "Error" in book_text:
        print(book_text) 
    else:
        num_words = count_words(book_text)
        print("============ BOOKBOT ============")
        print(f"""Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

        characters = get_characters_stats(book_text)
        for char in characters:
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

import sys
from stats import count_words, count_characters, sorted_character_counts  # Import all necessary functions

def get_book_text(filepath):
    """Read and return the contents of the specified file."""
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    """Main function to execute the book text retrieval, count words, and count characters."""
    # Check if a valid book path was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with a status code of 1


    # Use the second argument as the path to the book file
    filepath = sys.argv[1]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_contents = get_book_text(filepath)

    # Count and print the number of words
    num_words = count_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Count and sort the character occurrences
    char_counts = count_characters(book_contents)
    sorted_counts = sorted_character_counts(char_counts)

    print("--------- Character Count -------")
    for char_count in sorted_counts:
        print(f"{char_count['char']}: {char_count['num']}")

    print("============= END ===============")

if __name__ == '__main__':
    main()

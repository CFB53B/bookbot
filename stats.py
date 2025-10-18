def count_words(text):
    """Return the number of words in the given text."""
    words = text.split()  # Split the text into words
    return len(words)     # Return the number of words

def count_characters(text):
    """Return a dictionary with counts of each character in the given text."""
    char_count = {}
    text = text.lower()  # Convert the text to lowercase

    for char in text:  # Iterate over each character in the text
        if char in char_count:
            char_count[char] += 1  # Increment count if the character already exists
        else:
            char_count[char] = 1  # Initialize count if the character does not exist

    return char_count  # Return the dictionary with character counts

def sorted_character_counts(char_counts):
    """Return a sorted list of dictionaries of character counts."""
    sorted_counts = []

    for char, count in char_counts.items():
        if char.isalpha():  # Skip non-alphabetical characters
            sorted_counts.append({"char": char, "num": count})
    
    # Sort the list from greatest to least by the count
    sorted_counts.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_counts

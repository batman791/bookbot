def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    print(f"There are {count_words(text)} words in {book_path}.")

    print(count_distinct_characters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_distinct_characters(text):
    chardict = {}
    lowertext = text.lower()
    for word in lowertext.split():
        for char in word:
            key = char
            chardict[key] = chardict.get(key, 0) + 1

    return chardict
    
def count_words(book):
    words = book.split()
    word_count = len(words)

    return word_count


main()


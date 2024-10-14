def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(text)

    char_counts = dict(sorted(count_distinct_characters(text).items(), key=lambda item: item[1], reverse=True))

    print(format_report(book_path, count_words(text), char_counts))

    return 0


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

def format_report(book_path, word_count, char_count):
    lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    report = ""

    report_title = f"--- Begin report of {book_path} ---\n"
    report__wordcount = f"{word_count} words found in the document\n\n"
    
    report += report_title + report__wordcount

    for key, value in char_count.items():
        if key in lowercase_letters:
            report_line = f"The '{key}' character was found {value} times\n"
            report += report_line
    
    return report
 


main()


from string import ascii_lowercase as low_letter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    report = get_report(num_words, num_characters)
    print(report)

def get_report(words, characters):
    report ="--- Begin report of books/frankenstein.txt ---\n"
    report +=f"{words} words found in the document\n\n"

    # Sorting the dictionary
    char_tuples = characters.items()
    sorted_chars = sorted(char_tuples, key=lambda item: item[1], reverse=True)
    sorted_char_dict = {k: v for k, v in sorted_chars}


    #Looping through the sorted dictionary
    for char, times in sorted_char_dict.items():
        sentence = f"The '{char}' character was found {times} times\n"
        report += sentence

    report += "\n--- End report ---"

    return report

def char_sort(char):
    return char["char_count"]

def get_num_characters(text):
    text.lower()
    lettersdict = {}
    for letter in low_letter:
        char_count = text.count(letter)
        lettersdict.update({letter:char_count})
    return lettersdict


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()
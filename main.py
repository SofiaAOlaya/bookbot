def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    count = count_words(text)
    letter_count = count_letters(text)
    report = generate_report(letter_count)
    print(f"---Begin report of {book_path}---")
    print(f"{count} words found in the document")
    print()

    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book(book_path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = 0
    countable = text.split()
    for str in countable:
        words += 1
    return words

def count_letters(text):
    letters_dic = {}
    for c in text:
        lowered = c.lower()
        if lowered in letters_dic:
            letters_dic[lowered] += 1
        else:
            letters_dic[lowered] = 1
    return letters_dic
        
def sort_on(d):
    return d["num"]

def generate_report(letter_count):
    list_of_characters = []
    for ch in letter_count:
        list_of_characters.append({"char": ch, "num": letter_count[ch]})
    list_of_characters.sort(reverse=True, key=sort_on)
    return list_of_characters 

main()

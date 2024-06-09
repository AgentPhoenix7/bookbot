def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    word_count = count_words(text)
    print(f"{word_count} words found in the document.\n")
    character_count = count_characters(text)
    sorted_character_count = sort_character_counts(character_count)
    #print("Character counts:")
    #print(character_count)
    print("Sorted character counts:")
    for item in sorted_character_count:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_count = {}
    for char in text:
        if char.isalpha():
            if char in character_count:
                character_count[char] +=1
            else:
                character_count[char] = 1

    return character_count

def sort_on(dict_item):
    return dict_item["num"]

def sort_character_counts(character_count):
    character_count_list = [{"char": char, "num": num} for char, num in character_count.items()]
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list

main()
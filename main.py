from stats import number_of_words, number_of_occurring_characters, sorted_dictionary
import sys

def get_book_text(file_path:str) -> str:
    if isinstance(file_path, str):

        with open(file_path) as book:
            book_contents = book.read()
        return book_contents
    else:
        return "error, please provide a valid file path"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_of_book_to_work_on = sys.argv[1]
    book_content = get_book_text(path_of_book_to_work_on)
    words_in_the_text = number_of_words(book_content)
    characters_in_the_text = number_of_occurring_characters(book_content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_of_book_to_work_on}...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_the_text} total words")
    print("--------- Character Count -------")
    for val in sorted_dictionary(characters_in_the_text):
        if val["char"].isalpha():
            print(f"{val["char"]}: {val["num"]}")
    print("============= END ===============")


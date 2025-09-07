import sys
from stats import count_words
from stats import count_chars
from stats import sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        word_list = get_book_text(sys.argv[1])
   
    word_count = count_words(word_list)
    char_counts = count_chars(word_list)
    sorted_dictionary_list = sort_dictionary(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_dictionary_list:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()
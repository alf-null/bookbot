from stats import get_num_words, get_symbol_count, sort_symbol_dict, print_report

import sys

def get_book_text(path) ->str:
    with open(path) as fp:
        return fp.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = get_num_words(text)
    symbol_count = get_symbol_count(text)
    sorted_symbols = sort_symbol_dict(symbol_count)

    print_report(book_path, count, sorted_symbols)

main()

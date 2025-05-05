
def get_num_words(text) ->int:
    return len(text.split())

def get_symbol_count(text):
    symbol_count = {}
    for letter in text:
        if letter.lower() not in symbol_count:
            symbol_count[letter.lower()] = 1
        else:
            symbol_count[letter.lower()] += 1
    return symbol_count

def sort_symbol_dict(count_dict):
    list_of_symbols = [{"letter":k, "count": v} for k, v in count_dict.items() if k.isalpha()]
    list_of_symbols.sort(reverse=True, key=lambda x: x["count"])
    return list_of_symbols

def print_report(path, count, sorted_symbols):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for element in sorted_symbols:
        print(f'{element["letter"]}: {element["count"]}')
    print("============= END ===============")

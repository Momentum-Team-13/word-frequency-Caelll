STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
        filtered_words = [word for word in read_file if word not in STOP_WORDS]
        no_punct = read_file.replace(".", "").replace("!", "").replace(",", "").replace("-", " ").replace("?", "")
        lower_word = no_punct.lower() # lowercase all words
        word_list = lower_word.split() # make words one by one in lines
        text_dict = dict.fromkeys(word_list, 0)
        
        for word in word_list:
            text_dict[word] += 1
        print(text_dict)








if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

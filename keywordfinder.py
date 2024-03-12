#!/usr/bin/env python
import sys


def main():
    """
    This script compares two files and prints the words that are missing in each file and the words that are in both files.
    Usage: python keywordfinder.py <file_1> <file_2>
    :return: None
    """
    if not len(sys.argv) == 3:
        print('Usage: python keywordfinder.py <file_1> <file_2>')
        return
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    words_no_duplicates_1 = get_file_words_no_duplicates(file_1)
    words_no_duplicates_2 = get_file_words_no_duplicates(file_2)
    missing_words_in_file_2 = words_no_duplicates_1 - words_no_duplicates_2
    missing_words_in_file_1 = words_no_duplicates_2 - words_no_duplicates_1
    words_in_both_files = words_no_duplicates_1 & words_no_duplicates_2
    print(f'Missing words in {file_1}: {" ".join(missing_words_in_file_1)}\n\n')
    print(f'Missing words in {file_2}: {" ".join(missing_words_in_file_2)}\n\n')
    print(f'Words in both files: {" ".join(words_in_both_files)}')


def get_file_words_no_duplicates(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        all_punctuation_and_brackets = ['.', ',', '!', '?', '(', ')', '[', ']', '{', '}', ':', ';', '-', '_', '+', '=', '*', '/', '\\', '|', '<', '>', '@', '#', '$', '%', '^', '&', '~', '`']
        file_content = file_content.lower()
        for punctuation in all_punctuation_and_brackets:
            file_content = file_content.replace(punctuation, '')
        words = file_content.split()
        words_no_duplicates = set(words)
        return words_no_duplicates


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

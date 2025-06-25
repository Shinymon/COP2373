"""
This program allows the user to enter a paragraph that may include sentences starting with numbers.
It splits the paragraph into individual sentences using lookahead regular expressions
and then displays each sentence and the total sentence count.
"""

import re


def split_sentences(paragraph):
    """
    Splits the paragraph into sentences using lookahead for punctuation like '.', '?', or '!'
    Ensures punctuation is preserved at the end of each sentence.
    """
    # Lookahead regex: split where we find punctuation followed by space or end of string
    return re.split(r'(?<=[.!?])\s+', paragraph.strip())


def display_sentences(sentences):
    """
    Prints each sentence on a new line and shows the total count.
    """
    print("\nSentences found:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    paragraph = input("Enter a paragraph (you can include sentences that begin with numbers):\n")
    sentences = split_sentences(paragraph)
    display_sentences(sentences)


if __name__ == "__main__":
    main()
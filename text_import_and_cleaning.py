import re
import os
import argparse
import numpy as np


def preprocessing(filename):

    with open(filename, 'r') as myfile:
        # get the list of lines
        list_lines = myfile.readlines()
        # remove trailing whitespace
        list_lines = map(lambda x: x.rstrip(), list_lines)
        # remove leading whitespace
        list_lines = map(lambda x: x.lstrip(), list_lines)
        # keep length > 0 lines
        list_lines = [l for l in list_lines if len(l) > 0]
        # lowercase the text
        list_lines = map(lambda x: x.lower(), list_lines)
        # split sentences based on ., !, ?
        list_sentences = map(lambda x: re.split(r'[.?!]+', x), list_lines)
        # remove sentences which may still be empty
        # flatten the list and remove length 0 sentences
        list_sentences = [subs for s in list_sentences for subs in s if subs != ""]
        # characters to remove
        chars_to_remove = ['?', ';', '!', ',', '"', '<','>',
                           '[', ']', '#', '(', ')', '/', '*', '%', '.', ':', '\t', '\n']
        # remove the characters from the sentences
        list_sentences = [s.translate(None, ''.join(chars_to_remove)) for s in list_sentences]
        # remove any trailing:leading whitespace induced by previous operations
        list_sentences = map(lambda x: x.rstrip(), list_sentences)
        list_sentences = map(lambda x: x.lstrip(), list_sentences)
        # get the list of words by splitting the lines according to whitespaces
        list_words = []
        for s in list_sentences:
            list_words += s.split(" ")
        return list_sentences, list_words

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="filename containing the paragraph to process")
    args = parser.parse_args()

    assert args.filename is not None, "Please specify filename"
    assert os.path.isfile(args.filename), "File does not exist"

    sentences, words = preprocessing(args.filename)

    print "The total number of words is %s " % (len(words))
    print "The total number of unique words is %s " % (len(set(words)))
    print "The total number of sentences is %s " % (len(sentences))

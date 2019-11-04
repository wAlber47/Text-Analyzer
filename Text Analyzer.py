"""
Week 11 Python Lab - Basic Text Analyzer
Will allow input from user or a file
Gives the user a dictionary of words and their frequency
William Alber 11/3/2019
"""
import string, sys, json, os

menu_text = """
Please select option:
- Analyze Text Input [t]
- Analyze File [f]
- View Analysis [v]
- Quit [q]
"""

def input_analysis(sentence):
    """ Returns a list of word count from string input

    :param sentence (string)
    :return final (dict) words and their frequency
    """
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator).split()

    final = {}
    for i in sentence:
        word_count = sentence.count(i)
        final.update( {i: word_count} )

    return final


def file_analysis(fname):
    text = open(fname, "r").read()
    
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).split()

    final = {}
    for i in text:
        word_count = text.count(i)
        final.update( {i: word_count} )

    return final

def write_file(dict_):
    """ Writes to analysis.txt

    :param dict_ (dict) words and their frequency
    """
    output_name = input("\nOutput File Name [include .txt]: ")
    with open(output_name, "w") as f:
        print(dict_, file=f)
        

while True:
    print(menu_text)
    choice = input()

    # Analyze Text
    if choice.lower() == "t":
        sentence = input("\nInput Sentence: ")
        t_dict = input_analysis(sentence)
        output = input("Write output to file? [y/n] ")
        if output.lower() == "y":
            write_file(t_dict)
        else:
            print(t_dict)

    # Analyze File
    if choice.lower() == "f":
        fname = input("File Name: ")
        f_dict = file_analysis(fname)
        output = input("Write output to file? [y/n] ")
        if output.lower() == "y":
            write_file(f_dict)
        else:
            print(f_dict)

    # View Analysis
    if choice.lower() == "v":
        file_name = input("\nFile Name: ")
        try:
            os.startfile(file_name)
        except FileNotFoundError:
            print("File Not Found.")

    # Quit
    if choice.lower() == "q":
        sys.exit()

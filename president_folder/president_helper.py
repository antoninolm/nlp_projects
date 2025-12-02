import os
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter

# Directory where this file (president_helper.py) lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_file(file_name):
    """Read a speech file from the president_folder directory."""
    full_path = os.path.join(BASE_DIR, file_name)
    with open(full_path, "r", encoding="utf-8") as file:
        file_text = file.read()
    return file_text


def process_speeches(speeches):
    word_tokenized_speeches = []
    for speech in speeches:
        sentence_tokenizer = PunktSentenceTokenizer()
        sentence_tokenized_speech = sentence_tokenizer.tokenize(speech)
        word_tokenized_sentences = []
        for sentence in sentence_tokenized_speech:
            word_tokenized_sentence = [
                word.lower()
                    .strip(".")
                    .strip("?")
                    .strip("!")
                for word in sentence
                    .replace(",", "")
                    .replace("-", " ")
                    .replace(":", "")
                    .split()
            ]
            word_tokenized_sentences.append(word_tokenized_sentence)
        word_tokenized_speeches.append(word_tokenized_sentences)
    return word_tokenized_speeches


def merge_speeches(speeches):
    all_sentences = []
    for speech in speeches:
        for sentence in speech:
            all_sentences.append(sentence)
    return all_sentences


def get_president_sentences(president):
    """
    Return all tokenized sentences for a single president.
    Looks for .txt files in the same folder as president_helper.py
    whose filename contains the president string (case-insensitive).
    """
    files = sorted(
        f
        for f in os.listdir(BASE_DIR)
        if president.lower() in f.lower() and f.endswith(".txt")
    )

    speeches = [read_file(f) for f in files]
    processed_speeches = process_speeches(speeches)
    all_sentences = merge_speeches(processed_speeches)
    return all_sentences


def get_presidents_sentences(presidents):
    """
    Return all tokenized sentences for a list of presidents.
    """
    all_sentences = []
    for president in presidents:
        files = sorted(
            f
            for f in os.listdir(BASE_DIR)
            if president.lower() in f.lower() and f.endswith(".txt")
        )
        speeches = [read_file(f) for f in files]
        processed_speeches = process_speeches(speeches)
        all_prez_sentences = merge_speeches(processed_speeches)
        all_sentences.extend(all_prez_sentences)
    return all_sentences


def most_frequent_words(list_of_sentences):
    all_words = [word for sentence in list_of_sentences for word in sentence]
    return Counter(all_words).most_common()
"""
import os
import re
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_file(file_name):
  with open(file_name, 'r+', encoding='utf-8') as file:
    file_text = file.read()
  return file_text

def process_speeches(speeches):
  word_tokenized_speeches = list()
  for speech in speeches:
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_speech = sentence_tokenizer.tokenize(speech)
    word_tokenized_sentences = list()
    for sentence in sentence_tokenized_speech:
      word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").split()]
      word_tokenized_sentences.append(word_tokenized_sentence)
    word_tokenized_speeches.append(word_tokenized_sentences)
  return word_tokenized_speeches

def merge_speeches(speeches):
  all_sentences = list()
  for speech in speeches:
    for sentence in speech:
      all_sentences.append(sentence)
  return all_sentences

def get_president_sentences(president):
    # list all files in the same folder as this helper
    files = sorted(
        f
        for f in os.listdir(BASE_DIR)
        if president.lower() in f.lower() and f.endswith(".txt")
    )

    speeches = [read_file(f) for f in files]
    processed_speeches = process_speeches(speeches)
    all_sentences = merge_speeches(processed_speeches)
    return all_sentences

def get_president_sentences(president):
  base_path = os.path.join("..", "president_folder")   # go up 1 level, then into utils
  files = sorted([file for file in os.listdir(base_path) if president.lower() in file.lower()])
  speeches = [read_file(file) for file in files]
  processed_speeches = process_speeches(speeches)
  all_sentences = merge_speeches(processed_speeches)
  return all_sentences

def get_presidents_sentences(presidents):
  all_sentences = list()
  for president in presidents:
    files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
    speeches = [read_file(file) for file in files]
    processed_speeches = process_speeches(speeches)
    all_prez_sentences = merge_speeches(processed_speeches)
    all_sentences.extend(all_prez_sentences)
  return all_sentences

def most_frequent_words(list_of_sentences):
  all_words = [word for sentence in list_of_sentences for word in sentence]
  return Counter(all_words).most_common()
  
    """

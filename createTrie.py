from os import listdir
import re

from autocomplete import AutoCompleteData


# import json
# from os import close
# ​
# ​
# def write_to_json(path,data):
#     with open(path, "w") as the_file:
#         json.dump(data, the_file)
# ​
# ​
# def read_from_json(path):
#     the_file = open(path)
#     data = json.load(the_file)
#     the_file.close()
#     return data


def insertPrefixs(data, trie, start, dataIndex):
    for char in normalForm(data.completed_sentence[start:]):
        if char not in trie.keys():
            trie[char] = dict()
            trie[char]["end"] = [dataIndex]
        else:
            if dataIndex not in trie[char]["end"]:
                trie[char]["end"] += [dataIndex]
        trie = trie[char]


def insertSufixs(data, index, trie, item):
    for char in range(len(normalForm(index.completed_sentence))):
        insertPrefixs(index, trie, char, item)
        # data[item].offset = char


def insertTotrie(data, index, trie, item):
    insertPrefixs(index, trie, 0, item)
    insertSufixs(data, index, trie, item)


def normalForm(sentence):
    # str = " ".join(e for e in str if e.isalnum() or e == ' ').lower()
    return " ".join(((sentence.replace("\n", "")).replace(",", "")).split())



def createDataBase(data):
    search_trie = dict()
    # onlyfiles = [f for f in listdir('RFC')]
    # file = onlyfiles[0]
    # for file in onlyfiles:
    file = "abstract.txt"
    path = f'technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/c-api/{file}'
    my_file = open(path, "r", encoding="utf8")
    for index, sentence in enumerate(my_file):
        if sentence != "":
            data[index] = AutoCompleteData(sentence, f'{file} {index}')
            insertTotrie(data, data[index], search_trie, index)
    my_file.close()
    return search_trie
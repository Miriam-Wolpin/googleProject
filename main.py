from autocomplete import autoComplete
from createTrie import createDataBase, normalForm

if __name__ == '__main__':
    # init trie
    data = dict()
    trie = createDataBase(data)

    # auto complete sentence
    while 1:
        sentenceToCheck = ""
        while 1:
            sentenceToCheck += input(f"your sentence here: {sentenceToCheck}")
            if sentenceToCheck[-1] == "#" or autoComplete(trie, data, normalForm(sentenceToCheck)) == 0:
                print("-----new search-----")
                break







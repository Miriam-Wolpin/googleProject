from search import searchInTrie
class AutoCompleteData:

    def __init__(self, completed_sentence, source_text):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = -1
        self.score = 0


    def print(self):
        print(self.completed_sentence)
        print("( path:",self.source_text , "| offset:",self.offset ,"| score:", self.score, ")")
        print()


def printAutoComplete(res):
    for item in res:
        AutoCompleteData.print(item)

def sortByScore(res):
    res.sort(key=lambda x: x.completed_sentence)
    res.sort(key=lambda x: x.score, reverse=True)
    return res


def restartScoreAndOffset(res):
    for item in res:
        item.score = 0
        item.offset = -1


def autoComplete(trie,data,sentenceForSearch):
    res = searchInTrie(data, sentenceForSearch, trie)
    if len(res) == 0:
        print("-----no result-----!")
        return 0
    res = sortByScore([data[i] for i in res])
    printAutoComplete(res[:5])
    restartScoreAndOffset(res)
    return 1
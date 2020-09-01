python3 import cltk

from cltk.stem.latin.declension import CollatinusDecliner

def dec(words):
    decliner = CollatinusDecliner()
    dec_words = {}
    for word in words:
        dec_word = decliner.decline(word)
        print (dec_word)


words = ["locutio", "fructus"]

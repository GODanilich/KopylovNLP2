import gensim

pos = ["проблема_NOUN", "радость_NOUN"]
neg = []

file = "cbow.txt"

word2vec = gensim.models.KeyedVectors.load_word2vec_format(file, binary=False)
dist = word2vec.most_similar(positive=pos, negative = neg)
for i in dist:
    print(i)
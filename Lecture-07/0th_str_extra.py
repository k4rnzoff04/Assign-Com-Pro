def sort_words_in_sentecnce(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentecnce = ' '.join(words)
    return sorted_sentecnce

sentence = "This is a man world"
sorted_result = sort_words_in_sentecnce(sentence)
print(("Sorted sentence:", sorted_result))
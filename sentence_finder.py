unknown_word_limit = 1

def load_known_words():
    words = []
    with open('word_list', 'r') as word_file:
        for line in word_file:
            words.append(line.replace('\n',''))
    return words

def load_sentences():
    sentences = []
    with open('sentence_list', 'r') as sentence_file:
        for line in sentence_file:
            sentences.append(line.replace('\n','').replace('.','').split())
    return sentences

def sentences_with_unknown_words(unknown_word_limit, sentences, words):
    new_sentences = []
    for sentence in sentences:
        unknown = 0
        for word in sentence:
            if word not in words:
                unknown += 1
                if unknown > unknown_word_limit:
                    break
        if unknown > 0 and unknown <= unknown_word_limit:
            new_sentences.append(" ".join(sentence) + '\n')
    return new_sentences

def write_sentences_to_file(new_sentences):
    with open('new_sentences', 'a') as output_file:
        for line in new_sentences:
            output_file.write(line)

def Main():
    sentences = load_sentences()
    known_words = load_known_words()
    new_sentences = sentences_with_unknown_words(unknown_word_limit, sentences, known_words)
    write_sentences_to_file(new_sentences)

Main()

#!/usr/bin/python3
import math
import sys
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, sent_tokenize

STOPWORDS_PATH = 'stopwords.txt'


def get_all_files(directory):
    return sys.argv

def load_topic_words(topic_file, n):
    temp_dict = {}
    with open(topic_file) as f:
        for line in f:
            (key, val) = line.split()
            temp_dict[key] = float(val)
    sorted_list = sorted(temp_dict, key=temp_dict.__getitem__, reverse=True)
    top_n = sorted_list[:n]
    return top_n


def cluster_keywords(keylist, outputfile):
    f = open(outputfile, "w")
    temp_list = []
    temp_list2 = []

    i = 0
    while(i < len(keylist)):
        keyword = keylist[i]
        f.write(keyword)
        # n = len(keylist)
        synset_list = wn.synsets(keyword)
        for single_synset in synset_list:
            hyper_list = single_synset.hypernyms()
            hypo_list = single_synset.hyponyms()
            for lemma in single_synset.lemmas():

                temp_list.append(lemma)
            for single_hypo in hypo_list:
                for lemma in single_hypo.lemmas():

                    temp_list.append(lemma)
            for single_hyper in hyper_list:
                for lemma in single_hyper.lemmas():

                    temp_list.append(lemma)

        j = keylist.index(keyword)+1

        while(j < len(keylist)):
            next_word = keylist[j]
            syn_list_new = wn.synsets(next_word)
            for each_el in syn_list_new:
                for lemma in each_el.lemmas():
                    # print(lemma) #put in set2
                    temp_list2.append(lemma)

            common = set(temp_list).intersection(temp_list2)
            if(common):
                f.write(",")
                f.write(next_word)
                keylist.remove(next_word)
                temp_list2[:] = []

            j = j+1

        f.write("\n")
        keylist.remove(keyword)
        temp_list[:] = []
        temp_list2[:] = []
        i = 0


def summarize_baseline(directory, outputfile):
    file_list = get_all_files(directory)
    file_list.sort()
    sum_text = ''
    total_len = 0
    for filename in file_list:
        f = open(filename, "r")
        text = f.readlines()[0]
        f.close()
        total_len += len(word_tokenize(text))
        sum_text += text
        if(total_len >= 100):
            break

    f = open(outputfile, "w")
    f.write(sum_text)
    f.close()


def get_unigram_dist(text):
    list_words = word_tokenize(text)
    stopf = open(STOPWORDS_PATH, "r")
    stop_words = stopf.readlines()
    stopf.close()
    stop_words = [word.strip() for word in stop_words]
    unigram_dict = {}
    total_count = 0
    for word in list_words:
        if word in stop_words:
            continue
        total_count = total_count + 1
        if word in unigram_dict:
            unigram_dict[word] = unigram_dict[word] + 1
        else:
            unigram_dict[word] = 1

    unigram_dict.update({k: float(unigram_dict[k])/float(total_count) for k in unigram_dict.keys()})

    return unigram_dict


def summarize_kl(inputdir, outputfile):

    file_list = get_all_files(inputdir)
    input_text = ''
    list_sen = []
    for filename in file_list:
        f = open(filename, "r")
        sen = f.read()
        list_sen.append(sen)
        input_text = input_text + sen + ' '
        f.close()

    input_unigram_dist = get_unigram_dist(input_text)

    sum_text = ''
    sum_text_to_write = ''
    sen_list = []
    sen_ind = []

    while(len(word_tokenize(sum_text)) < 100):
        min_kl = 100000.0
        best_sentence = ''

        for ind_i, sentences in enumerate(list_sen):
            for ind_j, sentence in enumerate(sentences.split('\n')):
                if sentence in sum_text or sentence in sen_list or (ind_i, ind_j) in sen_ind:
                    continue

                temp_sum_text = sum_text + ' ' + sentence
                sen_unigram_dist = get_unigram_dist(temp_sum_text)

                kl_val = 0
                for key in sen_unigram_dist.keys():
                    p_word = sen_unigram_dist[key]
                    q_word = 0
                    if key in input_unigram_dist:
                        q_word = input_unigram_dist[key]
                    if p_word != 0 and q_word != 0:
                        kl_val += p_word * math.log(float(p_word)/float(q_word))

                if kl_val < min_kl:
                    min_kl = kl_val
                    best_sentence = sentence.strip()
                    best_ind_i = ind_i
                    best_ind_j = ind_j

        sum_text = sum_text + best_sentence+' '
        sum_text_to_write = sum_text_to_write + best_sentence+'\n'
        sen_list.append(best_sentence)
        sen_ind.append((best_ind_i, best_ind_j))

    with open(outputfile, "w"):
        f.write(sum_text_to_write)


def load_collection_sentences(directory):
    files = get_all_files(directory)
    li = list()
    for f in files:
        sents = load_file_sentences(f)
        li.extend(sents)
    return li


def load_collection_tokens(directory):
    files = get_all_files(directory)
    li = list()
    for f in files:
        tokens = load_file_tokens(f)
        li.extend(tokens)

    stopf = open(STOPWORDS_PATH, "r")
    stop_words = stopf.readlines()
    stopf.close()
    stop_words = [word.strip() for word in stop_words]

    temp = list(set(li)-set(stop_words))
    return temp


def load_file_sentences(filepath):
    file1 = open(filepath)
    sent = file1.read()
    return sent_tokenize(sent)


def load_file_tokens(filepath):
    file1 = open(filepath)
    text = file1.read()
    return word_tokenize(text)


def makeVectDict(dir):
    vectDict = dict()
    words = load_collection_tokens(dir)
    sentences = load_collection_sentences(dir)
    # make vector for sentence
    for sentence in sentences:
        temp_sent = word_tokenize(sentence)
        sent_vec = [0] * len(words)
        for idx, word in enumerate(words):
            if word in temp_sent:
                sent_vec[idx] = 1
        vectDict[sentence] = sent_vec
    return vectDict


def cosine_similarity(x, y):
    prodCross = 0.0
    xSquare = 0.0
    ySquare = 0.0
    for i in range(min(len(x), len(y))):
        prodCross += x[i] * y[i]
        xSquare += x[i] * x[i]
        ySquare += y[i] * y[i]
    if (xSquare == 0 or ySquare == 0):
        return 0.0
    return prodCross / (math.sqrt(xSquare) * math.sqrt(ySquare))


def notChanging(currRank, nextRank):
    threshold = 0.00000001
    for key, value in currRank.items():
        if nextRank[key] - value > threshold:
            return False
    return True


def valid(sent, summary, vectDict, threshold):
    for sentence in summary:
        if cosine_similarity(vectDict[sent], vectDict[sentence]) > threshold:
            return False
    return True


def summarize_lexpagerank(inputdir, outputfile):
    sentences = load_collection_sentences(inputdir)
    adjList = dict()
    currRank = dict()
    vectDict = makeVectDict(inputdir)
    edge_threshold = 0.1

    for idx, sent in enumerate(sentences):
        adjList[idx] = list()
        currRank[idx] = 1.0/len(sentences)

    # Construct the Graph
    for idx, sent in enumerate(sentences):
        for idx2, sent2 in enumerate(sentences):
            if sent != sent2:
                sim = cosine_similarity(vectDict[sent], vectDict[sent2])
                if sim > edge_threshold:
                    adjList[idx].append(idx2)

    # Lex Rank
    while True:
        nextRank = {i: 0.0 for i in currRank.keys()}
        d = 0.85
        n = len(sentences)
        constant = 0.15/n
        for sent, edges in adjList.items():
            temp1 = 0.0
            for sent2 in edges:
                temp1 += float(currRank[sent2]) / float(len(adjList[sent2]))
            nextRank[sent] = constant+(d*temp1)
        if notChanging(currRank, nextRank):
            break
        else:
            currRank = nextRank

    sorted_sents = [sentences[x] for x in sorted(currRank.keys(), key=lambda x: currRank[x], reverse=True)]

    summary = list()
    sumLength = 0
    for sent in sorted_sents:
        if valid(sent, summary, vectDict, 0.75):
            sumLength += len(word_tokenize(sent))
            summary.append(sent)
            if sumLength > 100:
                break

    # construct text with sentences
    sum_to_write = ''
    for summ in summary:
        sum_to_write = sum_to_write+summ+'\n'

    with open(outputfile, "w") as f:
        f.write(sum_to_write)


if __name__ == "__main__":

    directory="/home/cis505/hackathon/trial"
    #ques 4.1
    summarize_baseline(directory, "/home/cis505/hackathon/trial_output.txt")
    
    #directory="/home1/c/cis530/hw4/dev_input/dev_10"
    #ques 4.2
    summarize_kl(directory,"/home/cis505/hackathon/trial_output2.txt.txt")
    
    #ques4.3
    #summarize_lexpagerank("/home1/c/cis530/hw4/dev_input/dev_10","/home1/a/agrima/hw4_agrima/trial3.txt")

#!/usr/bin/env python

"""Topic Extraction using NLTK RakeKeywordExtractor

CERN Webfest 2017

This file contains routines for
    - Summarization
    - Representative Messages

"""

import networkx as nx
import numpy as np

from nltk import sent_tokenize

from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils import load_sample


def textrank(document, tokenize=True, num_msgs=5):
    if tokenize:
        sentences = sent_tokenize(document)
    else:
        sentences = document

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    # similarity_graph = normalized * normalized.T
    # nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)

    similarity_graph = cosine_similarity(normalized)
    nx_graph = nx.from_numpy_matrix(similarity_graph)

    scores = nx.pagerank(nx_graph)
    sentence_array = sorted(((scores[i], s, i) for i, s in enumerate(sentences)), reverse=True)

    sentence_array = np.asarray(sentence_array)

    # print(sentence_array[:10])

    fmax = float(sentence_array[0][0])
    fmin = float(sentence_array[len(sentence_array) - 1][0])

    temp_array = []
    # Normalization
    for i in range(0, len(sentence_array)):
        if fmax - fmin == 0:
            temp_array.append(0)
        else:
            temp_array.append((float(sentence_array[i][0]) - fmin) / (fmax - fmin))

    threshold = (sum(temp_array) / len(temp_array)) + 0.2

    # print(temp_array[:10])

    sentence_list = []

    for i in range(0, len(temp_array)):
        if temp_array[i] > threshold:
            sentence_list.append(sentence_array[i][1])

    # print(sentence_list[:10])

    sentence_list = sentence_list[:num_msgs]

    seq_list = []
    positions = []
    for sentence, position in zip(sentences, range(len(sentences))):
        if sentence in sentence_list:
            seq_list.append(sentence)
            positions.append(position)

    return seq_list, positions


def representative_msgs_textrank(messages, num_msgs=5):
    contents = [d['content'] for d in messages]
    sentences, positions = textrank(contents, tokenize=False, num_msgs=num_msgs)
    return [messages[i] for i in positions]


if __name__ == '__main__':
    messages = load_sample()
    for m in representative_msgs_textrank(load_sample()):
        print(m)
        pass

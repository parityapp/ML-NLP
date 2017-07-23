#!/usr/bin/env python

"""Summarization Routines for Parity App

CERN Webfest 2017

This module contains the routines for:
    - Representative Message retrieval
    - Message summarization

"""

from datetime import datetime
import dateutil.parser
import json
from typing import List, Dict

from nltk import sent_tokenize, word_tokenize

from ntlk_rake import topic_extraction_rake

from gensim.summarization import summarize
from gensim.summarization import keywords

from textrank import representative_msgs_textrank

from lex_and_kl_summary import summarize_kl, summarize_lexpagerank

Message = Dict[str, datetime]


def whole_text(messages, lines=None):
    if lines is not None:
        messages = messages[:lines]
    return ". ".join(d['content'] for d in messages)


def load_sample(file='data/sample_chat.json'):
    with open(file, 'r') as f:
        sample = json.load(f)

    for d in sample:
        d['timestamp'] = dateutil.parser.parse(d['timestamp'])

    return sample


def load_sample_text(file='data/sample_chat.json', lines=None):
    return whole_text(load_sample(text), lines=lines)


def tokenize_for_mglda(messages):

    def _tokenize_message(message):
        sentences = sent_tokenize(message)
        tokenized_sentences = [word_tokenize(s) for s in sentences]
        return tokenized_sentences

    return [_tokenize_message(m['content']) for m in messages]


def representative_msgs(messages: List[Message], method) -> List[Message]:

    if method == 'textrank':
        return representative_msgs_texrank(messages)


def summarize_msgs(messages: List[Message], method) -> str:
    text = whole_text(messages)

    if method == 'gensim':
        return summarize(text)
    elif method == 'lexrank':
        summarize_lexpagerank(text)
    elif metod == 'kl':
        summarize_kl(text)


def relevant_topics(messages: List[Message], method) -> List[str]:

    text = whole_text(messages)

    if method == 'RAKE':
        return topic_extraction_rake(text)
    elif method == 'gensim':
        return keywords(text)

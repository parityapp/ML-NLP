#!/usr/bin/env python

"""Summarization Routines for Parity App

CERN Webfest 2017

This module contains the routines for:
    - Representative Message retrieval
    - Message summarization

"""

from datetime import datetime
from typing import List, Dict

from utils import whole_text, sort_summary
from ntlk_rake import topic_extraction_rake
from gensim.summarization import summarize, keywords
from textrank import representative_msgs_textrank
from lex_and_kl_summary import summarize_kl, summarize_lexpagerank

Message = Dict[str, datetime]

REPRESENTATIVE_METHODS = ['textrank'] #, 'gensim']
SUMMARIZE_METHODS = ['gensim', 'lexrank', 'kl']
KEYWORDS_METHODS = ['RAKE', 'gensim']


def representative_msgs(messages: List[Message], method='textrank') -> List[Message]:

    if method == 'textrank':
        return representative_msgs_textrank(messages)
    # elif method == 'gensim':
    #     text =
    #     return summarize(text, split=True)


def summarize_msgs(messages: List[Message], method='kl') -> str:
    text = whole_text(messages)

    if method == 'gensim':
        return summarize(text)
    elif method == 'lexrank':
        return sort_summary(summarize_lexpagerank(text), messages)
    elif method == 'kl':
        return sort_summary(summarize_kl(text), messages)


def keywords_from_msgs(messages: List[Message], method='gensim') -> List[str]:

    text = whole_text(messages)

    if method == 'RAKE':
        return topic_extraction_rake(text)
    elif method == 'gensim':
        return keywords(text)
    elif method == 'mglda':
        raise NotImplementedError("Not Yet")

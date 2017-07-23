#!/usr/bin/env python

"""Summarization Routines for Parity App

CERN Webfest 2017

This module contains the routines for:
    - Representative Message retrieval
    - Message summarization

"""

from datetime import datetime
from typing import List, Dict

from utils import whole_text

from ntlk_rake import topic_extraction_rake

from gensim.summarization import summarize, keywords

from textrank import representative_msgs_textrank

from lex_and_kl_summary import summarize_kl, summarize_lexpagerank

Message = Dict[str, datetime]


def representative_msgs(messages: List[Message], method) -> List[Message]:

    if method == 'textrank':
        return representative_msgs_texrank(messages)
    elif method == 'gensim':
        return summarize(text, split=True)


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

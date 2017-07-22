#!/usr/bin/env python

"""Summarization Routines for Parity App

CERN Webfest 2017

This module contains the routines for:
    - Representative Message retrieval
    - Message summarization

"""

from typing import List, Dict, NewType
from datetime import datetime
import dateutil.parser
import json


Message = Dict[str, datetime]


def load_sample(file='data/sample_chat.json'):
    with open(file, 'r') as f:
        sample = json.load(f)

    for d in sample:
        d['timestamp'] = dateutil.parser.parse(d['timestamp'])

    return sample


def load_sample_text(file='data/sample_chat.json', lines=None):
    messages = [d['content'] for d in load_sample(file)]
    if lines is not None:
        messages = messages[:lines]
    return ". ".join(messages)


def representative_msgs(messages: List[Message]) -> List[Message]:
    pass


def summarize_msgs(messages: List[Message]) -> str:
    pass


def relevant_topics(messages: List[Message]) -> List[str]:
    pass

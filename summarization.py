#!/usr/bin/env python

"""Summarization Routines for Parity App

CERN Webfest 2017

This module contains the routines for:
    - Representative Message retrieval
    - Message summarization

"""

from typing import List, Dict, NewType
from datetime import datetime
import json


Message = Dict[str, datetime]


def load_sample(file='sample.json'):
    with open(file, 'r') as f:
        return json.load(f)


def representative_msgs(messages: List[Message]) -> List[Message]:
    print(messages)
    pass


def summarize_msgs(messages: List[Message]) -> str:
    print(messages)
    pass


if __name__ == '__main__':
    representative_msgs(load_sample())
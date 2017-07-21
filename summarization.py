#!/usr/bin/env python

"""Summarization Routines for Parity App

CERN Webfest 2017

This module contains the routines for:
    - Representative Message retrieval
    - Message summarization

"""

from typing import List, Dict, NewType
from datetime import datetime

Message = Dict[str, datetime]


def representative_msgs(messages: List[Message]) -> List[Message]:
    pass


def summarize_msgs(messages: List[Message]) -> str:
    pass
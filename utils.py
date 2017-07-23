import dateutil.parser
import json
from nltk import sent_tokenize, word_tokenize


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
    return whole_text(load_sample(file), lines=lines)


def tokenize_for_mglda(messages):

    def _tokenize_message(message):
        sentences = sent_tokenize(message)
        tokenized_sentences = [word_tokenize(s) for s in sentences]
        return tokenized_sentences

    return [_tokenize_message(m['content']) for m in messages]


def sort_summary(text, messages):
    sentences = sent_tokenize(text)
    sentences = [s.strip('. ') for s in sentences]
    sorted_sents = []
    for message in messages:
        if any(s in message['content'] for s in sentences):
            sorted_sents.append(message['content'])
    return ". ".join(sorted_sents)

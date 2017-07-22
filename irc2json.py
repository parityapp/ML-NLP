#!/usr/bin/env python

import json
import sys
from datetime import datetime


def irc2json(text):
    messages = []
    for line in text.split('\n'):
        if line.startswith("*"):
            continue
        if len(line) < 1:
            continue
        user, content = line.split('> ', 1)
        user = user.strip('<>')
        time = datetime.now().isoformat()

        message = {
            "content": content,
            "userid": user,
            "timestamp": time
        }
        messages.append(message)
    return messages


if __name__ == '__main__':

    for file in sys.argv[1:]:
        with open(file, 'r') as fr:
            messages = irc2json(fr.read())
        with open(file.replace('.txt', '')+'.json', 'w') as fw:
            json.dump(messages, fw)

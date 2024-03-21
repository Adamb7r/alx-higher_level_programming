#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        lenght = len(sentence)
        first = None
    else:
        lenght = len(sentence)
        first = sentence[0]
    return lenght, first

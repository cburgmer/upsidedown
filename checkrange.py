#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find all characters in Latin like scripts that are flagged REVERSED or TURNED.

Example::
    $ python3 checkrange.py
    'ʻ' ʻ MODIFIER LETTER TURNED COMMA
    'ʽ' ʽ MODIFIER LETTER REVERSED COMMA
    'ˁ' ˁ MODIFIER LETTER REVERSED GLOTTAL STOP
    '‛' ‛ SINGLE HIGH-REVERSED-9 QUOTATION MARK
    '‟' ‟ DOUBLE HIGH-REVERSED-9 QUOTATION MARK
    '‵' ‵ REVERSED PRIME
    ...

Needs Python3.

You need the Scripts.txt file from Unicode::
    $ wget http://unicode.org/Public/UNIDATA/Scripts.txt
"""
import unicodedata
from util import readScriptRanges, CharacterRangeIterator

ranges = readScriptRanges()
for c in CharacterRangeIterator(ranges):
    try:
        name = unicodedata.name(c)
    except ValueError:
        continue
    if 'REVERSED' in name or 'TURNED' in name:
        print(repr(c), c, name)

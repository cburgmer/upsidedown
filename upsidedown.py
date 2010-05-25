#!/usr/bin/python
# -*- coding: utf-8 -*-

u"""
Simple module that "flips" latin characters in a string to create an
"upside-down" impression. Makes extensive use of compatible latin characters
encoded in Unicode.

Support for diacritics offered through combining diacritical marks. Depends on
proper rendering though.

2008-2010 Christoph Burgmer (cburgmer@ira.uka.de)

      ˙ǝɹɐʍʇɟos ǝɥʇ uı sƃuılɐǝp ɹǝɥʇo ɹo ǝsn ǝɥʇ ɹo ǝɹɐʍʇɟos ǝɥʇ ɥʇıʍ uoıʇɔǝuuoɔ
         uı ɹo ɟo ʇno 'ɯoɹɟ ƃuısıɹɐ 'ǝsıʍɹǝɥʇo ɹo ʇɹoʇ 'ʇɔɐɹʇuoɔ ɟo uoıʇɔɐ uɐ uı
  ɹǝɥʇǝɥʍ 'ʎʇılıqɐıl ɹǝɥʇo ɹo sǝƃɐɯɐp 'ɯıɐlɔ ʎuɐ ɹoɟ ǝlqɐıl ǝq sɹǝploɥ ʇɥƃıɹʎdoɔ
  ɹo sɹoɥʇnɐ ǝɥʇ llɐɥs ʇuǝʌǝ ou uı ˙ʇuǝɯǝƃuıɹɟuıuou puɐ ǝsodɹnd ɹɐlnɔıʇɹɐd ɐ ɹoɟ
ssǝuʇıɟ 'ʎʇılıqɐʇuɐɥɔɹǝɯ ɟo sǝıʇuɐɹɹɐʍ ǝɥʇ oʇ pǝʇıɯıl ʇou ʇnq ƃuıpnlɔuı 'pǝıldɯı
      ɹo ssǝɹdxǝ 'puıʞ ʎuɐ ɟo ʎʇuɐɹɹɐʍ ʇnoɥʇıʍ '"sı sɐ" pǝpıʌoɹd sı ǝɹɐʍʇɟos ǝɥʇ
                                 ˙ǝɹɐʍʇɟos ǝɥʇ ɟo suoıʇɹod lɐıʇuɐʇsqns ɹo sǝıdoɔ
  llɐ uı pǝpnlɔuı ǝq llɐɥs ǝɔıʇou uoıssıɯɹǝd sıɥʇ puɐ ǝɔıʇou ʇɥƃıɹʎdoɔ ǝʌoqɐ ǝɥʇ
                                            :suoıʇıpuoɔ ƃuıʍolloɟ ǝɥʇ oʇ ʇɔǝɾqns
 'os op oʇ pǝɥsıuɹnɟ sı ǝɹɐʍʇɟos ǝɥʇ ɯoɥʍ oʇ suosɹǝd ʇıɯɹǝd oʇ puɐ 'ǝɹɐʍʇɟos ǝɥʇ
ɟo sǝıdoɔ llǝs ɹo/puɐ 'ǝsuǝɔılqns 'ǝʇnqıɹʇsıp 'ɥsılqnd 'ǝƃɹǝɯ 'ʎɟıpoɯ 'ʎdoɔ 'ǝsn
    oʇ sʇɥƃıɹ ǝɥʇ uoıʇɐʇıɯıl ʇnoɥʇıʍ ƃuıpnlɔuı 'uoıʇɔıɹʇsǝɹ ʇnoɥʇıʍ ǝɹɐʍʇɟos ǝɥʇ
   uı lɐǝp oʇ '("ǝɹɐʍʇɟos" ǝɥʇ) sǝlıɟ uoıʇɐʇuǝɯnɔop pǝʇɐıɔossɐ puɐ ǝɹɐʍʇɟos sıɥʇ
 ɟo ʎdoɔ ɐ ƃuıuıɐʇqo uosɹǝd ʎuɐ oʇ 'ǝƃɹɐɥɔ ɟo ǝǝɹɟ 'pǝʇuɐɹƃ ʎqǝɹǝɥ sı uoıssıɯɹǝd

                                                            ǝsuǝɔıl ʇıɯ :ǝsuǝɔıl
"""

__all__ = ["transform"]
__version__ = '0.2'
__author__ = 'Christoph Burgmer <cburgmer@ira.uka.de>'
__url__ = 'http://github.com/cburgmer/upsidedown'
__license__ = 'MIT'

import unicodedata

BASE_LATIN_FLIP = u"ɐqɔpǝɟƃɥıɾʞlɯuodbɹsʇnʌʍxʎz"

OTHERS_FLIP = {'!': u'¡', '?': u'¿', '(': ')', '{': '}', ';': u'؛', '>': '<',
    '\'': ',','.': u'˙'}

# See:
# http://de.wikipedia.org/wiki/Unicode-Block_Kombinierende_diakritische_Zeichen
UNICODE_COMBINING_DIACRITICS = {u'̈': u'̤', u'̊': u'̥', u'́': u'̗', u'̀': u'̖',
    u'̇': u'̣', u'̃': u'̰', u'̄': u'̱', u'̂': u'̬', u'̆': u'̯', u'̌': u'̭',
    u'̑': u'̮', u'̍': u'̩'}

TRANSLITERATIONS = {u'ß': 'ss'}

# character lookup
_CHARLOOKUP = dict([(unichr(charOrd), BASE_LATIN_FLIP[i]) for i, charOrd \
    in enumerate(range(ord('a'), ord('z') + 1))])
_CHARLOOKUP.update(OTHERS_FLIP)
# get reverse direction
for char in _CHARLOOKUP.copy():
    _CHARLOOKUP[_CHARLOOKUP[char]] = char

# lookup for diacritical marks, reverse first
_DIACRITICSLOOKUP = dict([(UNICODE_COMBINING_DIACRITICS[char], char) \
    for char in UNICODE_COMBINING_DIACRITICS])
_DIACRITICSLOOKUP.update(UNICODE_COMBINING_DIACRITICS)

def transform(string, transliterations=None):
    u"""
    Transform the string to "upside-down" writing.

    Example:

        >>> import upsidedown
        >>> print upsidedown.transform('hello world!')
        ¡plɹoʍ ollǝɥ

    For languages with diacritics you might want to supply a transliteration to
    work around missing (rendering of) upside-down forms:
        >>> import upsidedown
        >>> print upsidedown.transform(u'Köln', transliterations={u'ö': 'oe'})
        ulǝoʞ
    """
    transliterations = transliterations or TRANSLITERATIONS

    string = string.lower()
    for character in transliterations:
        string = string.replace(character, transliterations[character])

    inputChars = list(string)
    inputChars.reverse()

    output = []
    for character in inputChars:
        if character in _CHARLOOKUP:
            output.append(_CHARLOOKUP[character])
        else:
            charNormalised = unicodedata.normalize("NFD", character)

            for c in charNormalised[:]:
                if c in _CHARLOOKUP:
                    charNormalised = charNormalised.replace(c, _CHARLOOKUP[c])
                elif c in _DIACRITICSLOOKUP:
                    charNormalised = charNormalised.replace(c,
                        _DIACRITICSLOOKUP[c])

            output.append(unicodedata.normalize("NFC", charNormalised))

    return ''.join(output)

def main():
    """Main method for running upsidedown.py from the command line."""
    import sys
    import locale
    _, default_encoding = locale.getdefaultlocale()

    line = sys.stdin.readline().decode(default_encoding)

    while line:
        line = line.strip("\n")
        print transform(line).encode(default_encoding)

        line = sys.stdin.readline().decode(default_encoding)

if __name__ == "__main__":
    main()

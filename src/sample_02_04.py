#!/usr/bin/env python

import re
import unicodedata

if __name__ == '__main__':
    text = '    CLEANSing  によりテキストデータを変換すると　トラブルが少なくなります。'
    print('Before:', text)

    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'\s+', ' ', text)
    print('After:', text)

#!/usr/bin/env python

import urllib.request
import cchardet

if __name__ == '__main__':
    # "Japanese" wikipedia page URL written by Japanese
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'

    with urllib.request.urlopen(url) as res:
        byte = res.read()

        # convert character encoding (auto detect by cchardet)
        html = byte.decode(cchardet.detect(byte)['encoding'])
        print(html)

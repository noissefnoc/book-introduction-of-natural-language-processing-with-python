#!/usr/bin/env python

import urllib.request

if __name__ == '__main__':
    # "Japanese" wikipedia page URL written by Japanese
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'

    with urllib.request.urlopen(url) as res:
        byte = res.read()

        # convert character encoding
        html = byte.decode('utf-8')
        print(html)

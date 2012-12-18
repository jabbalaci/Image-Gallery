#!/usr/bin/env python

import json
import gallery
import webbrowser

def main():
    urls = []
    with open('test/test.json', 'r') as f:
        urls = json.load(f)
    dir = '/tmp/image-gallery'

    if gallery.generate(dir, urls):
        print '# gallery created'
        webbrowser.open_new_tab(dir + '/index.html')
    else:
        print '# something went wrong'


#############################################################################

if __name__ == "__main__":
    main()

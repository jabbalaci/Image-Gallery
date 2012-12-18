#!/usr/bin/env python

import os
import json
import shutil
import webbrowser
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'assets')),
    trim_blocks=False)


def verify(dir, urls):
    class NoUrls(Exception): pass
    class NotDir(Exception): pass

    try:
        if not os.path.exists(dir):
            print "# creating", dir
            os.makedirs(dir)
        if not os.path.isdir(dir):
            raise NotDir("# cannot create the directory {}".format(dir))
        if not urls:
            raise NoUrls("# specify at least one image")
        return True
    except (NoUrls, NotDir) as e:
        print e
        return False


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html(dir, urls):
    fname = "{dir}/index.html".format(dir=dir)
    context = {
        'urls': urls
    }
    #
    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)


def create_page_html(dir, index, url, length):
    fname = "{dir}/{name}.html".format(dir=dir, name=index)
    #
    if index == 0:
        prev = "{n}.html".format(n=index)
    else:
        prev = "{n}.html".format(n=index-1)
    #
    if index == length-1:
        next = "{n}.html".format(n=index)
    else:
        next = "{n}.html".format(n=index+1)
    #
    progress = int(float(index + 1) / length * 100)
    #
    context = {
        'prev': prev,
        'next': next,
        'url': url,
        'progress': progress,
        'index': index+1,
        'length': length,
        'first': "0.html",
        'last': "{n}.html".format(n=length-1),
        'clippy_text': url,
        'bgcolor': '#dddddd'
    }
    with open(fname, 'w') as f:
        html = render_template('page.html', context)
        f.write(html)


def generate(dir, urls):
    if not verify(dir, urls):
        return None
    # else, if everything is OK
    shutil.copy('{curr}/assets/style.css'.format(curr=PATH), dir)
    shutil.copy('{curr}/assets/clippy.swf'.format(curr=PATH), dir)
    #
    length = len(urls)
    for index, url in enumerate(urls):
        create_page_html(dir, index, url, length)
    #
    create_index_html(dir, urls)
    return True

#############################################################################

if __name__ == "__main__":
    urls = []
    with open('test/test.json', 'r') as f:
        urls = json.load(f)
    dir = '/tmp/image-gallery'

    generate(dir, urls)
    webbrowser.open_new_tab(dir + '/index.html')


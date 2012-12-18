Image-Gallery
=============

Creates a stylish image gallery from a list of URLs.

Typical use case: you scrape the URLs of some images and
you want to visualize them.

Live demo: [here](https://dl.dropbox.com/u/144888/wordpress/20121218_image-gallery/index.html)


Usage
-----

You can launch it directly (see `gallery.py`) or you can call it
from your script as a module (see `call_as_a_module.py`).
Collect the URLs in your script and pass them to the `generate` function.


Credits
-------

This image gallery is based on another project called
[gallerize](http://homework.nwsnet.de/). gallerize works
with *local* image files.

My image gallery works with *remote* files. My idea is that
you have a list of image URLs (that you scraped for instance)
and you want to visualize them without downloading them all first.

I reused the stylesheet of gallerize, so big thanks to Jochen Kupperschmidt
for his great work.
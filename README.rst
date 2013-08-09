REmbed-Markdown
===============

.. image:: https://secure.travis-ci.org/matt-thomson/rembed-markdown.png?branch=master
    :target: http://travis-ci.org/matt-thomson/rembed-markdown
.. image:: https://coveralls.io/repos/matt-thomson/rembed-markdown/badge.png
    :target: https://coveralls.io/r/matt-thomson/rembed
.. image:: https://codeq.io/github/matt-thomson/rembed-markdown/badges/master.png
    :target: https://codeq.io/github/matt-thomson/rembed-markdown/branches/master
.. image:: https://pypip.in/v/rembed-markdown/badge.png
    :target: https://crate.io/packages/rembed-markdown/
.. image:: https://pypip.in/d/rembed-markdown/badge.png
    :target: https://crate.io/packages/rembed-markdown/

Python Markdown extension for embedding content using `OEmbed`_.

REmbed-Markdown allows you to embed content in your Markdown websites and
documents from a wide range of producers.  You don't need to configure
anything - simply add the extension, and use a link with the text `[!embed]`:

::

    >>> md = markdown.Markdown(extensions=[REmbedExtension()])
    >>> embedding = md.convert('[!embed](http://www.youtube.com/watch?v=9bZkp7q19f0)')
    <iframe width="480" height="270" src="http://www.youtube.com/embed/9bZkp7q19f0?feature=oembed" frameborder="0" allowfullscreen></iframe>

Compatibility
-------------

REmbed-Markdown has been tested with Python 2.7 and 3.3.

Installation
------------

REmbed-Markdown can be installed using pip:

::

    pip install rembed-markdown

Contributing
------------

To report an issue, request an enhancement, or contribute a patch, go to
the REmbed-Markdown `GitHub`_ page.

.. _OEmbed: http://oembed.com
.. _GitHub: https://github.com/matt-thomson/rembed-markdown
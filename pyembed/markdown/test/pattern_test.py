# The MIT License(MIT)

# Copyright (c) 2013-2014 Matt Thomson

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pyembed.markdown.pattern import PyEmbedPattern

from hamcrest import assert_that, equal_to, none, not_none
from mock import patch, Mock


def test_should_match_pyembed_link():
    md = Mock()

    re = PyEmbedPattern(md).getCompiledRegExp()
    match = re.match('[!embed](http://www.example.com)')

    assert_that(match, not_none())


def test_should_match_pyembed_link_with_params():
    md = Mock()

    re = PyEmbedPattern(md).getCompiledRegExp()
    match = re.match('[!embed?param=value](http://www.example.com)')

    assert_that(match, not_none())


def test_should_not_match_non_pyembed_link():
    md = Mock()

    re = PyEmbedPattern(md).getCompiledRegExp()
    match = re.match('[example](http://www.example.com)')

    assert_that(match, none())


def test_should_substitute_link_with_embedding():
    source = '[!embed](http://www.example.com)'
    generic_embed_test(source, 'http://www.example.com', None, None, None)


def test_should_apply_max_height():
    source = '[!embed?max_height=200](http://www.example.com)'
    generic_embed_test(source, 'http://www.example.com', None, 200, None)


def test_should_apply_max_width():
    source = '[!embed?max_width=100](http://www.example.com)'
    generic_embed_test(source, 'http://www.example.com', 100, None, None)


def test_should_apply_max_height_and_width():
    source = '[!embed?max_width=100&max_height=200](http://www.example.com)'
    generic_embed_test(source, 'http://www.example.com', 100, 200, None)


def test_should_ignore_extra_params():
    source = '[!embed?max_height=200&extra=value](http://www.example.com)'
    generic_embed_test(source, 'http://www.example.com', None, 200, None)


def test_should_pass_through_template_path():
    md = Mock()
    pattern = PyEmbedPattern(md, 'templates')
    source = '[!embed](http://www.example.com)'
    match = pattern.getCompiledRegExp().match(source)

    with patch('pyembed.core.consumer.embed') as mock_embed:
        mock_embed.return_value = '<h1>Bees!</h1>'

        result = pattern.handleMatch(match)
        assert_that(result, not_none())

        mock_embed.assert_called_with(
            'http://www.example.com', None, None, 'templates')

    md.htmlStash.store.assert_called_with('<h1>Bees!</h1>')


def generic_embed_test(source, *embed_params):
    md = Mock()
    pattern = PyEmbedPattern(md)
    match = pattern.getCompiledRegExp().match(source)

    with patch('pyembed.core.consumer.embed') as mock_embed:
        mock_embed.return_value = '<h1>Bees!</h1>'

        result = pattern.handleMatch(match)
        assert_that(result, not_none())

        mock_embed.assert_called_with(*embed_params)

    md.htmlStash.store.assert_called_with('<h1>Bees!</h1>')

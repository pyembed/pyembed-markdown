from rembed.markdown.pattern import REmbedPattern

from hamcrest import assert_that, equal_to, none, not_none
from mock import patch, Mock


def test_should_match_rembed_link():
    md = Mock()

    re = REmbedPattern(md).getCompiledRegExp()
    match = re.match('[!embed](http://www.example.com)')

    assert_that(match, not_none())


def test_should_match_rembed_link_with_params():
    md = Mock()

    re = REmbedPattern(md).getCompiledRegExp()
    match = re.match('[!embed?param=value](http://www.example.com)')

    assert_that(match, not_none())


def test_should_not_match_non_rembed_link():
    md = Mock()

    re = REmbedPattern(md).getCompiledRegExp()
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
    pattern = REmbedPattern(md, 'templates')
    source = '[!embed](http://www.example.com)'
    match = pattern.getCompiledRegExp().match(source)

    with patch('rembed.core.consumer.embed') as mock_embed:
        mock_embed.return_value = '<h1>Bees!</h1>'

        result = pattern.handleMatch(match)
        assert_that(result, not_none())

        mock_embed.assert_called_with(
            'http://www.example.com', None, 200, 'templates')

    md.htmlStash.store.assert_called_with('<h1>Bees!</h1>')


def generic_embed_test(source, *embed_params):
    md = Mock()
    pattern = REmbedPattern(md)
    match = pattern.getCompiledRegExp().match(source)

    with patch('rembed.core.consumer.embed') as mock_embed:
        mock_embed.return_value = '<h1>Bees!</h1>'

        result = pattern.handleMatch(match)
        assert_that(result, not_none())

        mock_embed.assert_called_with(*embed_params)

    md.htmlStash.store.assert_called_with('<h1>Bees!</h1>')

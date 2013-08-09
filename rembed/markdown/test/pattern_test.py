from rembed.markdown.pattern import REmbedPattern

from hamcrest import assert_that, equal_to, none, not_none
from mock import patch


def test_should_match_rembed_link():
    re = REmbedPattern().getCompiledRegExp()
    match = re.match('[!embed](http://www.example.com)')
    assert_that(match, not_none())


def test_should_not_match_non_rembed_link():
    re = REmbedPattern().getCompiledRegExp()
    match = re.match('[example](http://www.example.com)')
    assert_that(match, none())


def test_should_substitute_link_with_embedding():
    pattern = REmbedPattern()
    source = '[!embed](http://www.example.com)'
    match = pattern.getCompiledRegExp().match(source)

    with patch('rembed.core.consumer.embed') as mock_embed:
        mock_embed.return_value = '<h1>Bees!</h1>'

        result = pattern.handleMatch(match)
        assert_that(result, equal_to('<h1>Bees!</h1>'))

        mock_embed.assert_called_with('http://www.example.com')

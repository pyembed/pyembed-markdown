from rembed.markdown.extension import REmbedExtension
import markdown

from hamcrest import assert_that, contains_string, equal_to, is_not
import pytest


def test_should_get_correct_embedding():
    md = markdown.Markdown(extensions=[REmbedExtension()])

    embedding = md.convert(
        '[!embed](https://twitter.com/BarackObama/status/266031293945503744)')

    assert_that(embedding, contains_string('Four more years.'))
    assert_that(embedding, is_not(contains_string('&gt;')))


def test_should_embed_with_max_height():
    md = markdown.Markdown(extensions=[REmbedExtension()])

    embedding = md.convert(
        '[!embed?max_height=200](http://www.youtube.com/watch?v=9bZkp7q19f0)')

    assert_that(embedding, contains_string('height="200"'))
    assert_that(embedding, is_not(contains_string('&gt;')))


def test_should_embed_with_custom_templates():
    template_path = 'rembed/markdown/test/fixtures/templates'
    md = markdown.Markdown(extensions=[REmbedExtension(template_path)])

    embedding = md.convert(
        '[!embed](http://www.youtube.com/watch?v=qrO4YZeyl0I)')

    assert_that(embedding, equal_to(
        '<p>Lady Gaga - Bad Romance by LadyGagaVEVO from ' +
        'http://www.youtube.com/watch?v=qrO4YZeyl0I</p>'))


@pytest.mark.xfail
def test_should_get_correct_embedding_when_initializing_by_name():
    md = markdown.Markdown(extensions=['rembed.markdown'])

    embedding = md.convert(
        '[!embed](https://twitter.com/BarackObama/status/266031293945503744)')

    assert_that(embedding, contains_string('Four more years.'))

from rembed.markdown.extension import REmbedExtension
import markdown

from hamcrest import assert_that, contains_string
import pytest


@pytest.mark.xfail
def test_should_get_correct_embedding():
    md = markdown.Markdown(extensions=[REmbedExtension()])
    embedding = md.convert(
        '![](https://twitter.com/BarackObama/status/266031293945503744)')
    assert_that(embedding, contains_string('Four more years.'))

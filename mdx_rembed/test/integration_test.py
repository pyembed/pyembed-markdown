import markdown

from hamcrest import *
import pytest

@pytest.mark.xfail
def test_should_get_correct_embedding():
    md = markdown.Markdown(extensions=['rembed'])
    embedding = md.convert('![](https://twitter.com/BarackObama/status/266031293945503744)')
    assert_that(embedding, contains_string('Four more years.'))
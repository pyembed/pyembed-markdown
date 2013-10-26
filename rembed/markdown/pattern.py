from markdown.inlinepatterns import Pattern
from rembed.core import consumer

REMBED_PATTERN = '\[!embed\]\((.*)\)'


class REmbedPattern(Pattern):

    def __init__(self, md):
        super(REmbedPattern, self).__init__(REMBED_PATTERN)

        self.md = md

    def handleMatch(self, m):
        url = m.group(2)
        html = consumer.embed(url)
        return self.md.htmlStash.store(html)

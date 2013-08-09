from markdown.inlinepatterns import Pattern
from rembed.core import consumer

REMBED_PATTERN = '\[!embed\]\((.*)\)'


class REmbedPattern(Pattern):

    def __init__(self):
        super(REmbedPattern, self).__init__(REMBED_PATTERN)

    def handleMatch(self, m):
        return consumer.embed(m.group(2))

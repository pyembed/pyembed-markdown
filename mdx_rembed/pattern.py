from markdown.inlinepatterns import Pattern

REMBED_PATTERN = 'abc'

class REmbedPattern(Pattern):
    def __init__(self):
        super(REmbedPattern, self).__init__(REMBED_PATTERN)

    def handleMatch(self, m):
        pass
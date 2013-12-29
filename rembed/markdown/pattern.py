from markdown.inlinepatterns import Pattern
from rembed.core import consumer

try:  # pragma: no cover
    from urlparse import parse_qs
except ImportError:  # pragma: no cover
    from urllib.parse import parse_qs

REMBED_PATTERN = '\[!embed(\?(.*))?\]\((.*)\)'


class REmbedPattern(Pattern):

    def __init__(self, md, template_path=None):
        super(REmbedPattern, self).__init__(REMBED_PATTERN)

        self.md = md
        self.template_path = template_path

    def handleMatch(self, m):
        url = m.group(4)
        (max_width, max_height) = self.__parse_params(m.group(3))
        html = consumer.embed(url, max_width, max_height, self.template_path)
        return self.md.htmlStash.store(html)

    def __parse_params(self, query_string):
        if not query_string:
            return (None, None)

        query_params = parse_qs(query_string)
        return (self.__get_query_param(query_params, 'max_width'),
                self.__get_query_param(query_params, 'max_height'))

    def __get_query_param(self, query_params, name):
        if name in query_params:
            return int(query_params[name][0])
        else:
            return None

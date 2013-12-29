from markdown.extensions import Extension

from . import pattern


class REmbedExtension(Extension):

    def __init__(self, template_path=None):
        self.template_path = template_path

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add(
            'rembed', pattern.REmbedPattern(md, self.template_path), '_begin')

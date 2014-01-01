from markdown.extensions import Extension

from . import pattern


class PyEmbedExtension(Extension):

    def __init__(self, template_path=None):
        self.template_path = template_path

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add(
            'pyembed', pattern.PyEmbedPattern(md, self.template_path), '_begin')

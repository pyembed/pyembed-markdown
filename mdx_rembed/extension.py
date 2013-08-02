from markdown.extensions import Extension

import pattern

class REmbedExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('rembed', pattern.REmbedPattern(), '_begin')
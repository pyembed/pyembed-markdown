from . import extension


def makeExtension(configs=None):  # pragma: no cover
    return extension.REmbedExtension()

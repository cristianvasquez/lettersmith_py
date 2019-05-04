from pathlib import PurePath
from markdown import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

from lettersmith import doc as Doc


MD_LANG_EXTENSIONS=(GithubFlavoredMarkdownExtension(),)


def house_markdown(s):
    """
    Just a wrapper for our house flavor of markdown.
    We use Github-flavored markdown as a base.
    """
    return markdown(s, extensions=MD_LANG_EXTENSIONS)


@Doc.uplifts_frontmatter
def render_doc(doc, extensions=MD_LANG_EXTENSIONS):
    """
    Render markdown in content field of doc dictionary.
    Updates the output path to .html.
    Returns a new doc.
    """
    content = markdown(doc.content, extensions=extensions)
    output_path = PurePath(doc.output_path).with_suffix(".html")
    return doc._replace(
        content=content,
        output_path=str(output_path)
    )


def parse_markdown(docs, extensions=MD_LANG_EXTENSIONS):
    """
    Markdown rendering plugin
    """
    for doc in docs:
        if Doc.has_ext(doc, ".md", ".markdown", ".mdown", ".txt"):
            yield render_doc(doc, extensions)
        else:
            yield doc
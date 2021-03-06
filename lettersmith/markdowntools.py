from markdown import markdown as md
from mdx_gfm import GithubFlavoredMarkdownExtension

from lettersmith import docs as Docs
from lettersmith.functional.func import compose
from lettersmith.html import strip_html


def markdown(s):
    """
    Render markdown on content field.
    """
    return md(s, extensions=(GithubFlavoredMarkdownExtension(),))


strip_markdown = compose(strip_html, markdown)
content = Docs.renderer(markdown)

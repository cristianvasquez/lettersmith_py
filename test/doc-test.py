"""
Unit tests for Doc
"""

import snapshottest
from pathlib import Path
from lettersmith import doc as Doc

module_path = Path(__file__).parent
fixtures_path = Path(module_path, "package_data", "fixtures")


class TestLoadBareDoc(snapshottest.TestCase):

    def test_content(self):
        doc_path = fixtures_path.joinpath("Bare doc.md")
        doc = Doc.load(doc_path)
        self.assertMatchSnapshot(doc)


class TestParseFrontmatter(snapshottest.TestCase):

    def test_content(self):
        doc_path = fixtures_path.joinpath("Doc with meta.md")
        doc = Doc.load(doc_path)
        doc = Doc.parse_frontmatter(doc)
        self.assertMatchSnapshot(doc)

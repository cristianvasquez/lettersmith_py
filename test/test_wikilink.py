import unittest
from lettersmith import wikimarkup


class RestParseWikilink(unittest.TestCase):
    def test_returns_tuple(self):
        s = "[[WikiLink]]"
        result = wikimarkup._parse_wikilink(s)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_well_formed(self):
        slug, title = wikimarkup._parse_wikilink("[[WikiLink]]")
        self.assertEqual(slug, "wikilink")
        self.assertEqual(title, "WikiLink")

    def test_piped(self):
        slug, title = wikimarkup._parse_wikilink("[[dog | Dogs]]")
        self.assertEqual(slug, "dog")
        self.assertEqual(title, "Dogs")

    def test_piped_snug(self):
        slug, title = wikimarkup._parse_wikilink("[[dog|Dogs]]")
        self.assertEqual(slug, "dog")
        self.assertEqual(title, "Dogs")

    def test_piped_space(self):
        slug, title = wikimarkup._parse_wikilink("[[dog  |       Dogs]]")
        self.assertEqual(slug, "dog")
        self.assertEqual(title, "Dogs")


class TestStripWikilinks(unittest.TestCase):
    def test_returns_tuple(self):
        s = "lorem ipsum [[WikiLink]] dolar [[wiki| Link]]"
        result = wikimarkup.strip_wikilinks(s)
        self.assertEqual(result,
                         "lorem ipsum WikiLink dolar Link"
                         )


if __name__ == '__main__':
    unittest.main()

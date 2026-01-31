import unittest
from gencontent import extract_title


class TestMarkdownRandomStuff(unittest.TestCase):
    def test_title_extraction(self):
        node = """# This is a title in markdown
        just some text
        """
        title = extract_title(node)
        self.assertEqual(title, "This is a title in markdown")

    def test_title_extraction_not_at_beggining(self):
        node = """Some text  
Some more text  
This is before the title  
# This is a title in markdown
just some text
        """
        title = extract_title(node)
        self.assertEqual(title, "This is a title in markdown")

    def test_title_extraction_bad_format(self):
        node = """#This is a title in markdown
        just some text
        """

        with self.assertRaises(Exception) as err:
            extract_title(node)
        self.assertEqual(str(err.exception), "Could not extract title")


if __name__ == "__main__":
    unittest.main()

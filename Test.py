import unittest
from lib.Author import Author
from lib.Article import Article
from lib.Magazine import Magazine

class TestAuthorMethods(unittest.TestCase):
    def test_author_articles(self):
        author = Author("Author Name")
        magazine = Magazine("Magazine Name", "Category")
        article = author.add_article(magazine, "Article Title")
        
        self.assertEqual(author.articles(), [article])


if __name__ == "__main__":
    unittest.main()

import unittest
from Author import Author
from Article import Article
from Magazine import Magazine

class TestAuthorMethods(unittest.TestCase):
    def test_author_articles(self):
        author = Author("Author Name")
        magazine = Magazine("Magazine Name", "Category")
        article = author.add_article(magazine, "Article Title")
        
        self.assertEqual(author.articles(), [article])

    # Add more test cases for other methods

if __name__ == "__main__":
    unittest.main()

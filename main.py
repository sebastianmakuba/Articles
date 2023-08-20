from Author import Author
from Article import Article
from Magazine import Magazine

if __name__ == "__main__":
    # Create authors, magazines, and articles
    author1 = Author("Author 1")
    author2 = Author("Author 2")

    magazine1 = Magazine("Magazine 1", "Category 1")
    magazine2 = Magazine("Magazine 2", "Category 2")

    article1 = author1.add_article(magazine1, "Article 1 by Author 1")
    article2 = author2.add_article(magazine1, "Article 2 by Author 2")
    article3 = author1.add_article(magazine2, "Article 3 by Author 1")

    # Test object relationships
    print(article1.author().name())  # Output: Author 1
    print(article1.magazine().name())  # Output: Magazine 1

    print(author1.articles())  # Output: [Article 1 by Author 1, Article 3 by Author 1]
    print(author1.magazines())  # Output: [Magazine 1, Magazine 2]

    print(magazine1.contributors())  # Output: [Author 1, Author 2]
    print(Magazine.all())  # Output: [Magazine 1, Magazine 2]

    print(Magazine.article_titles("Magazine 1"))  # Output: [Article 1 by Author 1, Article 2 by Author 2]
    print(Magazine.contributing_authors("Magazine 1"))  # Output: []

    print(Magazine.article_titles("Magazine 2"))  # Output: [Article 3 by Author 1]
    print(Magazine.contributing_authors("Magazine 2"))  # Output: [Author 1]

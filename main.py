from lib.Author import Author
from lib.Article import Article
from lib.Magazine import Magazine

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
    print("Author:", article1.author().name())
    print("Magazine:", article1.magazine().name())
    
    print("\nArticles by Author:")
    for article in author1.articles():
        print(article.title())

    print("\nMagazines contributed by Author:")
    for magazine in author1.magazines():
        print(magazine.name())

    print("\nContributors for Magazine:")
    for contributor in magazine1.contributors():
        print(contributor.name())

    print("\nAll Magazines:")
    for magazine in Magazine.all():
        print(magazine.name())

    print("\nArticle Titles for Magazine 1:")
    for title in Magazine.article_titles("Magazine 1"):
        print(title)

    print("\nContributing Authors for Magazine 1:")
    for contributor in Magazine.contributing_authors("Magazine 1"):
        print(contributor.name())

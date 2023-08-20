from Article import Article
class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def contributors(self):
        return list(set(article.author() for article in self._articles))

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all if magazine.name() == name), None)

    @classmethod
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            return [article.title() for article in magazine._articles]
        return []

    @classmethod
    def contributing_authors(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            author_counts = {}
            for article in magazine._articles:
                author = article.author()
                if author in author_counts:
                    author_counts[author] += 1
                else:
                    author_counts[author] = 1
            return [author for author, count in author_counts.items() if count > 2]
        return []

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Defines the human-readable string representation of the object."""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Defines the developer-friendly representation of the object."""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def __len__(self):
        """Defines the behavior of len() on the object."""
        return self.pages

# Example usage
book = Book("1984", "George Orwell", 328)

# __str__
print(str(book))  # Output: '1984' by George Orwell
print(book)       # Output: '1984' by George Orwell

# __repr__
print(repr(book))  # Output: Book(title='1984', author='George Orwell', pages=328)

# __len__
print(len(book))   # Output: 328

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    year_first_published INTEGER NOT NULL,
    current_price_dollar REAL NOT NULL
);

CREATE TABLE authors (
    author_id PRIMARY KEY,
    author_name TEXT NOT NULL,
    year_born INTEGER NOT NULL,
    year_died INTEGER
);

CREATE TABLE authors_books (
    author_id TEXT NOT NULL,
    book_id TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (author_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
);

CREATE VIEW books_all_infos AS
    SELECT
        title,
        year_first_published,
        current_price_dollar,
        author_name,
        year_born,
        year_died
    FROM
        books
        JOIN authors_books USING (book_id)
        JOIN authors USING (author_id)
    ORDER BY
        year_first_published ASC,
        title ASC,
        author_name ASC
;

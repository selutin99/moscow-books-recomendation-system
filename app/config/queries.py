class Queries:
    GET_BOOKS_COUNT = 'SELECT COUNT(*) FROM moscow_books.book;'
    GET_USER_HISTORY_BOOK_IDS = 'SELECT catalogueRecordID FROM moscow_books.books_issuance WHERE readerID=%s;'
    GET_BOOKS_HISTORY = 'SELECT recId AS id, aut AS author, title FROM moscow_books.book WHERE recId=%s;'

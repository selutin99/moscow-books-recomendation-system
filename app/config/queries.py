class Queries:
    GET_BOOKS_COUNT = 'SELECT COUNT(*) FROM moscow_books.book;'
    GET_USER_HISTORY_BOOK_IDS = 'SELECT catalogueRecordID FROM moscow_books.books_issuance WHERE readerID=%s;'
    GET_BOOK = 'SELECT recId AS id, aut AS author, title FROM moscow_books.book WHERE recId=%s;'

    GET_BOOK_NEWCOMER = 'SELECT recId AS id, aut AS author, title FROM moscow_books.book LIMIT 10 OFFSET %s;'

    FIND_BOOK_COEFFICIENT = 'SELECT (place+publ+yea+lan+rubrics+person+serial+material+biblevel)/10 as summary FROM moscow_books.books_converted WHERE recId=%s;'
    FIND_NEAREST_BOOK = 'SELECT recId, (place+publ+yea+lan+rubrics+person+serial+material+biblevel)/10 as summary FROM moscow_books.books_converted LIMIT 100 OFFSET %s;'

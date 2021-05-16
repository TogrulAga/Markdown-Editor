def print_book_info(title, author=None, year=None):
    #  Write your code here
    print(f'"{title}"{" was written " if author is not None or year is not None else ""}\
{"by " + author + " " if author is not None else ""}\
{"in " + year if year is not None else ""}')

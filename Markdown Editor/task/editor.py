# write your code here
class MarkDown:
    text = None
    document = ""

    @staticmethod
    def choose_formatter():
        formatter = input("- Choose a formatter:")

        if formatter == "header":
            MarkDown.header()
        elif formatter == "plain":
            MarkDown.plain()
        elif formatter == "new-line":
            MarkDown.new_line()
        elif formatter == "link":
            MarkDown.link()
        elif formatter == "bold":
            MarkDown.bold()
        elif formatter == "italic":
            MarkDown.italic()
        elif formatter == "inline-code":
            MarkDown.inline_code()
        elif formatter == "ordered-list":
            MarkDown.markdown_list(ordered=True)
        elif formatter == "unordered-list":
            MarkDown.markdown_list()
        elif formatter == "!help":
            MarkDown.help()
        elif formatter == "!done":
            return MarkDown.done()
        else:
            print("Unknown formatting type or command. Please try again.")

        print(MarkDown.document)
        return 1

    @staticmethod
    def get_text():
        MarkDown.text = input("Text: ")

    @staticmethod
    def header():
        level = int(input("Level: "))
        MarkDown.get_text()
        MarkDown.document += f"{'#' * level} {MarkDown.text}\n"

    @staticmethod
    def plain():
        MarkDown.get_text()
        MarkDown.document += MarkDown.text

    @staticmethod
    def new_line():
        MarkDown.document += "\n"

    @staticmethod
    def link():
        label = input("Label: ")
        url = input("URL: ")
        MarkDown.document += f"[{label}]({url})"

    @staticmethod
    def bold():
        MarkDown.get_text()
        MarkDown.document += f"**{MarkDown.text}**"

    @staticmethod
    def italic():
        MarkDown.get_text()
        MarkDown.document += f"*{MarkDown.text}*"

    @staticmethod
    def inline_code():
        MarkDown.get_text()
        MarkDown.document += f"`{MarkDown.text}`"

    @staticmethod
    def markdown_list(ordered: bool = False):
        while True:
            n_rows = int(input("Number of rows: "))
            if n_rows <= 0:
                print("The number of rows should be greater than zero")
            else:
                break

        for i in range(1, n_rows + 1):
            MarkDown.document += f'{str(i) + ". " if ordered else "* "}{input(f"Row {i}: ")}\n'

    @staticmethod
    def help():
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    @staticmethod
    def done():
        with open("output.md", 'w', encoding='utf-8') as file:
            file.write(MarkDown.document)

        return 0


def main():
    MarkDown.choose_formatter()
    while MarkDown.choose_formatter():
        pass


main()

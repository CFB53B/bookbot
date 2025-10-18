def get_book_text():
	with open("/home/adamwilliams/github.com/CFB53B/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read()
		print(file_contents)

def main():
	book_contents = get_book_text
	print(book_contents)

main()



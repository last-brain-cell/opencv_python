
class Book:
    def __init__(self, id, title, author, content):
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.last_page = 0
        # print("Book Created")

    def display_page(self):
        print(self.content[self.last_page])

    def next_page(self):
        self.last_page += 1
        self.display_page()

    def goto_page(self, page_no):
        self.last_page = page_no
        self.display_page()


class Library:
    def __init__(self):
        self.collection = dict()
        self.active_book = None

    def add_book_to_collection(self, id, title, author, content = ['Page1', 'Page2', 'Page3', 'so on...']):
        new_book = Book(id, title, author, content)
        self.collection[id] = new_book
        print(f"{title} by {author} added to collection. (id={id})")

    def activate_book(self, id):
        self.active_book = id

    def display_page(self):
        return self.collection[self.active_book].display_page()

    def turn_page(self):
        return self.collection[self.active_book].next_page()

    def goto_page(self, page):
        return self.collection[self.active_book].goto_page(page)

    def display_collection(self):
        print(self.collection.keys(), f"\nNumber of Books: {len(self.collection.keys())}")


kindle = Library()

kindle.add_book_to_collection("ID1234", "The Catcher in the Rye", "J.D. Salinger", ['The quick brown fox jumps over the lazy dog.', 'She sells seashells by the seashore.', 'Jack and Jill went up the hill to fetch a pail of water.', 'The cat in the hat sat on the mat.', 'I scream, you scream, we all scream for ice cream.'])
kindle.add_book_to_collection("ID5678", "To Kill a Mockingbird", "Harper Lee", ['To be or not to be, that is the question.', "All the world's a stage, and all the men and women merely players.", 'The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.', 'It is not in the stars to hold our destiny but in ourselves.', 'We know what we are, but know not what we may be.'])
kindle.add_book_to_collection("ID9101", "1984", "George Orwell", ['The only way to do great work is to love what you do.', 'Success is not final, failure is not fatal: it is the courage to continue that counts.', 'The only true wisdom is in knowing you know nothing.', "Don't watch the clock; do what it does. Keep going.", "I have not failed. I've just found 10,000 ways that won't work."])
kindle.add_book_to_collection("ID1121", "The Great Gatsby", "F. Scott Fitzgerald", ['The world is a book and those who do not travel read only one page.', 'Not all those who wander are lost.', 'I am not a product of my circumstances. I am a product of my decisions.', "Believe you can and you're halfway there.", "In three words I can sum up everything I've learned about life: it goes on."])
kindle.add_book_to_collection("ID3141", "Pride and Prejudice", "Jane Austen", ['A person who never made a mistake never tried anything new.', 'Imagination is more important than knowledge.', 'The greatest glory in living lies not in never falling, but in rising every time we fall.', 'Life is like riding a bicycle. To keep your balance, you must keep moving.', 'It does not matter how slowly you go as long as you do not stop.'])


kindle.activate_book("ID1234")
kindle.display_page()
kindle.turn_page()

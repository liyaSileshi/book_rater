# rater/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rater.models import Book, Comment
from rater.forms import BookForm, CommentForm
from django.urls import reverse
# Create your tests here.

class RaterTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_book_slugify_on_save(self):
        """ Tests the slug generated when saving a Book. """
        # Create and save a new book to the test database.
        book = Book(title="My Test Book", summary="test", author='lorem', isbn=0000, image='ipsum')
        book.save()
        self.assertEqual(book.slug, "my-test-book")

    def test_comment_author_is_correct(self):
        # tests the author of the comment
        user = User()
        user.save()
        book = Book(title="My Test Book", summary="test", author='lorem', isbn=0000, image='ipsum')
        book.save()
        comment = Comment(comment="book comment", rating=4, author=user, book_id=book.id)
        comment.save()
        self.assertEqual(comment.author, user)

class BookListViewTests(TestCase):
    def test_multiple_books(self):
        # Make some test data to be displayed on the mainpage.
        Book.objects.create(title="My Test Book", summary="test", author='lorem', isbn=0000, image='ipsum')
        Book.objects.create(title="Another Test Book", summary="test2", author='lorem1', isbn=0000, image='ipsum1')

        # Issue a GET request to the BookRater homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/rater/')

        # Check that the response is 200 okay.
        self.assertEqual(response.status_code, 200)

        # Check that the number of books passed to the template
        # matches the number of books we have in the database.
        responses = response.context['books']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Book: My Test Book>', '<Book: Another Test Book>'],
            ordered=False
        )

class BookDetailViewTests(TestCase):
    def test_one_book_detail(self):
        #create a fake book
        Book.objects.create(title="My Test Book", summary="test", author='lorem', isbn=0000, image='ipsum')

        # Issue a GET request to the details page.
        # When we make a request, we get a response back.
        response = self.client.get('/rater/my-test-book/')
        self.assertEqual(response.status_code, 200)

        book = response.context['book']
        self.assertEqual(book.title, "My Test Book")
    
class BookCreateViewTests(TestCase):
    def test_book_create(self):
        # check that the creation book form loads when visiting
        response = self.client.get('/rater/new/')
        self.assertEqual(response.status_code, 200)

        form = BookForm()
        self.assertTrue(form)

        self.assertIn(b'book title', response.content)
        self.assertIn(b'book description', response.content)

    def test_page_form_post(self):
        #make a form dictionary

        form = {'title':"My Test Book",
                        'summary':"testing", 'author': 'writer',
                        'isbn':0000, 'image':'ipsum'}

        response = self.client.post('/rater/new/', form = form)
        self.assertEqual(response.status_code, 200)

        #create a book form with the form data and check if it's valid
        form_book = BookForm(data=form)
        form_book.save()
        self.assertTrue(form_book.is_valid())
        #check if the form is saved in the test db
        book = Book.objects.get(title = 'My Test Book')
        self.assertEqual(book.title, 'My Test Book')
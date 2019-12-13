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

# class PageDetailViewTests(TestCase):
#     def test_one_page_detail(self):
#         user = User.objects.create()

#         #create a fake page
#         Page.objects.create(title="My Test Page", content="test", author=user)

#         # Issue a GET request to the details page.
#         # When we make a request, we get a response back.
#         response = self.client.get('/my-test-page/')
#         self.assertEqual(response.status_code, 200)

#         page = response.context['page']
#         self.assertEqual(page.title, "My Test Page")
    
# class PageCreateViewTests(TestCase):
#     def test_page_create(self):
#         # check that the creation page form loads when visiting
#         response = self.client.get('/new/')
#         self.assertEqual(response.status_code, 200)

#         form = PageForm()
#         self.assertTrue(form)

#         self.assertIn(b'Title of your page.', response.content)
#         self.assertIn(b'Write the content of your page here.', response.content)

#     def test_page_form_post(self):
#         #get a user object
#         user = User.objects.create()

#         #make a form dictionary
#         form = {'title':"My Test Page",
#                         'content':"testing", 'author': user.id}

#         response = self.client.post('/new/', form = form)
#         self.assertEqual(response.status_code, 302) #not working

#         #create a page form with the form data and check if it's valid
#         form_page = PageForm(data=form)
#         form_page.save()
#         self.assertTrue(form_page.is_valid())

#         users = User.objects.all()
#         self.assertEqual(len(users), 1)

#         #check if the form is saved in the test db
#         page = Page.objects.get(title = 'My Test Page')
#         # print(page.author)
#         # self.assertEqual(page.title, 'My Test Page')
from django.test import TestCase

from ..forms import CommentForm
from ..models import Comment

class FormTests(TestCase):
    def test_valid_form(self):
        form = CommentForm({'author':'test', 'body':'This is a test body'})
        self.assertTrue(form.is_valid())

    def test_clean_author_returns_anonymous_if_author_not_given(self):
        form = CommentForm({'body':'This is a test body'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['author'], 'Anonymous')
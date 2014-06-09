from django.test import TestCase

from .models import Tag, Post


class TagTest(TestCase):
    def setUp(self):
        tag1, tag2 = Tag(name="Tag 1"), Tag(name="Tag 2")
        post1, post2 = Post(title = "Post One"), Post(title = "Post Two")
        post1.save()
        post2.save()
        tag1.save()
        tag2.save()
        post1.tags.add(tag1)
        post2.tags.add(tag1, tag2)


    def test_getTagsWithQuantity_returns_correct_numbers(self):
        resultArray = Tag.getTagsWithQuantity()
        #Tag 1 occurs 2 times, Tag 2 occurs 1 times
        self.assertIn(("Tag 1", 2), resultArray)
        self.assertIn(("Tag 2", 1), resultArray)

    def test_getTagsWithQuantity_returns_number_occurrences_in_correct_order_descending(self):
        resultArray = Tag.getTagsWithQuantity()
        #tag 1 is most popular
        self.assertEqual(resultArray[0], ("Tag 1", 2))

    def test_getTagsWithQuantity_returns_number_occurrences_in_correct_order_ascending(self):
        resultArray = Tag.getTagsWithQuantity(reverse=False)
        #tag 2 is least popular
        self.assertEqual(resultArray[0], ("Tag 2", 1))


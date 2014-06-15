from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTests(TestCase):
    fixtures = [r'Blog\fixtures\Blog_testdata.json']

    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Ipsum', resp.content)

    def test_postPage(self):
        resp = self.client.get(reverse('postPage', args=[1]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Space Ipsum', resp.content)

    def test_postByTag(self):
        resp = self.client.get(reverse('postByTag', args=['TunaIpsum']))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Tuna Ipsum', resp.content)
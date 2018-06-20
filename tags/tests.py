from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Tag


class TagModelTests(TestCase):
    def test_empty_term(self):
        tag = Tag(term="", tags='')
        with self.assertRaises(ValidationError):
            tag.full_clean()

    def test_empty_tags(self):
        tag = Tag(term="sddfd", tags='')
        self.assertIsNone(tag.full_clean())

    def test_valid_tags(self):
        tag = Tag(term="sddfd", tags='sdfsdf, sdfsdf, sdgt ,rrg')
        self.assertIsNone(tag.full_clean())

    def test_invalid_tags(self):
        tag = Tag(term="sddfd", tags='sdfsdf sdfsdf sdgt ,rrg')
        with self.assertRaisesMessage(ValidationError, '"sdfsdf sdfsdf sdgt" is not a valid tag'):
            self.assertIsNone(tag.full_clean())


from django.urls import reverse
from django.test import Client

class TagViewsTests(TestCase):
    def test_root(self):
        c = Client()
        response = c.get(reverse('tags:root'))
        self.assertEqual(response.status_code, 200)

    def test_add_tag(self):
        c = Client()
        response = c.get(reverse('tags:add'))
        self.assertEqual(response.status_code, 200)

    def test_add_tag_submit(self):
        c = Client()
        response = c.post(reverse('tags:add'), {'term': 'dfdfdf', 'tags': 'sdfsd, sdfdsf'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_tag(self):
        c = Client()
        c.post(reverse('tags:add'), {'term': 'dfdfdf', 'tags': 'sdfsd'}, follow=True)
        response = c.get(reverse('tags:delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_delete_tag_submit(self):
        c = Client()
        c.post(reverse('tags:add'), {'term': 'dfdfdf', 'tags': 'sdfsd'}, follow=True)
        response = c.post(reverse('tags:delete', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)

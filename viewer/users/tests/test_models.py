from test_plus.test import TestCase


class TestUser(TestCase):

    def setUp(self):
        user = self.make_user()
        user.first_name = 'first_name'
        user.last_name = 'last_name'
        self.user = user

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            "testuser"  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_get_short_name(self):
        self.assertEqual(
            self.user.get_short_name(),
            'last_name'
        )

    def test_get_full_name(self):
        self.assertEqual(
            self.user.get_full_name(),
            'first_name last_name'
        )

from test_plus.test import TestCase
from ..models import UploadedFile


class TestUploadedFile(TestCase):

    def test_str(self):
        uploaded_file = UploadedFile(file_name='test_file')
        self.assertEqual('test_file', uploaded_file.__str__())

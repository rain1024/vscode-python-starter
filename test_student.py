import unittest

from student import Student

class TestStudent(unittest.TestCase):
    def test_display(self):
        student = Student("John", 16)
        self.assertEqual(student.display(), "John is 16 years old")
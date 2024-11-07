import unittest
 
class OnlineCourse():
    def __init__(self, length_in_hours):
        self.length_in_hours = length_in_hours
 
class TestQuizQuestion(unittest.TestCase):
    def setUp(self):
        self.python_course = OnlineCourse(length_in_hours = 50)
 
    def test_arithmetic(self):
        self.assertEqual(python_course.length_in_hours, 50)
      
if __name__ == "__main__":
    unittest.main()
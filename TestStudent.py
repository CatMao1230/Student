import Student
import unittest

class TestStudent(unittest.TestCase):
	def test_get_name(self):
		s = Student.student("Celine", 20)
		self.assertEqual(s.get_name(), "Celine")
	def test_get_name_without_value(self):
		s = Student.student()
		self.assertEqual(s.get_name(), "NoName")
	def test_get_z_count_1(self):
		s1 = Student.student("Celine", 20)
		self.assertEqual(Student.student.get_count(), 1)
	def test_get_z_count_2(self):
		s2 = Student.student("Rita", 20)
		self.assertEqual(Student.student.get_count(), 2)

if __name__ == '__main__':
	tests = unittest.TestLoader().loadTestsFromTestCase(TestStudent)
	unittest.TextTestRunner(verbosity = 2).run(tests)

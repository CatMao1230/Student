class student:

	count = 0

	def __init__(self, name = "NoName", age = 0):
		self.name = name
		self.age = age
		student.count += 1

	def get_name(self):
		return self.name

	@staticmethod
	def get_count():
		return student.count
		

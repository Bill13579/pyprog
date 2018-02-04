import sys

class ProgressIndicatorFraction:

	def __init__(self, prefix, suffix, total, initial=0):
		self.p = prefix
		self.s = suffix
		self.length = total
		self.current_stat = initial

	def __print(self, data, end="\n"):
		sys.stdout.write(data + end)

	def set_prefix(self, prefix):
		'''
		Set the prefix.
		'''
		self.p = prefix

	def set_suffix(self, suffix):
		'''
		Set the suffix.
		'''
		self.s = suffix

	def set_total(self, total):
		'''
		Set the total.
		'''
		self.length = total

	def set_stat(self, current):
		'''
		Set the current progress. Only accept integers.
		'''
		self.current_stat = current

	def update(self):
		'''
		Update the progress indicator so that it shows the current progress.
		Note: Also call this to initiate the indicator.
		'''
		final = str(self.current_stat) + "/" + str(self.length)
		final = self.p + final + self.s
		self.__print(final, end="\r")

	def end(self):
		'''
		End the progress indicator.
		'''
		self.__print("", end="\n")

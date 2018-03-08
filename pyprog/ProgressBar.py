import sys
import math

class ProgressBar:

	PROGRESS_LOC_START = 0
	PROGRESS_LOC_MIDDLE = 1
	PROGRESS_LOC_END = 2
	PROGRESS_LOC_EXP_START_PROGRESS_MID = 3
	PROGRESS_LOC_EXP_END_PROGRESS_MID = 4

	def __init__(self, prefix, suffix, total=100, bar_length=50, initial=0, decimals=0, complete_symbol="#", not_complete_symbol="-", progress_loc=0, progress_format="+p%", progress_explain="Progress: ", wrap_bar_prefix=" ", wrap_bar_suffix=" "):
		self.__end_m = False
		self.p = prefix
		self.s = suffix
		self.length = bar_length
		self.complete_sym = complete_symbol
		self.not_complete_sym = not_complete_symbol
		self.current_stat = initial
		self.total = total
		self.decimals = decimals
		self.progress_loc = progress_loc
		self.progress_format = progress_format
		self.progress_explain = progress_explain
		self.wrap_bar_prefix = wrap_bar_prefix
		self.wrap_bar_suffix = wrap_bar_suffix

	def __print(self, data, start="", end=""):
		sys.stdout.write(start + data + end)
		sys.stdout.flush()

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
		self.total = total

	def set_bar_length(self, bar_length):
		'''
		Set the bar length.
		'''
		self.length = bar_length

	def set_decimals(self, decimals):
		'''
		Set the decimal.
		'''
		self.decimals = decimals

	def set_symbols(self, symbols):
		'''
		Set the symbol for completed and not complete.
		'''
		self.complete_sym = symbols[0]
		self.not_complete_sym = symbols[1]

	def set_progress_loc(self, progress_loc):
		'''
		Set where progress text should be displayed.
		Values:
			PROGRESS_LOC_START -> At the start
			PROGRESS_LOC_MIDDLE -> In the middle of the bar
			PROGRESS_LOC_END -> At the end
			PROGRESS_LOC_EXP_START_PROGRESS_MID -> Show prefix at the start and progress text in the middle of the bar
			PROGRESS_LOC_EXP_END_PROGRESS_MID -> Show prefix at the end and progress text in the middle of the bar
		'''
		self.progress_loc = progress_loc

	def set_progress_explain(self, progress_explain):
		'''
		Set the progress explanation.
		Examples:
			"Progress: "
			"Current Progress: "
		'''
		self.progress_explain = progress_explain

	def set_wrap_bar_text(self, prefix, suffix):
		'''
		Set wrap bar text.
		Wrap bar text will wrap the bar.
		<prefix>bar<suffix>
		'''
		self.wrap_bar_prefix = prefix
		self.wrap_bar_suffix = suffix

	def set_progress_format(self, progress_format):
		'''
		Set progress format.
		Special Characters (include these in the format to display it):
			"+p" -> The current percentage
			"+c" -> The current stat
		'''
		self.progress_format = progress_format

	def set_stat(self, current):
		'''
		Set the current progress.
		'''
		self.current_stat = current

	def stat(self, current):
		'''
		Set the current progress and showing the progress bar.
		'''
		self.current_stat = current
		self.update()

	def progress(self, progress=1):
		'''
		Progress forward by an amount.
		'''
		self.current_stat += progress
		self.update()

	def update(self):
		'''
		Update the progress bar so that it shows the current progress.
		Note: Also call this to initiate the bar.
		'''
		decimal = float(self.current_stat) / float(self.total)
		blocks_to_fill = int(decimal * self.length)
		blocks_not_to_fill = self.length - blocks_to_fill
		final = self.complete_sym * blocks_to_fill + self.not_complete_sym * blocks_not_to_fill
		final = self.wrap_bar_prefix + final + self.wrap_bar_suffix
		percent = round(round(decimal, self.decimals + 2) * 100, self.decimals + 2)
		if self.__end_m:
			progress_str = ""
			self.progress_explain = self.__end_m
		else:
			if percent.is_integer():
				progress_str = self.progress_format.replace("+p", str(int(percent)))
			else:
				progress_str = self.progress_format.replace("+p", str(percent))
			progress_str = progress_str.replace("+c", str(self.current_stat))
		if self.progress_loc == ProgressBar.PROGRESS_LOC_START:
			final = self.progress_explain + progress_str + final
		elif self.progress_loc == ProgressBar.PROGRESS_LOC_MIDDLE:
			percent_explain_percent_str = " " + self.progress_explain + progress_str + " "
			bar_length_half = int(self.length / 2)
			bar_length_other_half = self.length - bar_length_half
			percent_str_half = int(len(percent_explain_percent_str) / 2)
			percent_str_other_half = len(percent_explain_percent_str) - percent_str_half
			bar_cut_from = bar_length_half - percent_str_half - 1
			bar_cut_to = bar_length_other_half + percent_str_other_half
			final = final[:bar_cut_from] + percent_explain_percent_str + final[bar_cut_to:]
		elif self.progress_loc == ProgressBar.PROGRESS_LOC_END:
			final += self.progress_explain + progress_str
		elif self.progress_loc == ProgressBar.PROGRESS_LOC_EXP_START_PROGRESS_MID:
			progress_str = " " + progress_str + " "
			bar_length_half = int(self.length / 2)
			bar_length_other_half = self.length - bar_length_half
			percent_str_half = int(len(progress_str) / 2)
			percent_str_other_half = len(progress_str) - percent_str_half
			bar_cut_from = bar_length_half - percent_str_half - 1
			bar_cut_to = bar_length_other_half + percent_str_other_half
			final = final[:bar_cut_from] + progress_str + final[bar_cut_to:]
			final = self.progress_explain + final
		elif self.progress_loc == ProgressBar.PROGRESS_LOC_EXP_END_PROGRESS_MID:
			progress_str = " " + progress_str + " "
			bar_length_half = int(self.length / 2)
			bar_length_other_half = self.length - bar_length_half
			percent_str_half = int(len(progress_str) / 2)
			percent_str_other_half = len(progress_str) - percent_str_half
			bar_cut_from = bar_length_half - percent_str_half - 1
			bar_cut_to = bar_length_other_half + percent_str_other_half
			final = final[:bar_cut_from] + progress_str + final[bar_cut_to:]
			final = final + self.progress_explain
		final = self.p + final + self.s
		self.__print(final, start="\r")

	def end_m(self, msg):
		'''
		End the progress bar with a message.
		'''
		self.__end_m = msg
		self.update()
		self.end()

	def end(self):
		'''
		End the progress bar.
		'''
		self.__print("", end="\n")

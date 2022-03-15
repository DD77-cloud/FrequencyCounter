import re
from settings import SAVE_LOGS
from TestSuite import testsettings
from log_processor import logger
import os

def count_words(filepath, is_test=False):
	"""Counts word frequency in a text file.
	Leaves words separated by apostrophes in tact.(i.e. they'll, didn't)
	Expected input: filepath(string)
	is_test: boolean.
	is_test loads up settings specific to running a test(i.e. whether to log the result.
	Output: a frequency dictionary in the format {string: int}.
	"""
	result_dict = {}
	errors = []


	save_logs = SAVE_LOGS
	if is_test:
		save_logs = testsettings.SAVE_LOGS

	text_file = open(os.path.abspath(filepath), "r", errors="replace")
	lines = text_file.readlines()
	decoding_errors = 0
	for i, line in enumerate(lines):
		split_line = []
		if not line.isascii():
			temp_split_line = line.split(" ")
			for word in temp_split_line:
				if u'\ufffd' in word:
					decoding_errors += 1
				elif not word.isascii():
					error = f"Non ascii input on line {i}: {word}"
					errors.append(error)
				else:
					word = re.split('[^a-zA-Z\']+', word)
					split_line+=word
		else:
			split_line = re.split('[^a-zA-Z\']+', line)
		for word in split_line:
			# ignores any empty splits
			# another option is to use this with minlength variable here so that the words that don't match the
			# but i thought it's best to collect maximum amount of data and then limit it upon recall.
			#same applies to stop_words
			if len(word) < 1:
				continue
			if word == "'":
				continue
			if(word[0] == word[0].upper()):  # prevents us from running lower() unnecessarily
				word = word.lower()
			if word in result_dict:
				result_dict[word] += 1
			else:
				result_dict[word] = 1
	if save_logs:
		file_name = "".join(re.split(r'/|\\', filepath)[-1].split('.')[0:-1])
		if decoding_errors>0:
			logger(f'{decoding_errors} have occurred while decoding file "{file_name}"', file_name)
		if len(errors)>0:
			for error in errors:
				logger(error, file_name)
	text_file.close()
	return result_dict
	

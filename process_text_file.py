from log_processor import logger
from count_words import count_words
from settings import (SAVE_LOGS, RAISE_EXCEPTIONS, PRINT_EXCEPTIONS, STOP_WORDS)
import re
import json
import os
from TestSuite import testsettings

def process_text_file(arg_array, source=""):
	"""Runs count_words on a text file to establish the entire text corpus.
	If requested saves the results to a json file.
	If requested prints out X most popular words into CLI.
	Expected input:
	required arg1: an array of:
	file_path(str), how_many_words_to_display(int), save_results(boolean), minimum_length_of_legit_word(int)
	optional arg2: source(str) determines if the call came from user menu or cl args.
	Output: none
	Created Files: Error log(optional), results_dictionary.json(optional)
	"""
	print(source)
	file_path = arg_array[0]
	words_to_display = arg_array[1]
	save_results = arg_array[2]
	min_length = arg_array[3]
	result_dict = count_words(arg_array[0])
	if words_to_display == -1:
		words_to_display = len(result_dict.keys())
	display_results = True
	if words_to_display == 0:
		display_results = False
	file_name = "".join(re.split(r'/|\\', file_path)[-1].split('.')[0:-1])
	if save_results:
		i = 0
		ending = "processed.json"
		while os.path.exists("."+os.sep+"Output"+os.sep+file_name+ending):
			ending = f"processed({str(i)}).json"
			i += 1
		with open("."+os.sep+"Output"+os.sep+file_name+ending, "w") as outfile:
			json.dump(result_dict, outfile)
	if display_results or source=="user_menu":
		results = process_results(result_dict, words_to_display, min_length)
		title_print = f"\nTop {words_to_display} most popular words in {file_name}.txt: "
		print("-"*len(title_print))
		print(title_print)
		print("-"*len(title_print))
		print("\n{:20s} {:10s}\n".format("Word", "Occurrences"))
		for entry in results:
			print("{:20s} {:10d}".format(entry[0], entry[1]))
		print("-"*len(title_print))





def process_results(dict, words_to_display, min_length, istest = False):
	"""Sorts the results of count_words by frequency
	Expected input:
	results_dict = {"string":int}(req)
	words_to_display(int)(req)
	min_length(int)(req)
	Output:
	array of arrays [[word(str), freq(int)]]
	"""
	output = []
	sorted_keys = sorted(dict, key = lambda k: (-dict[k], k))
	stop_words = STOP_WORDS
	if istest:
		stop_words = testsettings.STOP_WORDS
	for word in sorted_keys:
		if len(output)==words_to_display:
			break
		elif word in stop_words:
			continue
		elif len(word)<min_length:
			continue
		else:
			output.append([word, dict[word]])
	return output








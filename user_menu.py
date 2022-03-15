import os.path
from os import path

def menu():
	"""Generates menu for text-based CLI"""
	#while the input checks repeat here and in verify_inputs, i feel that it aids in code readability.
	filename = ""
	file_exists = False
	file_format_correct = False
	while (not file_format_correct) or (not file_exists):
		if not file_format_correct:
			filename = input("\nPlease input file name to process: ")
		elif not file_exists:
			print("\nFile not found.")
			filename = input("\nPlease input file name to process: ")
		file_format_correct = filename.split('.')[-1]=="txt"
		file_exists = path.exists(filename)
	count = "X"
	while not count.isdigit() and not count == "-1":
		count = input("\nReturn count for ? most popular words: (-1 for the entire corpus) ")
		if not count.isdigit() and not count == "-1": #checks the input for both decimals and numbers less than 0
			print("\nIncorrect input. Please input a valid number")
	
	save_results = "test"
	yes = ["Y", "y", "yes", "YES", "Yes"] 
	no = ["N", "n", "no", "NO", "No"]
	#it's a discussion of whether these inputs should be more precise to minimize the possibility of a  wrong input
	#or should be more user friendly and accept all possible combinations
	while not(save_results in yes) and not(save_results in no): 
		save_results = input("\nWould you like to save the results in a json file: y/n ")
	if save_results in no:
		save_results = False
	else:
		save_results = True
	return [filename, count, save_results]
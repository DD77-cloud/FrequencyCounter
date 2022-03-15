import sys
import re
import user_menu
from log_processor import logger
from verify_inputs import verify_inputs
from settings import USER_MENU_ENABLED, SAVE_LOGS, RAISE_EXCEPTIONS, PRINT_EXCEPTIONS
from process_text_file import process_text_file

## Example query:
## python main.py TextFiles/6.txt 10 y 5

def main(argv):
	"""
	Can accept command line arguments in the format of:
	file path(required), top words to display(number), save results to json file(y/n), minimum length of valid word
	If no command line arguments are passed and the USER_MENU_ENABLED flag is set to true there is also a command line
	user menu.
	Output: none
	Files generated(optional): error log file, processed text file.
	"""

	command_line_expectation = """
	Please input CLI arguments in the following format:
	filepath(required) i.e. Folder/file.txt, #of_words_to_display(optional), save_results?accepted: y/n(optional)
	"""

	if len(argv) == 1 and USER_MENU_ENABLED:
		arg_array = user_menu.menu()
		inputs = verify_inputs(arg_array)
		process_text_file(inputs, "user_menu")
	elif len(argv) == 1:
		print(command_line_expectation)
	else:
		try:
			inputs = verify_inputs(argv[1:])
			process_text_file(inputs)
		except Exception as e:
			print(command_line_expectation)
			if SAVE_LOGS:
				logger(e)
			if PRINT_EXCEPTIONS:
				print(e)
			if RAISE_EXCEPTIONS:
				raise(e)

if __name__ == "__main__":
	main(sys.argv)


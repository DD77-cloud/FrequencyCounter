import sys
from TestSuite.count_words_tests.count_words_test import count_words_test
from TestSuite.process_text_file_tests.process_text_file_tests import process_text_file_test, process_results_test
from count_words import count_words
from process_text_file import process_results, process_text_file

#For now there is only one menu, but there could potentially be more
#For example unit tests vs integration tests

#There is a consideration here as to whether or not to run the "parent" component through the same tests as the
#"child" packages. In the interest of time I am making here an assumption that other tests, dedicated to those packages,
#"prove" that those packages are functional. Hence I am only going to be testing functionality unique to a specific pkg.
#My personal preference would be to duplicate all the tests, at least those from count_words into main as an integration
#test.

#one of the changes that I would implement here in the future is
#a count of all failed tests for easier readability.


#all functions have an input variable which tells them whether a test is running.
#that is so i never have to overwrite user defined "settings.py" file, thus minimizing the risk
#of ever losing those settings for the user.

dict_of_menu_options = {
    "mainMenu":"""
    1. Run all tests.
    2. Test count_words.py
    3. Test process_text_file.py
    
    0. Exit
    """
}

def main_menu():
    """Draws a user menu for tests.
    Triggers tests based on user input
    Accepted input: none
    Output: none"""
    if len(sys.argv) > 1:
        execute_tests(int(sys.argv[1]))
    else:
        while True:
            print(dict_of_menu_options["mainMenu"])
            selection = int(input("Please enter your selection: "))
            execute_tests(selection)

def execute_tests(intIn):
    """Triggers appropriate test package based on user input.
    Expected input: user selection(int)(req)
    Output: none"""
    if intIn == 0:
        exit(1)
    elif intIn == 1:
        count_words_test(count_words)
        process_results_test(process_results)
        process_text_file_test(process_text_file)
    elif intIn == 2:
        count_words_test(count_words)
    elif intIn == 3:
        process_results_test(process_results)
        process_text_file_test(process_text_file)



main_menu()
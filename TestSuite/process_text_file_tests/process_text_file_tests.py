import json
import os

def process_results_test(process_results):
    print("\n\t>>>>> Running process_results tests <<<<<\n")
    """Unit tests for process_results function.
    Process_results accepts results dictionary, amount of words to display and min lenght of valid words.
    It also read the list of stop_words from settings.py(or in case of test, testsettings.py)
    """
    with open("TestSuite/process_text_file_tests/settings.py", "r") as infile:
        test_settings = infile.read()
        with open("TestSuite/testsettings.py", "w") as outfile:
            outfile.write(test_settings)

    PR_basic_tests(process_results)
    #commented out because the file might be too large to share
    #PR_huge_file(process_results)
    print("\n\t>>>>> Finished running process_results tests <<<<<\n")


def process_text_file_test(process_text_file):
    """Unit tests for process_text_file function."""
    print("\n\t>>>>> Running process_text_file tests <<<<<\n")
    # Process_text_file uses count_words and process_results functions.
    # Expected input:
    # required arg1: an array of:
    #   required: file_path(str)
    #   optional: how_many_words_to_display(int), save_results(boolean), minimum_length_of_legit_word(int)
    # optional arg2: source(str) determines if the call came from user menu or cl args.
    # Output: none
    # Created Files: Error log(optional), results_dictionary.json(optional)
    PT_basic_test(process_text_file)
    print("\n\t>>>>> Finished running process_text_file tests <<<<<\n")


def PT_basic_test(process_text_file):
    """Runs basic tests on process_text_file function."""

    print("\n>> Testing file saving")
    process_text_file(["./TestSuite/test_files/process_text_files/small.txt", 0, True, 1])
    with open("./Output/smallprocessed.json", "r") as processed_file:
        results = json.load(processed_file)
        expected = [['challenge',1],['charm',1],['creatine',1],  ['finale',1], ['potato',1],['small',1]]
    exception_list = []
    try:
        assert len(expected)==len(results), f"\texpected saved file to be: {expected}\n\tgot:{results}\n"
    except Exception as e:
        exception_list.append(str(e))
    try:
        for item in expected:
            assert item[0] in results, f"\tWord '{item[0]}' missing from saved file."
            assert item[1]==results[item[0]], f"\tOn word '{item[0]}':\n\t expected count: {item[1]}\n\t got:{results[item[0]]}"
    except Exception as e:
        exception_list.append(str(e))
    if len(exception_list):
        print("\n" + "\n".join(exception_list) + "\n")
    if len(exception_list) == 0:
        print(">> Testing successful\n")
    else:
        print(">> Testing failed\n")

    print("\n>> Testing saves files with the same name by adding (i) at the end.")

    process_text_file(["./TestSuite/test_files/process_text_files/small.txt", 0, True, 1])
    dir = os.listdir("./Output")

    exception_list = []
    try:
        assert "smallprocessed.json" in dir, f"Expected smallprocessed.json file to be in output directory.\n Instead got: {dir}"
        assert "smallprocessed(0).json" in dir, f"Expected smallprocessed.json file to be in output directory.\n Instead got: {dir}"
    except Exception as e:
        print(e)
        exception_list.append(e)
    if len(exception_list) == 0:
        print(">> Testing successful\n")
    else:
        print("\n" + "\n".join(exception_list) + "\n")
        print(">> Testing failed\n")




def PR_basic_tests(process_results):
    """Runs basic tests on process_results function."""

    result_dict = {"beauty": 15, "mike": 1, "butterfly": 3, "amaze": 4,
                   "test": 1, "paper": 3, "nomenclature": 1, "tribulations": 14,
                   "on": 2, "of": 1, "madman": 3
                   }
    expected = [["beauty", 15], ["tribulations", 14], ["amaze", 4], ["butterfly", 3],
                ["madman", 3], ["paper", 3],["on", 2], ["mike", 1], ["nomenclature", 1],
                ["of", 1], ["test", 1]]

    print("\n>> Testing sorting short dictionary")
    result = process_results(result_dict, len(expected), 1)
    PR_basic_asserter(result, expected)

    print("\n>> Testing for failure. Expect 2 error messages.")
    result = process_results(result_dict, len(expected), 1)
    PR_basic_asserter(result[0:(len(result) - 2)], expected, 2)

    print("\n>> Testing setting min_length")
    modified_expected = list(filter(lambda x: len(x[0])>=4, expected))
    result = process_results(result_dict, len(modified_expected), 4)
    PR_basic_asserter(result, modified_expected)

    print("\n>> Testing setting words_to_display")
    result = process_results(result_dict, 5, 1)
    PR_basic_asserter(result, expected[0:5])

    print("\n>> Testing setting all 3 inputs")
    modified_expected = list(filter(lambda x: len(x[0])>=5, expected))
    result = process_results(result_dict, 5, 5)
    PR_basic_asserter(result, modified_expected[0:5])

    expected = [["beauty", 15], ["tribulations", 14], ["amaze", 4], ["butterfly", 3],
                ["madman", 3], ["paper", 3], ["mike", 1], ["nomenclature", 1],
                 ["test", 1]]

    print("\n>> Testing using stop words")
    result = process_results(result_dict, 11, 1, True)
    PR_basic_asserter(result, expected)


def PR_basic_asserter(results, expected, accepted_failure = 0):
    """Runs assertions for basic_tests. Compares them to expected values. Stores exceptions in a list to prevent tests from exiting early."""
    exception_list = []
    try:
        assert len(expected)==len(results), f"\texpected results: {expected}\n\tgot:{results}\n"
    except Exception as e:
        exception_list.append(str(e))
    try:
        for i in range(0, len(expected)):
            assert i<len(results), f"\tWord '{expected[i][0]}' missing from results."
            assert expected[i][0]==results[i][0], f"\texpected '{expected[i][0]}',\n\t got:'{results[i][0]}'"
            assert expected[i][1]==results[i][1], f"\tOn word '{expected[i][0]}':\n\t expected count: {expected[i][1]}\n\t got:{results[i][0]}"
    except Exception as e:
        exception_list.append(str(e))
    if len(exception_list):
        print("\n"+"\n".join(exception_list)+"\n")
    if len(exception_list) == accepted_failure:
        print(">> Testing successful\n")
    else:
        print(">> Testing failed\n")


def PR_huge_file(process_results):
    """Tests process_results against a huge dictionary(over 200k words)"""
    print("\n>> Testing process_results against a very large file(over 200k words)")
    print(">>\t Expected behavior: to not throw any errors")
    print(">>\t Expected behavior: to return most popular word")
    with open("./TestSuite/test_files/process_text_files/en_USnewsprocessed.json", "r") as infile:
        data = json.load(infile)
        expected = [["the", 1969820]]
        result = process_results(data, 1, 1)
        PR_basic_asserter(result, expected)


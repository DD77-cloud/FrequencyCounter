

def count_words_test(count_words):
    print("\n\t>>>>> Running count_words tests <<<<<\n")
    """Unit tests for count_words function"""
    with open("TestSuite/count_words_tests/settings.py", "r") as infile:
        test_settings = infile.read()
        with open("TestSuite/testsettings.py", "w") as outfile:
            outfile.write(test_settings)
    basic_tests(count_words)

    #the following test is commented out because I did not want to take the liberty of including a huge file into
    #a package that other people will download
    #huge_file_test(count_words)

    #the following test is commented out because it expects files located outside of the package
    #which is also something that is an issue when sharing the package between different computers.
    #different_paths_test(count_words)

    #it is also a problem to verify if the tests will work on large files because you would need the control over the
    #word count. There needs to be a test that would have the functionality to generate random text files that would
    #keep track of all the words in the corpus at the time of generation.
    #I ran out of time before i could implement it

    various_languages_test(count_words)

    test_filenames(count_words)

    incorrect_encoding_test(count_words)

    print("\n\t>>>>> Finished running count_words tests <<<<<\n")


def basic_tests(count_words):

    """Runs the count_words program against a selection of hand written tests that have known
    word quantities"""


    print("\n>> Testing short, non repeating text with no punctuation.")
    expected = [["small", 1], ["charm", 1], ["challenge", 1], ["potato",1], ["finale",1], ["creatine",1]]
    results = count_words("./TestSuite/test_files/count_words/small.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing failures. Expect 3 error messages")
    expected = [["small", 1], ["challenge", 1], ["potato",4], ["finale",1], ["creatine",2]]
    basic_tests_asserter(expected, results, 3)

    print("\n>> Testing short, repeating text with no punctuation.")
    expected = [["small", 2], ["charm", 3], ["challenge", 2], ["potato",1], ["finale",4], ["creatine",3]]
    results = count_words("./TestSuite/test_files/count_words/small_repeating.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing short, repeating text with punctuation.")
    expected = [["small", 2], ["charm", 3], ["challenge", 2], ["potato",1], ["finale",4], ["creatine",3]]
    results = count_words("./TestSuite/test_files/count_words/small_repeating_punctuation.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing empty file.")
    expected = []
    results = count_words("./TestSuite/test_files/count_words/empty.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing short, repeating text with punctuation and capitalization.")
    print(">>\t Expected behavior: everything gets converted to lower case.")
    expected = [["small", 2], ["charm", 3], ["challenge", 2], ["potato", 1], ["finale", 4], ["creatine", 3]]
    results = count_words("./TestSuite/test_files/count_words/small_repeating_punctuation_mixedcases.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing short, repeating text with punctuation, capitalization and apostrophes.")
    print(">>\t Expected behavior: words don't get split on apostrophes.")
    expected = [["small", 2], ["charm", 3], ["challenge", 2], ["potato", 1], ["finale", 4], ["creatine", 3], ["they'll", 1]]
    results = count_words("./TestSuite/test_files/count_words/small_repeating_punctuation_mixedcases_apostrophes.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing short, repeating text that is all caps.")
    print(">> \tExpected behavior: everything gets converted to lower case.")
    expected = [["potato", 1], ["bananas", 2], ["banana", 1], ["potatoes", 1], ["amazing", 1], ["deal", 1], ["on", 1], ["and", 1], ["eat", 1], ["many", 1]]
    results = count_words("./TestSuite/test_files/count_words/small_allcaps.txt", True)
    basic_tests_asserter(expected, results)

    print("\n>> Testing multi line text.")
    expected = [["small", 6], ["charm", 9], ["challenge", 6], ["potato", 3], ["finale", 12], ["creatine", 9], ["they'll", 3]]
    results = count_words("./TestSuite/test_files/count_words/small_multiline.txt", True)
    basic_tests_asserter(expected, results)

def basic_tests_asserter(expected, results, accepted_failure = 0):
    """Runs assertions for basic_tests. Compares them to expected values. Stores exceptions in a list to prevent tests from exiting early."""
    exception_list = []
    try:
        assert len(expected)== len(results.keys()), f"\texpected keys: {sorted(expected)}\n\tgot keys:{sorted(results.keys())}\n"
    except Exception as e:
        exception_list.append(str(e))
    for key in expected:
        try:
            assert(key[0] in results), f"\tword from text('{key[0]}') is missing in result"
            assert(results[key[0]]==key[1]), f"\tword count in results doesnt match original for word '{key[0]}' expected: {key[1]} got: {results[key[0]]}"
        except Exception as e:
            exception_list.append(str(e))
    if len(exception_list):
        print("\n"+"\n".join(exception_list)+"\n")
    if len(exception_list) == accepted_failure:
        print(">> Testing successful\n")
    else:
        print(">> Testing failed\n")

def huge_file_test(count_words):
    """Attempts to execute count_words function on a huge file(over 200 million symbols)"""
    print("\n>> Testing processing huge file.")
    print(">>\t Expected behavior: to not throw any errors")
    raised=False
    try:
        results = count_words("C:\en_US.news.txt", True)
        print(results)
    except Exception as e:
        raised = True
        print(e)
    if raised:
        print(">> Test Failed")
    else:
        print(">> Testing Successful")


def different_paths_test(count_words):
    #leaving this empty because technically this is already tested in the huge_file_test
    pass

def incorrect_encoding_test(count_words):
    """Attempts to execute count_words on a file that contains encoding not understood by python's open"""
    print("\n>> Testing processing file that includes non-ascii letters.")
    print(">>\t Expected behavior: to not throw any errors")
    print(">>\t Expected behavior: to ignore words(not lines) that include undecipherable characters.")
    expected = ["lamb", "lies", "the", "down", "on", "genesis"]
    raised = False
    try:
        result = count_words("./TestSuite/test_files/count_words/incorrect_encoding.txt")
        for key in expected:
            assert key in result, f"Word {key} missing from results. Word shared a line with a non-decipherable character."
    except Exception as e:
        raised = True
        print(e)
    if raised:
        print(">> Test Failed")
    else:
        print(">> Testing Successful")


def various_languages_test(count_words):
    """Attempts to execute count_words function on a file that includes non-ascii characters.
    Expected behavior: skip. Optional: log as errors."""
    print("\n>> Testing processing file that includes non-ascii letters.")
    print(">>\t Expected behavior: to not throw any errors")
    print(">>\t Expected behavior: to ignore words(not lines) that include non-ascii characters.")
    raised = False
    try:
        result = count_words("./TestSuite/test_files/count_words/Polish.txt", True)
        expected = ["zawisza", "zdunowski"]
        for key in result.keys():
            assert key.isascii()==True, f"Non ascii word {key} found in results."
        for key in expected:
            assert key in result.keys(), f"Word {key} missing from results. Word shared a line with non-ascii word."
    except Exception as e:
        raised=True
        print(e)
    if raised:
        print(">> Test Failed")
    else:
        print(">> Testing Successful")

def test_filenames(count_words):
    #seems unnecessary as this seems to be testing open or path more than my code.
    filenames = ["test spaces.txt", "test(2).txt", "TESTCAPITAL.txt", "test#.txt"]
    directory = "./TestSuite/test_files/count_words/"
    raised = False
    print("\n>> Testing processing file names that include special characters.")
    for file in filenames:
        filepath = directory+file
        try:
            result = count_words(filepath, True)
            assert len(result.keys())>0, f"File '{file}' returned an empty result dictionary."
        except Exception as e:
            raised = True
            print(e)
    if raised:
        print(">> Test Failed")
    else:
        print(">> Testing Successful")





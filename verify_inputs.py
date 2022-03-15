from settings import DEFAULT_DISPLAY_X_MOST_POPULAR_WORDS, DEFAULT_SAVE_OUTPUT_BEHAVIOR, DEFAULT_MINIMUM_LENGTH_WORDS
from errors import InvalidFilePathError, CommandLineArgumentsMissingError, IncorrectFileFormatError
import os.path
#it could be possible to accept stop words as a command line input as well, but considering that 
#stop words usually are common and the inconvinience of passing large arrays as a command line
#argument i decided not to include that option

def verify_inputs(arg_array):
    print(arg_array)
    if (not arg_array) or (len(arg_array) == 0):
        raise CommandLineArgumentsMissingError

    words_to_display = DEFAULT_DISPLAY_X_MOST_POPULAR_WORDS
    save_results = DEFAULT_SAVE_OUTPUT_BEHAVIOR
    min_length = DEFAULT_MINIMUM_LENGTH_WORDS
    file_name = arg_array[0]
    if '.' not in file_name:
        raise IncorrectFileFormatError(file_name, 'none')
    elif file_name.split('.')[-1] != "txt":
        raise IncorrectFileFormatError(file_name, file_name.split('.')[-1])
    else: 
        file_exists = os.path.exists(file_name)
        if not file_exists:
            raise InvalidFilePathError(file_name)
    if len(arg_array) > 1:
        if arg_array[1].isdigit():
            words_to_display = int(arg_array[1])
    if len(arg_array) > 2:
        # because this function is used for batch processing we expect precise inputs.
        if arg_array[2] == "y" or arg_array[2] == "n":
            save_results = arg_array[2]
    if len(arg_array) > 3:
        if arg_array[3].isdigit():
            min_length = int(arg_array[3])
            if min_length == 0:
                min_length = 1
    output = [file_name, words_to_display, save_results, min_length]
    return output

#this is mostly for logging purposes.
#another option is for this to be strings but because we want to include crucial information
#such as which file the error has occured on or what we expect as a valid parameter
#I felt that a custom error setup would be suitable. 
#I also use this setup when testing my javascript files, i.e. instead of trying to remember
#what some specific error says i have a list of strings titled PRISMA_INVALID_VALUE or GRAPHQL_INVALID_VALUE, etc
#which are easy to remember and are self-documenting.
#and this setup will be useful for any potential expansion such as accepting pdf file formats
#so for any change to the functionality we only need to modify errors in one central file. 
#Personally i think snake case would be easier to read but pascal case seems to be the python standard for error handling


class IncorrectFileFormatError(Exception):
    """Raised when the user attempts to pass in a file of unapproved file format"""
    def __init__(self, filename, received_file_format):
        self.expected_format = ".txt"
        self.message = f'Incorrect file format on: Filename "{filename}". Expected {self.expected_format} received {received_file_format}'
        super().__init__(self.message)

class CommandLineArgumentsMissingError(Exception):
    """Raised when no command line arguments have been passed and the user menu is turned off"""
    pass


class InvalidFilePathError(Exception):
    """Raised when os.path cannot locate the passed in filepath"""
    def __init__(self, filename):
        self.message = f'os.path can not locate file at path: "{filename}"'
        super().__init__(self.message)

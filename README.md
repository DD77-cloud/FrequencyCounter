This is an application that parses text files and counts the word frequency.

Example trigger query:
    python main.py TextFiles/6.txt 10 y 5

Example test-trigger query:
    python TestSuite.py 1

It only accepts utf8-encoded ascii-compliant text.

It provides two ways to use it - as a script that accepts command line arguments for batch or pipeline processing and 
a user menu for parsing single files.

The file settings.py contains default settings for how the program operates.

Options include:
    Turning on/off the user menu.
    Default minimum length of words to include into the top frequency counts.
    A list of stop words to include into top frequency counts.
    Save output on/off.
    Raise exceptions: whether or not the program should raise terminal exceptions.
    Save logs: whether or not the program should save error logs.
    Print exceptions: wheter or not the program should print exceptions to the terminal(independent of raise exceptions)

Text processing rules:
    All non-ascii words are ignored.
    All words that contain encoding failure are ignored.
    All words are converted to lower case.
    All words are recorded in the grammatical number they are presented in text(cats and cat are counted as separate)
    All words with apostrophes recorded as they are ("They'll", "didn't")
    (i feel that to properly process contractions and plural/singular words i would've had to move into NLP territory
    of processing word context.)
    All outputs are saved regardless of min_length and stop_words values.
    (this was done because i thought that it's usefull to have maximum amount of data and then process it on readback.
    Of course it would be an easy modification to change that.)
    Output is saved in json format.
    Json output files do not get overwritten or appended. Saved with (i) counter at the end.
    Error logs are saved as tab separated .txt files. 

    


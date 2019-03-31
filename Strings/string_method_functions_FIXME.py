"""
Define functions for the following:
redact_after_count(string, int)->string
redact_after_symbol(string, char)-string
numeric_scraper(string)->list
"""

def redact_after_count(text :str, count:int) ->str:
    """Replaces all characters after a certain count with XXXXX"""

def redact_after_symbol(text:str, symbol:str) ->str:
    """Replaces all characters after a certain symbol appears with XXXXX"""

def numeric_scraper(text:str) -> list:
    """Returns a list of all numbers in a given string ex "a11b2c333" -> [11, 2, 333]"""
"""
Constants for examples
"""
NON_VAR = None
STRING_VAR = "This is a string"
LIST_VAR = STRING_VAR.split()
DICT_VAR = dict(zip(i := iter(LIST_VAR), i))

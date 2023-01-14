"""
from <rf_lib> import <class> as <xyz> example

python Examples/Importing/02__from_import.py
"""

import constants as C
from robot.libraries.BuiltIn import BuiltIn


def main():
    """
    'from import' is a good option
    """

    BuiltIn().log_to_console(BuiltIn().get_length(C.STRING_VAR))
    BuiltIn().log_to_console(BuiltIn().get_length(C.LIST_VAR))
    BuiltIn().log_to_console(BuiltIn().get_length(C.DICT_VAR))
    try:
        BuiltIn().log_to_console(
            BuiltIn().get_length(C.NON_VAR))
    except RuntimeError as error:
        BuiltIn().log_to_console(error)


if __name__ == "__main__":
    main()

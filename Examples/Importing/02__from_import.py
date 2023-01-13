"""
from <rf_lib> import <class> as <xyz> example

python Examples/Importing/02__from_import.py
"""

import constants as C
from robot.libraries.BuiltIn import BuiltIn as rf_builtin


def main():
    """
    from import probably the best option
    """

    rf_builtin().log_to_console(rf_builtin().get_length(C.STRING_VAR))
    rf_builtin().log_to_console(rf_builtin().get_length(C.LIST_VAR))
    rf_builtin().log_to_console(rf_builtin().get_length(C.DICT_VAR))
    try:
        rf_builtin().log_to_console(
            rf_builtin().get_length(C.NON_VAR)
        )
    except RuntimeError as error:
        rf_builtin().log_to_console(error)


if __name__ == "__main__":
    main()

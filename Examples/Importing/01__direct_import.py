"""
import <rf_lib> as <xyz> example

python Examples/Importing/01__direct_import.py
"""

import constants as C
import robot.libraries.BuiltIn as rf_builtin


def main():
    """
    direct import can be cumbersome
    """

    rf_builtin.BuiltIn().log_to_console(
        rf_builtin.BuiltIn().get_length(C.STRING_VAR)
    )
    rf_builtin.BuiltIn().log_to_console(
        rf_builtin.BuiltIn().get_length(C.LIST_VAR)
    )
    rf_builtin.BuiltIn().log_to_console(
        rf_builtin.BuiltIn().get_length(C.DICT_VAR)
    )
    try:
        rf_builtin.BuiltIn().log_to_console(
            rf_builtin.BuiltIn().get_length(C.NON_VAR)
        )
    except RuntimeError as error:
        rf_builtin.BuiltIn().log_to_console(error)


if __name__ == "__main__":
    main()

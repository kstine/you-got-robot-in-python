"""
import <rf_lib>

python Examples/Importing/00__direct_import.py
"""

import constants as C
import robot.libraries.BuiltIn


def main():
    """
    direct import can be cumbersome
    """
    robot.libraries.BuiltIn.BuiltIn().log_to_console(
        robot.libraries.BuiltIn.BuiltIn().get_length(C.STRING_VAR)
    )
    robot.libraries.BuiltIn.BuiltIn().log_to_console(
        robot.libraries.BuiltIn.BuiltIn().get_length(C.LIST_VAR)
    )
    robot.libraries.BuiltIn.BuiltIn().log_to_console(
        robot.libraries.BuiltIn.BuiltIn().get_length(C.DICT_VAR)
    )
    try:
        robot.libraries.BuiltIn.BuiltIn().log_to_console(
            robot.libraries.BuiltIn.BuiltIn().get_length(C.NON_VAR)
        )
    except RuntimeError as error:
        robot.libraries.BuiltIn.BuiltIn().log_to_console(error)


if __name__ == "__main__":
    main()

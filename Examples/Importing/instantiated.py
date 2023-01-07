"""
Inheriting a library

python Examples/Importing/instantiated.py
"""

import constants as C
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections as collecions


class UberBuiltIn():  # pylint: disable=too-many-ancestors
    """
    Inheriting a robot framework library not advised
    """

    def __init__(self):
        self.rf_builtin = BuiltIn()

    def main(self):
        """
        the main method
        """
        self.rf_builtin.log_to_console(
            self.rf_builtin.get_length(C.STRING_VAR)
        )
        self.rf_builtin.log_to_console(self.rf_builtin.get_length(C.LIST_VAR))
        self.rf_builtin.log_to_console(self.rf_builtin.get_length(C.DICT_VAR))
        try:
            self.rf_builtin.log_to_console(
                self.rf_builtin.get_length(C.NON_VAR)
            )
        except RuntimeError as error:
            self.rf_builtin.log_to_console(error)

    def other_main(self):
        """
        Some fun with collections
        """
        self.rf_builtin.log_to_console(
            collecions().get_from_dictionary(
                C.DICT_VAR,
                "gnomes",
                default="awesome!"
            )
        )


if __name__ == "__main__":
    uber_built = UberBuiltIn()
    uber_built.main()
    uber_built.other_main()

"""
Create an instance of a library to be used withn a class.

python Examples/Importing/03__instantiated.py
"""

import constants as C
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections


class ClassyBuiltIn():
    """
    Create an instance with __init__
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
            Collections().get_from_dictionary(
                C.DICT_VAR,
                "gnomes",
                default="awesome!"
            )
        )


if __name__ == "__main__":
    uber_built = ClassyBuiltIn()
    uber_built.main()
    uber_built.other_main()

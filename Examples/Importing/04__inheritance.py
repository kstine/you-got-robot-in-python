"""
Inheriting a library (firehose inheritance)

python Examples/Importing/04__inheritance.py
"""

import constants as C
from robot.libraries.BuiltIn import BuiltIn


class UberBuiltIn(BuiltIn):  # pylint: disable=too-many-ancestors
    """
    Inheriting a robot framework library not advised
    """

    def main(self):
        """
        the main method
        """
        self.log_to_console(self.get_length(C.STRING_VAR))
        self.log_to_console(self.get_length(C.LIST_VAR))
        self.log_to_console(self.get_length(C.DICT_VAR))
        try:
            self.log_to_console(self.get_length(C.NON_VAR))
        except RuntimeError as error:
            self.log_to_console(error)


if __name__ == "__main__":
    uber_built = UberBuiltIn()
    uber_built.main()

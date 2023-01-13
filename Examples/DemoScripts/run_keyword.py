"""
Some keywords need Robot Framework running

python Examples/DemoScripts/run_keyword.py
"""

from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


def main():
    """
    Will trigger this error:
    robot.libraries.BuiltIn.RobotNotRunningError: Cannot access execution context  # noqa
    """
    try:
        BuiltIn().run_keyword("Log To Console", "This will probably fail.")
    except RobotNotRunningError as error:
        print(error)


if __name__ == "__main__":
    main()

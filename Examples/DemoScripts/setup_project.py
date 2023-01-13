"""
Final demo
Show how Dialogs, Builtin, and OperatingSystem can be used
Further demonstrate some struvtures not directly supported by Robot Framework
such as Enums, Match/Case
"""
from enum import Enum
from typing import Tuple

from robot.libraries import Dialogs
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.OperatingSystem import OperatingSystem


class Sections(Enum):
    """
    Simple Enum to store some values.
    """

    COMMENTS = """*** Comments ***
Add comments here"""
    TEST_SETTINGS = """*** Settings ***
Documentation       Add documentation
...                 robot -d Results Test.robot

Suite Setup         Suite Setup Keywords
Suite Teardown      Suite Teardown Keywords
Test Setup          Test Setup Keywords
Test Teardown       Test Teardown Keywords"""
    RESOURCE_SETTINGS = """*** Settings ***
Documentation       Add documentation"""
    VARIABLES = """*** Variables ***
${VARIABLE}    a variable"""
    TEST_CASES = """*** Test Cases ***
Test Case
    [Documentation]    Test documentation
    Log    Pass"""
    TEST_KEYWORDS = """*** Keywords ***
Suite Setup Keywords
    Log    Pass

Suite Teardown Keywords
    Log    Pass

Test Setup Keywords
    Log    Pass

Test Teardown Keywords
    Log    Pass"""
    RESOURCE_KEYWORDS = """*** Keywords ***
Resource Keyword
    [Documentation]    Add documentation
    [Arguments]    ${argument}
    Log    Pass"""


class SetupProject():
    """
    Basic script for creating Robot Framework files
    """

    rf_builtin = BuiltIn()
    rf_os = OperatingSystem()
    dialogs = Dialogs
    options = ("Resource", "Test", "All", "Destroy Folders")
    _no_yes = ("no", "yes")

    def setup_things(self):
        """
        Method for choosing Robot Framework Files
        """
        try:
            file_selections = self.dialogs.get_selections_from_user(
                "Select the file(s) you would like to create:", *self.options)
        except RuntimeError as error:
            self.rf_builtin.log(error)
            self.dialogs.pause_execution(
                """No file type was selected.\nExiting script."""
            )
        if file_selections:
            for file_selection in file_selections:
                match file_selection:
                    case "Resource":
                        self.setup_resource()
                    case "Test":
                        self.setup_test()
                    case "All":
                        self.setup_all_the_tings()
                    case "Destroy Folders":
                        self.destroy_folders()
                    case _:
                        self.dialogs.pause_execution(
                            "No file type was selected.")
        else:
            self.dialogs.pause_execution("No file type was selected.")

    def setup_all_the_tings(self):
        """
        Run all available methods for setup.
        """
        self.dialogs.pause_execution("Create Test File")
        self.setup_test()
        self.dialogs.pause_execution("Create Test File")
        self.setup_resource()

    def setup_test(self):
        """
        Create a test file with a basic starter structure.
        """
        sections = [
            self._add_comments,
            self._add_test_settings,
            self._add_variables,
            self._add_test_cases,
            self._add_test_keywords
        ]
        content = self._build_file_body(sections)
        self._write_file(content, "Tests", "Test")

    def setup_resource(self):
        """
        Create a resource file with a basic starter structure.
        """
        sections = [
            self._add_comments,
            self._add_resource_settings,
            self._add_variables,
            self._add_resource_keywords
        ]
        content = self._build_file_body(sections)
        self._write_file(content, "Resources", "Resource", ".resource")

    def destroy_folders(self):
        """
        Removes folders.
        """
        self.dialogs.pause_execution("Time to remove folders.")
        self.rf_os.remove_directory("Resources", recursive=True)
        self.rf_os.remove_directory("Tests", recursive=True)

    def _write_file(self,
                    content: str,
                    default_folder: str = "",
                    default_name: str = "",
                    default_ext=".robot"):
        while True:
            file_path, overwrite_file = self._input_file_path(
                default_folder, default_name, default_ext)
            if file_path is None:
                break
            try:
                if overwrite_file == self._no_yes[0]:
                    self.rf_os.file_should_not_exist(file_path)
                self.rf_os.create_file(file_path, content)
                break
            except AssertionError as error:
                self.dialogs.pause_execution(error)

    def _input_file_path(self, default_folder: str,
                         default_name: str,
                         default_ext: str) -> Tuple:
        try:
            file_folder = self.dialogs.get_value_from_user(
                "Enter folder path:", f"{default_folder}")
            file_name = self.dialogs.get_value_from_user(
                "Enter file name:", f"{default_name}")
            overwrite_file = self.dialogs.get_selection_from_user(
                "Overwrite file?", *self._no_yes)
            return (self.rf_os.join_path(file_folder, file_name + default_ext),
                    overwrite_file
                    )
        except RuntimeError as error:
            self.dialogs.pause_execution(error)
            return (None, None)

    def _get_value_from_sections(self,
                                 section: Sections,
                                 is_section: str
                                 ) -> str:
        return section.value if is_section == self._no_yes[1] else None

    def _add_comments(self):
        try:
            is_section = self.dialogs.get_selection_from_user(
                "Add Comments Section?", *self._no_yes)
        except RuntimeError as error:
            self.rf_builtin.log(error)
            is_section = self._no_yes[0]
        return self._get_value_from_sections(Sections.COMMENTS, is_section)

    def _add_test_settings(self):
        return Sections.TEST_SETTINGS.value

    def _add_resource_settings(self):
        return Sections.RESOURCE_SETTINGS.value

    def _add_variables(self):
        try:
            is_section = self.dialogs.get_selection_from_user(
                "Add Variables Section?", *self._no_yes)
        except RuntimeError as error:
            self.rf_builtin.log(error)
            is_section = self._no_yes[0]
        return self._get_value_from_sections(Sections.VARIABLES, is_section)

    def _add_test_cases(self):
        return Sections.TEST_CASES.value

    def _add_test_keywords(self):
        return Sections.TEST_KEYWORDS.value

    def _add_resource_keywords(self):
        return Sections.RESOURCE_KEYWORDS.value

    def _build_file_body(self, sections: list) -> str:
        content = None
        for section in sections:
            section_content = section()
            if content and section_content is not None:
                content = self.rf_builtin.catenate(
                    "SEPARATOR=\n\n\n", content, section_content)
            elif section_content is not None:
                content = section_content
        return content + "\n"


if __name__ == "__main__":
    setup = SetupProject()
    setup.setup_things()

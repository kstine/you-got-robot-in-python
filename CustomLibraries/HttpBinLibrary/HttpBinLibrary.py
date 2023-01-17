# pylint:disable=invalid-name
"""
Requests Library for Http Bin service

python CustomLibraries/HttpBinLibrary/HttpBinLibrary.py
"""
from typing import Union

from RequestsLibrary import RequestsLibrary
from robot.api.deco import keyword, library, not_keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


@library(scope="GLOBAL", version="1.0", auto_keywords=True)
class HttpBinLibrary():
    """
    This is a library and a script.
    """

    rf_builtin = BuiltIn()

    def __init__(self,
                 host: str = "http://localhost:8086",
                 alias: str = "gnome_alias"):
        self.host = host
        self.rf_requests = self._get_requests_library_instance()
        self.alias = alias
        self.headers = {"accept": "application/json"}

    @keyword("Create HTTP Bin Session")
    def create_http_bin_session(self):
        """
        Create session with the http bin service.
        """
        self.rf_requests.create_session(self.alias,
                                        self.host,
                                        headers=self.headers,
                                        verify=False,
                                        disable_warnings=True)

    @keyword("Get HTTP Method")
    def get_http_method(self) -> any:
        """
        Gets the response from http bin service

        Returns:
            any: response
        """
        response = self.rf_requests.get_on_session(self.alias, "/get")
        return response

    @keyword("Post Dynamic Data")
    def post_dynamic_data(self, delay: Union[str, int]) -> any:
        """
        Post request to http bin service

        Args:
            delay (Union[str, int]): the delay amount

        Returns:
            any: response
        """
        url = f"/delay/{str(delay)}"
        response = self.rf_requests.post_on_session(self.alias, url=url)
        return response

    @keyword("Get HTTP Bin Alias")
    def get_alias(self) -> str:
        """
        Gets alias

        Returns:
            str: alias used
        """
        return self.alias

    @not_keyword
    def _get_requests_library_instance(self) -> RequestsLibrary:
        try:
            rf_requests = self.rf_builtin.get_library_instance(
                "RequestsLibrary")
        except (RobotNotRunningError, RuntimeError):
            rf_requests = RequestsLibrary()
        return rf_requests


if __name__ == "__main__":

    http_bin = HttpBinLibrary()
    http_bin.rf_builtin.log_to_console("*** Results ***\n")

    http_bin.create_http_bin_session()

    get_resp = http_bin.get_http_method()
    http_bin.rf_builtin.log_to_console(
        "*** Headers ***\n" + str(get_resp.headers))

    data_response = http_bin.post_dynamic_data("2")
    http_bin.rf_builtin.log_to_console(
        "*** Dynamic Data ***\n" + str(data_response.json()))

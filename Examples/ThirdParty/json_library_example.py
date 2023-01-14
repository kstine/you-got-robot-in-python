"""
Example of using JSONLibrary in a script

Note that while jsonlibrary is excellent at manipulating json objects,
it lacks the ability to 'pretty print'


python Examples/ThirdParty/json_library_example.py
"""
# import logging

from JSONLibrary import JSONLibrary
from robot.api.logger import logging


class JsonLibraryExample():
    """
    Many Third party tools like JSONLibrary do not need
    Robot Framework running to work.
    """

    def __init__(self):
        self.file_path = "Examples/ThirdParty/gnomes.json"
        self.rf_json = JSONLibrary()
        self.all_gnomes = self.load_gnomes()

    def load_gnomes(self) -> any:
        """
        Loading a json file.

        Returns:
            json: a json object
        """
        all_gnomes = self.rf_json.load_json_from_file(self.file_path)
        all_gnome_count = len(
            self.rf_json.get_value_from_json(all_gnomes, "$..gnome"))
        logging.debug("%i Gnomes Loaded", all_gnome_count)
        return all_gnomes

    def get_gnomes(self) -> list:
        """
        Using Json Path to return list of matched/filtered items.

        Returns:
            list: _description_
        """
        gnomes = self.rf_json.get_value_from_json(
            self.all_gnomes,
            "$..gnomes[?(@.gnome==true)]"
        )
        logging.info("There seems to be %i true gnomes.", len(gnomes))
        return gnomes

    def find_trolls(self):
        """
        Identifying and returning false gnomes.
        """
        trolls = self.rf_json.get_value_from_json(
            self.all_gnomes,
            "$..gnomes[?(@.gnome==false)]"
        )
        logging.warning("There are %s troll(s)!", str(len(trolls)))

    def get_the_next_gnome(self):
        """
        Using the next() method from Python to get the next matching json obj.
        Very useful if you know there shoulld be only one returned value, and
        being able to set a default is handy.
        """
        gnomes = self.get_gnomes()
        iter_gnomes = iter(gnomes)
        for i in range(len(gnomes)+1):
            next_gnome = next(iter_gnomes, "no gnomes")
            logging.critical("Gnome number %i: %s", i+1, next_gnome)
        next_gnome = next(iter(self.get_gnomes()), "no gnomes")
        logging.critical(next_gnome)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        filename="Examples/ThirdParty/json_lib.log",
                        filemode="w")

    json_lib = JsonLibraryExample()

    json_lib.get_gnomes()
    json_lib.find_trolls()
    json_lib.get_the_next_gnome()

# AUTOGENERATED! DO NOT EDIT! File to edit: 00_base.ipynb (unless otherwise specified).

__all__ = ["ISTAT"]

# Cell
import requests

# Cell
class ISTAT:
    """Base class that provides useful functions to communicate with ISTAT API"""

    def __init__(self):
        self.base_url = "http://sdmx.istat.it/SDMXWS/rest"
        self.agencyID = "IT1"

    def _request(self, path, **kwargs):
        """Make a request to ISTAT API given a 'path'"""
        url = "/".join([self.base_url, path])
        # print(url)

        if "headers" in kwargs.keys():
            response = requests.get(url, headers=kwargs["headers"])
        else:
            response = requests.get(url)

        return response

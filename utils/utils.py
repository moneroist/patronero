# This Python file uses the following encoding: utf-8
from re import search as reSearch

class Utils:
    @staticmethod
    def isUrlValid(url):
        return reSearch(r"^http:\/\/|(www\.)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$", url)

    @staticmethod
    def isOpenAliasMonero(txtRecord):
        return reSearch(r"^oa1:xmr", txtRecord)

    @staticmethod
    def unpackOpenAliasRecord(txtRecord):
        entries = txtRecord.replace(r"oa1:xmr ", '').replace('"', '').split(";")
        filtered = list(map(lambda x: x.split("="), list(filter(lambda e: reSearch(r"=", e), entries))))
        data = {}

        for entry in filtered:
            data[entry[0].strip()] = entry[1].strip()

        if "recipient_address" in data.keys():
            return data
        else:
            return None

    def isMiningPoolUrlValid(url):
        return reSearch(r"^(?:[A-Za-z0-9-]+\.)+[A-Za-z0-9]{1,3}:\d{1,5}$", url)

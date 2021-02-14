# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os.path, json
from jsonschema import validate as validateJSON, ValidationError, SchemaError

class Config(QObject):
    openMessageBox = pyqtSignal(int, str, str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.configPath = os.getcwd() + "/config.json"

    def setProperty(self, property, value):
        self.data[property] = value
        self.saveConfig()

    def getProperty(self, property):
        return self.data[property]

    def addProtege(self, protege):
        self.data['proteges'].append(protege)
        self.saveConfig()

    def removeProtege(self, protegeId):
        self.data['proteges'] = [protege for protege in self.data['proteges'] if not (protegeId == protege.get('id'))]
        self.saveConfig()

    def addMiningPool(self, miningPool):
        self.data['miningPools'].append(miningPool)
        self.saveConfig()

    def removeMiningPool(self, miningPoolId):
        self.data['miningPools'] = [miningPool for miningPool in self.data['miningPools'] if not (miningPoolId == miningPool.get('id'))]
        self.saveConfig()

    def readConfig(self):
        if os.path.isfile(self.configPath):
            with open(self.configPath) as file:
                try:
                    jsonfile = json.load(file)
                    validateJSON(jsonfile, self.configSchema())
                    self.data = jsonfile
                except:
                    self.openMessageBox.emit(QMessageBox.Critical, "Error", "Current config is invalid! Created defualt config.")
                    self.saveConfig(True)
        else:
            self.openMessageBox.emit(QMessageBox.Critical, "Error", "Config is missing! Created defualt config.")
            self.saveConfig(True)
            self.data = self.defaultConfig()

    def saveConfig(self, default=False):
        with open(self.configPath, 'w') as file:
            if default:
                json.dump(self.defaultConfig(), file)
                self.data = self.defaultConfig()
            else:
                json.dump(self.data, file)

    def defaultConfig(self):
        return {
        "currentProtegeId": "cfe5bec7-01b0-4b03-bb84-9ffe4a964465",
        "currentMiningPoolId": "bd3bb20c-cc6d-4bd3-a462-b287fea30cbe",
        "currentThreads": 1,
        "currentMode": "fast",
        "proteges": [
            { "id": "cfe5bec7-01b0-4b03-bb84-9ffe4a964465", "name": "Patronero", "address": "82vnpmqm1TLAtk4eK2vSkpjNUKTBq3DhGRZUYuQnCdcHEfPhLpEzqT6Qw8wqVfq2HXV15hXw1uBfBSzMRbZAqTLtLUUmdwp"}
        ],
        "miningPools": [
            { "id": "bd3bb20c-cc6d-4bd3-a462-b287fea30cbe", "name": "Patronero", "url": "pool.patronero.com:3333" }
        ]
    }

    def configSchema(self):
        return {
            "type": "object",
            "properties": {
                "currentProtegeId": {
                    "type": ["string", "null"]
                },
                "currentMiningPoolId": {
                    "type": ["string", "null"]
                },
                "currentThreads": {
                    "type": "integer"
                },
                "currentMode": {
                    "type": "string"
                },
                "proteges": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/protege"
                    }
                },
                "miningPools": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/miningPool"
                    }
                }
            },
            "required": ["currentProtegeId", "currentMiningPoolId", "currentThreads", "currentMode", "proteges", "miningPools"],
            "definitions": {
                "protege": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "address": {
                            "type": "string"
                        }
                    }
                },
                "miningPool": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "url": {
                            "type": "string"
                        }
                    }
                }
            }
        }

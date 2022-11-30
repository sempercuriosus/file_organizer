import os
from datetime import datetime
import shutil
from zipfile import ZipFile
import json

class Settings:
    # def __init__(self, _file_source, _file_desination, _log_file_path):
    #     self._file_source = _file_source
    #     self._file_desination = _file_desination
    #     self._log_file_path = _log_file_path
    __conf = {
        "file_source":""
        , "file_destination":""
        , "log_path":""
    }

    __setters = ["file_source","file_destination", "log_path"]

    @staticmethod
    def config(name):
        return Settings.__conf[name]

    @staticmethod
    def set(name, value):
        if (name in Settings.__setters):
            Settings.__conf[name] = value
        
def __main__():
    # main file call
    # _file_source = ""
    # _file_destination = ""

    GetSettings()

    # print(Settings.config("file_source"))
    # print(Settings.config("file_destination"))
    # print(Settings.config("log_path"))

    if ((Settings.config("file_source") != "") and (Settings.config("file_destination") != "") and (Settings.config("log_path") != "")):

        DoesPathExist(Settings.config("file_source"))
        DoesPathExist(Settings.config("file_destination"))

        IsPathZipped(path=Settings.config("file_source"))

        WalkDirectory(file_source=Settings.config("file_source"), file_destination=Settings.config("file_destination"))

## end : [__main__]


def GetSettings():

    try:
        with open("./configurations/appsettings.json", "r") as config_file:
            text = config_file.read()
            config = json.loads(text)
            _file_source = config["settings"]["source_path"]
            _file_desination = config["settings"]["target_path"]
            _log_file_path = config["settings"]["log_path"]

            Settings.set("file_source", _file_source)
            Settings.set("file_destination", _file_desination) 
            Settings.set("log_path", _log_file_path)
            
            LogToFile("Loaded configuration file.")

    except Exception as e:
        LogToFile("There was an error in loading the configuration file.")
        LogToFile(e)


## end : [GetSettings]


def DoesPathExist(path):
    if (not(os.path.exists(path))):
        LogToFile(f"The location [{path}] does not exist.")
        CreateMissingPath(path)

## end : [DoesPathExist]


def CreateMissingPath(path):
    
    try:
        os.makedirs(os.path.dirname(path))
        LogToFile(f"The path was missing and then created : {path}")
    except Exception as e:
        # print(f"There was an issue in creating the path {path}")
        LogToFile(e)

## end : [CreateMissingPath]


def LogToFile(text_to_write):
    # _log_file_path = ""
    _date = SetDate()
    _log_file_name = f"{_date}_log.txt"
    
    if (_log_file_name != "" and Settings.config("log_path") != ""):

        _log_full_path = JoinPath(Settings.config("log_path"), _log_file_name) 

        try:
            with open (str(_log_full_path), "a") as file:
                file.writelines("= = = = = = = = = = = = = = = = = = = = =")
                file.writelines('\n')
                file.writelines(f"Log File : {_date}")
                file.writelines('\n')
                file.writelines(f"text : {text_to_write}")
                file.writelines('\n')
                file.writelines("= = = = = = = = = = = = = = = = = = = = =")
                file.writelines('\n')
                file.writelines('\n')

        except Exception as e:
            LogToFile(f"there was an error writing the log file : {str(e)}")

## end : [LogToFile]error_text


def SetDate():  
    _year = datetime.now().year
    _month = datetime.now().month
    _date_string = f"{_year}_{_month}"

    return _date_string

## end : [SetDate]


def WalkDirectory(file_source, file_destination):
    if (file_source != "" and file_destination != ""):
        for dirpath, dnames, fnames in os.walk("./"):
            for f in fnames:
                if f.endswith(".svg"):
                    MoveFile(source=file_source, destination=file_destination)
                elif f.endswith(".png"):
                    MoveFile(source=file_source, destination=file_destination)

## end : [WalkDirectory]


def JoinPath(file_path, file_name):
    _joined_path = ""

    try:
       _joined_path = os.path.join(file_path, file_name)
    except Exception as e:
        LogToFile(e)
    
    return _joined_path

## end : [MoveFiles]


def MoveFile(source, destination):
    try:
        shutil.move(source, destination) 
    except Exception as e:
        LogToFile(e)

## end : [MoveFile]


def IsPathZipped(path):
    
    # if path is zipped
    if (path.endswith(".zip")):
        UnzipFolder(path)    

## end : [IsPathZipped]


def UnzipFolder(path):
    try:
        with ZipFile (path) as _zip:
            _zip.extractall(path=path)
    except Exception as e:
        LogToFile(e)

## end : [UnzipFolder]



__main__()
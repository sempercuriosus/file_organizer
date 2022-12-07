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

        CheckPathExists(Settings.config("file_source"))
        CheckPathExists(Settings.config("file_destination"))

        IsPathZipped(path=Settings.config("file_source"))

        WalkDirectory(file_source=Settings.config("file_source"), file_destination=Settings.config("file_destination"))

        LogToFile(log_type="text", log_title="Script End", log_text="The script completed.", log_called_by="__main__")
## end : [__main__]


def GetSettings():
    _configuration_file_path = "./configurations/appsettings.json"
    CheckAppSettingsExists(configuration_file_location=_configuration_file_path)

    try:
        with open(_configuration_file_path, "r") as config_file:
            text = config_file.read()
            config = json.loads(text)
            _file_source = config["settings"]["source_path"]
            _file_desination = config["settings"]["target_path"]
            _log_file_path = config["settings"]["log_path"]

            Settings.set("file_source", _file_source)
            Settings.set("file_destination", _file_desination) 
            Settings.set("log_path", _log_file_path)
            
            LogToFile(log_type="text", log_title="Configuration Successful", log_text="Loaded configuration file.", log_called_by="GetSettings")

    except Exception as e:
        LogToFile(log_type="text", log_title="Configuration Error", log_text="There was an error in loading the configuration file : ", log_called_by="GetSettings()")
        LogToFile(log_type="e", log_title="Configuration Error", log_text=f"{e}", log_called_by="GetSettings()")


## end : [GetSettings]

def CheckAppSettingsExists(configuration_file_location):
    
    try:
        _file_exists = os.path.isdir(configuration_file_location)
    except Exception as e:
        LogToFile(log_type="error", log_title="Check If appsettings exists.", log_text="There was an issue in checking that appsettings existing ", log_called_by="CheckAppSettingsExists")

    _default_lines ="""{
    "settings": {
        "source_path": "",
        "target_path": "",
        "log_path": ""
    }
    }"""
    try:
        if _file_exists == False:
            with open(configuration_file_location, "w") as appsettings_file:
                appsettings_file.writelines(_default_lines)
    except Exception as e:
        LogToFile(log_type="Make Settings Fail", log_title="App Settings Create Error", log_text=f"There was an error in writing the file.", log_called_by="CheckAppSettingsExists", additional_lines=e) 

## end : [CheckAppSettingsExists]



def LogToFile(log_type, log_title, log_text, log_called_by, additional_lines=""):
    # _log_file_path = ""
    _date = SetDate()
    _log_file_name = f"{_date}_log.txt"
    _log_path = Settings.config("log_path")
    
    if _log_file_name == "":
        _log_file_name = f"no_date_log.txt" 
    
    if Settings.config("log_path") == "":
        _log_path = SetDefaultLogPath()

        _log_full_path = JoinPath(_log_path, _log_file_name) 

        if log_type == "e" or log_type == "error":
            log_title = "Error !!!"

        try:
            with open (str(_log_full_path), "a") as file:
                file.writelines("= = = = = = = = = = = = = = = = = = = = =")
                file.writelines('\n')
                file.writelines(f"Log File : {_date}")
                file.writelines('\n')
                file.writelines("- - - - -")
                file.writelines('\n')
                file.writelines(f"[{str(log_title)}] : {str(log_called_by)}")
                file.writelines('\n')
                file.writelines(f"{str(log_text)}")
                file.writelines('\n')
                file.writelines(f"Additional Note : ")
                file.writelines('\n')
                file.writelines(f"{additional_lines}")
                file.writelines('\n')
                file.writelines(f"Log File : End")
                file.writelines('\n')
                file.writelines("= = = = = = = = = = = = = = = = = = = = =")
                file.writelines('\n')
                file.writelines('\n')

        except Exception as e:
            print(f"there was an error writing the log file : {str(e)}")

## end : [LogToFile]error_text

def SetDefaultLogPath():
    _default_log_path = ""

    _default_log_path = os.getcwd()

    _default_log_path = JoinPath(_default_log_path, "logs")

    return _default_log_path
## end : [SetDefaultLogPath]




def CheckPathExists(path):
    if (not(os.path.exists(path))):
        LogToFile(log_type="text", log_title="Path Exists", log_text=f"The location [{path}] does not exist.", log_called_by="CheckPathExists")
        CreateMissingPath(path)

## end : [CheckPathExists]


def CreateMissingPath(path):
    try:
        os.makedirs(path)
        LogToFile(log_type="text",log_title="Path Created",log_text=path, log_called_by="CreateMissingPath", additional_lines="Path created.")
    except FileExistsError as _file_exists:
        LogToFile(log_type="error",log_title="File Exists Exception",log_text=_file_exists, log_called_by="CreateMissingPath")
    except Exception as e:
        LogToFile(log_type="error",log_title="Missing Path Exception",log_text=e, log_called_by="CreateMissingPath")

## end : [CreateMissingPath]


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
        LogToFile(log_type="error",log_title="Path Join Error", log_text=e, log_called_by="JoinPath")
    
    return _joined_path

## end : [MoveFiles]


def MoveFile(source, destination):
    try:
        shutil.move(source, destination) 
    except Exception as e:
        LogToFile(log_type="error", log_title="Move File Exception", log_text=f"Could not move the file : {source}", log_called_by="MoveFile")
        # LogToFile(e)

## end : [MoveFile]


def IsPathZipped(path):
    
    # if path is zipped
    if (path.endswith(".zip")):
        UnzipFolder(path)    

## end : [IsPathZipped]


def UnzipFolder(path):
    try:
        with ZipFile (path) as _zip:
            LogToFile(log_type="text", log_title="Unzip Start", log_text=f"path was zipped : {path}", log_called_by="UnzipFolder")
            _zip.extractall(path=path)
            LogToFile(log_type="text", log_title="Unzip End", log_text="path was unzipped.", log_called_by="UnzipFolder")

    except Exception as e:
        LogToFile(log_type="error",log_title="Unzip Error", log_text=f"could not extract files at : {path}", log_called_by="UnzipFolder")

        LogToFile(log_type="error",log_title="Error Details",log_text=e, log_called_by="UnzipFolder")

## end : [UnzipFolder]



__main__()
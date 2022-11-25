import os
from datetime import datetime
import shutil
from zipfile import ZipFile

def __main__():
    # main file call
    _file_source = ""
    _file_destination = ""

    DoesPathExist(_file_source)
    DoesPathExist(_file_destination)

    IsPathZipped(path=_file_source)

    WalkDirectory(file_source=_file_source, file_destination=_file_destination)

## end : [__main__]


def GetSettings():
    _file_source = ""
    _file_desination = ""
    _Log_file_path = ""

## end : [GetSettings]



def DoesPathExist(path):
    if (not(os.path.exists(path))):
        # print(f"The location [{path}] does not exist.")
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


def LogToFile(error_text):
    _log_file_path = "/Users/erichulse/Projects/file_organizer/logs"
    _date = SetDate()
    _log_file_name = f"{_date}_log.txt"
    
    if (_log_file_name != "" and _log_file_path != ""):

        _log_full_path = JoinPath(_log_file_path, _log_file_name) 

        try:
            with open (str(_log_full_path), "a") as file:
                file.writelines("= = = = = = = = = = = = = = = = = = = = =")
                file.writelines('\n')
                file.writelines(f"Log File : {_date}")
                file.writelines(f"error text : {error_text}")
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
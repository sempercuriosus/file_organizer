import os
import datetime


def __main__():
    # main file call
    _file_source = ""
    _file_destination = ""

    pass

## end : [__main__]

def DoesPathExist(path):
    _path_exists = False

    if (os.path.exists(path)):
        _path_exists = True
    else:
        print(f"The location [{path}] does not exist.")
        CreateMissingPath(path)

    return _path_exists

## end : [DoesPathExist]


def CreateMissingPath(path):
    
    try:
        os.makedirs(os.path.dirname(path))
    except:
        print(f"There was an issue in creating the path {path}")

## end : [CreateMissingPath]


def LogToFile(error_text):
    _log_file_path = ""
    _date = SetDate()
    _log_file_name = ""
    
    _log_file_name = f"{_date}_log.txt"
    
    if (_log_file_name != "" and _log_file_path != ""):
        _log_full_path = os.path.join(_log_file_path, _log_file_name)

        try:
            with open (_log_full_path, "a") as file:
                pass
        except:
            pass

## end : [LogToFile]error_text


def SetDate():  
    _year = datetime.now().year
    _month = datetime.now().month
    _date_string = f"{_year}_{_month}"

    return _date_string

## end : [SetDate]



def MoveFiles():
    pass

## end : [MoveFiles]


def UnzipFolder():
    pass

## end : [UnzipFolder]



__main__()
import os
import datetime
import shutil

def __main__():
    # main file call
    _file_source = ""
    _file_destination = ""
    _path_flag = False


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


def WalkDirectory(path_to_walk, file_source, file_destination):
    for dirpath, dnames, fnames in os.walk("./"):
        for f in fnames:
            if f.endswith(".svg"):
                MoveFile(source=file_source, destination=file_destination)
            elif f.endswith(".png"):
                MoveFile(source=file_source, destination=file_destination)
## end : [WalkDirectory]


def JoinPath(file_path, file_name):
    try:
        os.path.join(file_path, file_name)
    except Exception as e:
        LogToFile(e)

## end : [MoveFiles]

def MoveFile(source, destination):
    try:
        shutil.move(source, destination) 
    except Exception as e:
        LogToFile(e)

## end : [MoveFile]


def LogToFile(error_text):
    _log_file_path = ""
    _date = SetDate()
    _log_file_name = ""
    
    _log_file_name = f"{_date}_log.txt"
    
    if (_log_file_name != "" and _log_file_path != ""):

        _log_full_path = JoinPath(_log_file_path, _log_file_name) #os.path.join(_log_file_path, _log_file_name)

        try:
            with open (_log_full_path, "a") as file:
                file.writelines(f"Log File : {_date}")
                file.writelines(f"error text : {error_text}")
        except Exception as e:
            print(f"there was an error writing the log file : {str(e)}")

## end : [LogToFile]error_text


def SetDate():  
    _year = datetime.now().year
    _month = datetime.now().month
    _date_string = f"{_year}_{_month}"

    return _date_string

## end : [SetDate]


def UnzipFolder():
    pass

## end : [UnzipFolder]



__main__()
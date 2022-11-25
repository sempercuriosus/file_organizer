import os


def __main__():
    # main file call
    _file_source = ""
    _file_destination = ""
    _log_file = ""

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



def MoveFiles():
    pass

## end : [MoveFiles]


def UnzipFolder():
    pass

## end : [UnzipFolder]



__main__()
import os


def __main__():
    # main file call
    _file_source = ""
    _file_source_exists = False
    _file_destination = ""
    _file_destination_exists = False

    if (_file_source_exists and _file_destination_exists):
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
    pass

## end : [CreateMissingPath]


def WalkDirectory():
    pass    

## end : [WalkDirectory]


def CheckForFileType(file_path, file_type):
    if (file_type.endswith("")):
        MoveFiles(file_path)

## end : [CheckForFileType]


def ExtractFiles():
    pass

## end : [ExtractFiles]


def MoveFiles(file_path):
    try:
        pass
    except Exception as e:
        Log(e)

## end : [MoveFiles]


def UnzipFolder():
    pass

## end : [UnzipFolder]



__main__()
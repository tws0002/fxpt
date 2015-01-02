import os


def pathToSlash(path):
    return path.replace('\\', '/')


def pathToBackslash(path):
    return path.replace('/', '\\')


def getFxptLocation():
    scriptDir = pathToSlash(os.path.dirname(__file__))
    return '/'.join(scriptDir.split('/')[:-2])


def getFxUtilsDir():
    return pathToSlash(os.path.dirname(__file__))
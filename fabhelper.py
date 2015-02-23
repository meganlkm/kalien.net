""" fabric helper functions """

import os
import shutil


def cwd():
    """ get the current working directory """
    return os.getcwd()


def isdir(src):
    """ alias for os.path.isdir """
    return os.path.isdir(src)


def exists(src):
    """ alias for os.path.exists """
    return os.path.exists(src)


def joinpath(*args):
    """ os join shortcut """
    return os.path.join(*args)


def rm(src):
    """ remove file/dir """
    if os.path.isdir(src):
        return rmdir(src)
    return rmfile(src)


def rmfile(src):
    """ remove file """
    return os.remove(src)


def rmdir(src):
    """ remove directory """
    return shutil.rmtree(src)


def move(src, dest):
    """ move a file """
    if isdir(src):
        return movedir(src, dest)
    return shutil.move(src, dest)


def movedir(src, dest):
    """ rename directory """
    return os.rename(src, dest)


def touch(filename):
    """ touch a file """
    if exists(filename):
        return os.utime(filename, None)
    return open(filename, 'a').close()


def get_file_contents(filename):
    """ load contents of the file """
    if exists(filename):
        with open(filename) as doc:
            return doc.read()


def file2list(filename):
    """ read in a file and convert to list """
    content = get_file_contents(filename)
    return content.rstrip('\n').split('\n')

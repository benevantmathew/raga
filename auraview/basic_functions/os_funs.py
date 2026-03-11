"""
basic_functions/os_funs.py

Author: Benevant Mathew
Date: 2025-12-16
"""

import os
import shutil

import pandas as pd


def get_ext(file):
    """
    Docstring for get_ext

    :param file: Description
    """
    ext = file.split('.')[-1]
    return ext

def rename(file, new_name):
    """
    Docstring for rename

    :param file: Description
    :param new_name: Description
    """
    os.rename(file, new_name)
    return print('rename completed')

def get_all_files(loc):
    """
    Docstring for get_all_files

    :param loc: Description
    """
    out = []
    for (path, _, files) in os.walk(loc):
        for name in files:
            out.append(os.path.join(path, name))
    return out

def get_rootname(file):
    """
    Docstring for get_rootname

    :param file: Description
    """
    out = '.'.join(file.split('.')[:-1])
    return out

def get_end_from_path(path):
    """
    Docstring for get_end_from_path

    :param path: Description
    """
    file = os.path.basename(path)
    return file

def get_previous_dir_from_path(path):
    """
    Docstring for get_previous_dir_from_path

    :param path: Description
    """
    out = os.path.dirname(path)
    return out

def read_excel(file, page_name=None):
    """
    Docstring for read_excel

    :param file: Description
    :param page_name: Description
    """
    if page_name == None:
        df = pd.read_excel(file)
    else:
        xls = pd.ExcelFile(file)
        df = pd.read_excel(xls, page_name)
    return df

def read_csv(file):
    """
    Docstring for read_csv

    :param file: Description
    """
    #read a csv file to df
    return(pd.read_csv(file))

def move(c_path, d_path):
    """
    Docstring for move

    :param c_path: Description
    :param d_path: Description
    """
    os.rename(c_path, d_path)
    return print('{} moved'.format(c_path))

def copy(c_path, d_path):
    """
    Docstring for copy

    :param c_path: Description
    :param d_path: Description
    """
    if not os.path.exists(c_path):
        print('Path not found: {}'.format(c_path))
        return
    shutil.copyfile(c_path, d_path)
    return print('{} created'.format(d_path))

def get_file_size(file):
    """
    Docstring for get_file_size

    :param file: Description
    """
    out = round(os.path.getsize(file) / (1024 * 1024), 2)
    return out

import json
from typing import List, Tuple, Union
from .check import is_file, is_folder
import os


def load_from_file(file_path: str) -> dict:
    '''
    function to read json.
    Args:
        filename (str): json file.
    Returns:
        dict: json load to dictionary
    '''
    if not is_file(file_path):
        raise ValueError(f'{file_path} is not exist.')
    with open(str(file_path), 'r') as f:
        data = json.load(f)
    return data


def dump_to_file(
    data: Union[dict, list, tuple],
    file_path: str
):
    '''
    function to dump json.
    Args:
        data: object need to be dumped.
        filename (str): json file.
    '''
    if not is_folder(to_path.parent):
        os.makedirs(to_path.parent)
    with open(file_path, 'w') as f:
        json.dump(data, f)

from pathlib import Path
from .check import is_folder, is_str, is_file
import os
import errno
import shutil
from typing import List, Tuple, Union
import hashlib
import pickle


def find(
    folder: Union[str, Path],
    suffix: Union[str, List[str], Tuple[str]] = None,
    return_pathlib: bool = True,
):
    '''
    Function to getting all files in the folder with given suffix.

    Args:
        folder (str):
            An existing folder.
        suffix (Union[str, List[str], Tuple[str]], optional):
            Get all files with same suffix, ex: ['.jpg', '.png'].
            Default is None, which means getting all files in the folder.
        return_pathlib (bool, optional):
            whether to return Path or not

    Raises:
        TypeError:
            check folder is exist.
            suffix must be a list or a string.

    Returns:
        files (list):
            Output a list of files' path in absolute mode.
    '''

    # checking folders
    folder = Path(folder)
    if not is_folder(folder):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), str(folder))

    # checking suffix
    suffix = [suffix] if is_str(suffix) else suffix
    if not isinstance(suffix, (list, tuple)) and suffix is not None:
        raise TypeError('suffix must be a string, list or tuple.')

    # walk through all files
    if suffix is None:
        files = [f.absolute() for f in folder.rglob('*')]
    else:
        files = [f.absolute() for f in folder.rglob('*') if f.suffix in suffix]

    if not return_pathlib:
        files = [str(f) for f in files]

    return files


def copy_file(from_path: Union[str, Path],
              to_path: Union[str, Path]):
    from_path = Path(from_path)
    to_path = Path(to_path)
    if not is_file(from_path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), str(from_path))
    if not is_folder(to_path.parent):
        os.makedirs(to_path.parent)
    shutil.copyfile(from_path, to_path)


def move_file(from_path: Union[str, Path],
              to_path: Union[str, Path]):
    from_path = Path(from_path)
    to_path = Path(to_path)
    if not is_file(from_path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), str(from_path))
    if not is_folder(to_path.parent):
        os.makedirs(to_path.parent)
    shutil.move(from_path, to_path)


def move_folder(from_path: Union[str, Path],
                to_path: Union[str, Path],
                overwrite=False):
    from_path = Path(from_path)
    to_path = Path(to_path)
    if not is_folder(from_path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), str(from_path))
    if overwrite:
        remove(to_path/from_path.name)
    if is_folder(to_path/from_path.name):
        raise FileExistsError(
            errno.EEXIST, os.strerror(errno.EEXIST), str(to_path))
    if not is_folder(to_path):
        os.makedirs(to_path)
    shutil.move(from_path, to_path/from_path.name)


def load_pickle(path: Union[str, Path]):
    '''
    Function to load a pickle.

    Args:
        path (Union[str, Path]): file path.

    Returns:
        loaded_pickle (dict): loaded pickle.
    '''
    if not is_file(path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), str(path))
    with open(str(path), 'rb') as f:
        return pickle.load(f)


def dump_pickle(obj, path: Union[str, Path]):
    '''
    Function to dump an obj to a pickle file.

    Args:
        obj: object to be dump.
        path (Union[str, Path]): file path.
    '''
    with open(str(path), 'wb') as f:
        pickle.dump(obj, f)


def remove(path):
    if is_folder(path):
        shutil.rmtree(path)
    else:
        Path(path).unlink()


def gen_md5(file: Union[str, Path], block_size: int = 256 * 128) -> str:
    '''
    This function is to gen md5 based on given file.

    Args:
        file (Union[str, Path]): filename
        block_size (int, optional): reading size per loop. Defaults to 256*128.

    Raises:
        ValueError: check file is exist.

    Returns:
        md5 (str)
    '''
    if not is_path_exist(file):
        raise ValueError(f'{file} is not exist.')

    with open(str(file), 'rb') as file:
        md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(block_size), b''):
            md5.update(chunk)
    md5 = str(md5.hexdigest())

    return md5

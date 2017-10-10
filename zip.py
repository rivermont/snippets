import shutil
from os import makedirs


def zip_files(out_file_name, dir_):
    """
    Creates a .zip file in the current directory containing all contents of dir_, then clears dir_.
    """
    shutil.make_archive(str(out_file_name), 'zip', dir_)
    shutil.rmtree(dir_)
    makedirs(dir_[:-1])

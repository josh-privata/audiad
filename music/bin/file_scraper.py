import os
from mutagen.id3 import ID3


def mp3_files(root):
    # this is a generator that will return mp3 file paths within given dir
    for f in os.listdir(root):
        fullpath = os.path.join(root, f)
        if os.path.isdir(fullpath) and not os.path.islink(fullpath):
            for x in mp3_files(fullpath):  # recurse into subdir
                yield x
        else:
            if fullpath[len(fullpath)-3:] == 'mp3':
                yield fullpath


def get_tags(root_dir):
    try:
        for p in mp3_files(root_dir):
            id3_data = ID3(p)
            id3_data.update_to_v24()
            id3_data.keys()
            for k, v in id3_data.items():
                print(k, ":", v)
            return id3_data
    except ():
        print("Invalid ID3 tag")

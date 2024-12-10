# Deleting a File from TAR Archive
# The tarfile module does not support direct file deletion. Instead, create a new archive excluding the file:

import tarfile

with tarfile.open("example.tar", "r") as tar:
    with tarfile.open("new_example.tar", "w") as new_tar:
        for member in tar.getmembers():
            if member.name != "file1.txt":
                new_tar.addfile(member, tar.extractfile(member) if member.isfile() else None)

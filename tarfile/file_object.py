# Working with File Objects
import tarfile

# Read File Content Directly
with tarfile.open("example.tar", "r") as tar:
    file = tar.extractfile("file1.txt")
    content = file.read()
    print(content.decode("utf-8"))

# Write to a File-Like Object
import io

data = io.BytesIO(b"Hello, World!")
with tarfile.open("example.tar", "w") as tar:
    tarinfo = tarfile.TarInfo(name="hello.txt")
    tarinfo.size = len(data.getvalue())
    tar.addfile(tarinfo, data)

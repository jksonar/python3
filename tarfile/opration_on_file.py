import tarfile, sys

try:
    #open tarfile
    tar = tarfile.open(sys.argv[1], "r:tar")

    #present menu and get selection
    selection = input("Enter\n\
    1 to extract a file\n\
    2 to display information on a file in the archive\n\
    3 to list all the files in the archive\n\n")

    #perform actions based on selection above
    if selection == "1":
        filename = input("enter the filename to extract:  ")
        tar.extract(filename)
    elif selection == "2":
        filename = input("enter the filename to inspect:  ")
        for tarinfo in tar:
            if tarinfo.name == filename:
                print("Filename:", tarinfo.name, "Size:", tarinfo.size, "bytes")
    elif selection == "3":
        print(tar.list(verbose=True))
except:
    print("There was a problem running the program")

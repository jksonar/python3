import librsync

# Example of file delta creation
with open("source_file", "rb") as source, open("patch_file", "wb") as patch:
    librsync.signature(source, patch)

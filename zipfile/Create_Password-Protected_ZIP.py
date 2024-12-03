# Create Password-Protected ZIP
import pyminizip

pyminizip.compress("file1.txt", None, "protected.zip", "password", 5)  # 5 = Compression level

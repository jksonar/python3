import os
import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    print("Temporary Directory:", temp_dir)
    # Use the temp_dir for temporary file storage
# The directory is automatically deleted when the block ends

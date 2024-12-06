# Remove an Environment Variable
import os

os.environ.pop('MY_VAR', None)
print("MY_VAR removed.")

import json
from pathlib import Path

# write JSON files:
with Path("temp.json").open("w", encoding="UTF-8") as target: 
    json.dump(travel3, target, default=blog_j2_encode)


# read JSON files:
from pathlib import Path
with Path("some_source.json").open(encoding="UTF-8") as source:
     objects = json.load(source, object_hook=blog_decode)

# read JSON files single line code:
objects = json.loads(Path("some_source.json").read_text(encoding="UTF-8"), object_hook=blog_decode)
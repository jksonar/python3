# Accept JSON Strings as Arguments
import argparse
import json

def parse_json(value):
    try:
        return json.loads(value)
    except json.JSONDecodeError as e:
        raise argparse.ArgumentTypeError(f"Invalid JSON: {e}")

parser = argparse.ArgumentParser(description="Parse JSON strings.")
parser.add_argument("--data", type=parse_json, help="Provide a JSON string.")
args = parser.parse_args()

print(f"Parsed JSON: {args.data}")

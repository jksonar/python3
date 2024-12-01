# Specify Argument Groups
import argparse

parser = argparse.ArgumentParser(description="Organize arguments into groups.")
group1 = parser.add_argument_group("Group 1", "Arguments related to feature 1.")
group1.add_argument("--feature1", help="Enable feature 1.")

group2 = parser.add_argument_group("Group 2", "Arguments related to feature 2.")
group2.add_argument("--feature2", help="Enable feature 2.")

args = parser.parse_args()
print(args)

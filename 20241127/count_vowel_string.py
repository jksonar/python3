# Count Vowels in a String



text_line = input("Enter string one line ").lower()
vowels_char = "aeiou"
count_all_vowels = sum(1 for char in text_line if char in vowels_char)
print("Number of vowels: ", count_all_vowels)
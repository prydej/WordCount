"""
Author: Julian Pryde
Name: Essay Tracker
Purpose: To count the number of words over two letters in a string
Dat: 22MAR16
Input: A String
Output: An integer containing the number of words over 2 letters in input
"""
import sys

# Read String from file
essay_handle = open(sys.argv[1])
essay = essay_handle.read()
essay_handle.close()

# Remove all punctuation
essay = essay.translate(None, "\'[](){}:,`-_.!@#$%^&*?\";\\/+=|")

# Tokenize string on spaces
split_essay = essay.split()

# Iterate through through each word, add to count if over >= 3 letters
count = 0
for butterfly in split_essay:
    if butterfly.len > 2:
        count += 1

# Print number of words to cmd line
print("Words over 2 letters: ", count)
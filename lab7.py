"""
TEXT ANALYZER TOOL (Basic Version - No function)
-------------------------------------------------------------------
Concept Demonstrated: strings, Indexing, Slicing String Transversal 

The user enters a paragraph, and the program analyzes it to count:
    - Total characters
    - Total words
    - Total vowels
    - Total spaces
    - Total consonants
    - Total digits
"""

print("=" * 45)
print("             TEXT ANALYZER TOOL ")
print("=" * 45)

paragraph = input(" Enter a paragraph:\n")

# ----------------- Basic Info using len() and slicing -------------
total_length = len(paragraph)

print("\n----- Basic Info -----")
print("Total characters (including spaces):", total_length)
print("First 10 characters (slicing)      :", paragraph[0:10])
print("Last 10 characters (slicing)       :", paragraph[-10:])
print("Reversed paragraph (slicing)       :", paragraph[::-1])

#-----------------counters-------------------
vowel_count = 0
space_count = 0
consonent_count = 0
digit_count = 0
other_count = 0

vowels = "aeiouAEIOU"

# ---------------------------- Transversal using indexing ------------------
for i in range(len(paragraph)):
    ch = paragraph[i]          # accesing character using index

    if ch == " ":
        space_count = space_count + 1
    elif ch.isalpha():
        if ch in vowels:
            vowel_count = vowel_count + 1
        else:
            consonent_count = consonent_count + 1
    elif ch.isdigit():
        digit_count = digit_count + 1
    else:
        other_count = other_count + 1       #punctuation, symbols, etc.

# ------------------- Word count --------------------
words = paragraph.split()          #splits paragraph into a list of words
word_count = len(words)

#---------------------------- Display Results ----------------------
print("\n----- Character Analysis -----")
print("Total vowels          :", vowel_count)
print("Total consonants      :", consonent_count)
print("Total spaces          :", space_count)
print("Total spaces          :", space_count)
print("Other characters      :", other_count,  "(punctuation/symmbols)")

print("\n----- Word Analysis -----")
print("Total Words           :", word_count)
print("First Word            :", words[0])
print("Last Word             :", words[-1])

print("\n--------- word List (Transversal) --------")
for i in range(len(words)):
    print(f"Word {i + 1}: {words[i]}")

    print()
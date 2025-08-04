from collections import Counter
if Counter(input("s1:").rstrip())==Counter(input("s2:").rstrip()):
    print("Anagram")
else:
    print("Not Anagram")
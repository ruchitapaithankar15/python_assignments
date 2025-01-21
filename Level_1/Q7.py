# Taking input from the user
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Check if lengths are different
if len(s) != len(t):
    print("The strings are not anagrams.")
else:
    # Create dictionaries to count character occurrences
    dictS = {}
    dictT = {}

    for i in range(len(s)):
        dictS[s[i]] = 1 + dictS.get(s[i], 0)
        dictT[t[i]] = 1 + dictT.get(t[i], 0)

    # Compare character counts
    is_anagram = True
    for i in dictS:
        if dictS[i] != dictT.get(i, 0):
            is_anagram = False
            break

    if is_anagram:
        print("True")
    else:
        print("False")

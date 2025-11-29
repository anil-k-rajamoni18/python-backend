vowels=['a','e','i','o','u']
word=input("Enter the word: ")
noofVowels=0
for letter in word:
    if letter in vowels:
        noofVowels+=1
print(f"No of vowels is : {noofVowels}")
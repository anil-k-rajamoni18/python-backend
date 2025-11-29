paragraph=input("Enter a paragraph: ")
print(f"Total Words:{len(paragraph.split())}")
print(f"Total Characters:{len(paragraph)}")
max=0
for word in paragraph.split():
    if len(word)>max:
        max=len(word)
        indexofword=paragraph.find(word)
print(f"longest word : {paragraph[indexofword:indexofword+max+1]}")        
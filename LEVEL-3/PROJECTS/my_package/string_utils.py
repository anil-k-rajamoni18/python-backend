def is_upper(string):
    return string.isupper()

def contains_vowel(string: str) -> bool:
    vowels = 'aeiouAEIOU'
    return  any(char in vowels for char in string)



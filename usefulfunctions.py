from collections import Counter # Had to SO this because I had no idea what the most efficient way to check list duplication is

def list_to_string(list: list): # I'm sure I'm overthinking it, but all the ways I found on SO had edge cases where they didn't work
    string = ""
    for i in list:
        string = string + string.join(i)
    return string

def remove_duplicates(plain: str):
    removed = [x for x in plain]
    removed.reverse()
    duplications = Counter(removed)
    for key in duplications:
        if duplications.get(key) > 1:
            while duplications.get(key) > 1:
                removed.remove(key)
                duplications = Counter(removed)
    removed.reverse()
    removed_str = list_to_string(removed)
    return removed_str
                
            
print(remove_duplicates("duckkd"))
print(remove_duplicates("xxkittyxx"))
print(remove_duplicates("Python makes we want to hang myself with a list iterator"))
def disemvowel(string_: str):
    new_string = [char for char in string_ if char not in 'aeiouAEIOU']
    return "".join(new_string)
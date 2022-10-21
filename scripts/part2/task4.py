def printer_error(s):
    err_counter = 0
    for char in s:
        if not 96 < ord(char) < 110:
            err_counter += 1
    return f"{err_counter}/{len(s)}"
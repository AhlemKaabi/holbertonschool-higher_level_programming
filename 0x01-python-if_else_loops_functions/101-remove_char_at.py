#!/usr/bin/python3
def remove_char_at(str, n):
    if (n < len(str) and n >= 0):
        ch = list(str)
        del(ch[n])
        str = "".join(ch)
        return(str)
    else:
        return(str)

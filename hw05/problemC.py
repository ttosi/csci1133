def character_search(string_a, string_b, string_c):
    str_first = ""
    for a in string_a:
        for b in string_b:
            if a == b:
                str_first += a

    str_second = ""
    for s in str_first:
        test = False
        for c in string_c:
            if c == s:
                test = True
        if not test:
            str_second += s

    return str_second


if __name__ == "__main__":
    print(character_search("ABCDEFGHI", "ABCD", "abCd"))  # "ABD"
    print(character_search("cats dog", "cats", "a"))  # "cts"
    print(character_search("cats dog", "rats", "a"))  # "ts"
    print(character_search("cats dog", "cats ", "cats "))  # ""


# def character_search(string_a, string_b, string_c):
#     output_str = ""
#     for char_a in string_a:
#         found = False
#         for char_b in string_b:
#             if char_a == char_b:
#                 for char_c in string_c:
#                     if char_a == char_c:
#                         found = True
#                         break
#                 if not found:
#                     output_str += char_a
#                 break
#     return output_str

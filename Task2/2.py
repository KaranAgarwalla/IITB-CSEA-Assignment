a = [204, 216, 389, 413, 493, 437, 234, 197, 465, 421, 224, 433, 205, 381, 401, 421, 213, 449, 209, 232, 198, 208, 381, 98, 461, 190, 209, 477, 202, 213, 193, 437, 405, 250]
b = [(x-1)/4 if x%2==1 else x/2 for x in a]
b = [int(x) for x in b]
print(''.join(chr(i) for i in b))
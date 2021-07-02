# Task2

There are three definitions of 'f' differing in the type of arguments: int, float and string.

The f(float) transforms x to 4*floor(x)+1

The f(int) transforms x to 2*x

f(string) transforms input characters to integer and casts it into float and int types randomly. Calls f on each of these numbers.

To reconstruct flag, reverse f and then convert it into characters. If number is odd then it must have been float else int. Thus, if number is odd, divide (x-1) by 4 else divide x by 2 to obtain ascii codes. Convert the ascii codes to character. 

Run [2.py](2.py) to obtain flag.

flag: mu1tipl3_di5p4tch_1s_4we50me
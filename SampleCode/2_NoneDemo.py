# THIS IS JUST A SIMPLE FILE TO DEMONSTRATE SOME OF THE DIFFERENCES BETWEEN IS NONE AND NOT.
import numpy as np

list_of_values = ["Hello",[], {},"", " ", 1, 0, '1', '0',None, np.nan, True, False, "True", "False", -1]


#  WHEN YOU RUN THIS CODE WHAT DO YOU THINK THE OUT PUT IS GOING TO BE?
for val in list_of_values:
    sval = f"'{val}'".ljust(8)
    print(f"{sval} : ", end="")

    if val:
        print("truthy".ljust(8), end="")
    else:
        print("falsy".ljust(8), end="")

    if val is None:
        print(" - is None")
    else:
        print(" - is NOT None")

print ("""
We see the following items are False, it shouldn't be surprising, but may catch you off guard.
 []     (EMPTY LIST)
 {}    (EMPTY DICTIONARY)
 ''    (EMPTY STRING
 0     (THE INTEGER ZERO)
 None  (NULL)
 False (BOOLEAN FALSE)

The following are true, does np.NaN surprise you?
 'Hello' (STRING WITH LEN > 0)
 ' '     (STING WITH ONLY SINGLE SPACE)
 1       (THE INTEGER 1)
 '1'     (THE STRING '1')
 '0'     (THE STRING '0')
 NaN     (NUMPY's NaN) <- This might be surprising
 'True'  (THE STRING 'True')
 True    (BOOLEAN TRUE)
 'False' (THE STRING 'False')
 -1      (THE INTEGER -1)
 
Of all these values, the only one that "is None" is, well, None.  So, it may be
tempting to take a few keystrokes off and use "if variable_name:" to verify
"None-ness" but don't. Use "if variable_name is None:"
""")



primes = [
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
]

fibonacci = [
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
]

alphas = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

special_characters = """'`"!@#$%^&* (){}[]-+?_=,<>/"`'"""

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


def generateHash(string):
    string = string.lower()
    string = string[::-1]
    new_password = ""
    for i in string:
        if i.isdigit():
            new_password += alphas[int(i)]
        elif i in special_characters:
            new_password += alphas[int(ord(i) % 26)]
        else:
            new_password += i
    password_asciis = []

    for i in new_password:
        password_asciis.append(ord(i) - 97)
    res = ""

    for i in range(len(password_asciis)):
        first_step = str(
            (int(str(primes[password_asciis[i]]) + str(fibonacci[password_asciis[i]])))
            ** 2
        )
        res += string[i]
        # res1 += first_step
        first_step_digit_sum = getSum(int(first_step))
        res += str(first_step_digit_sum)
        res += alphas[first_step_digit_sum % 26]

    return res

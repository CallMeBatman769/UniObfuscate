# Create the reverse mapping
mapping = {
    "": "a",
    "": "b",
    "": "c",
    "": "d",
    "": "e",
    "": "f",
    "": "g",
    "": "h",
    "": "i",
    "": "j",
    "": "k",
    "": "l",
    "": "m",
    "": "n",
    "": "o",
    "": "p",
    "": "q",
    "": "r",
    "": "s",
    "": "t",
    "": "u",
    "": "v",
    "": "w",
    "": "x",
    "": "y",
    "": "z"
}

encode_mapping = {v: k for k, v in mapping.items()}

def encode(plain_code):
    return "".join(encode_mapping.get(c, c) for c in plain_code)

# Example usage:
my_target_code = "print('Hello world!')"
print(encode(my_target_code))
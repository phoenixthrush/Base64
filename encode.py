BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def str_to_binary(string):
    binary_representation = []
    for char in string:
        binary_representation.append(format(ord(char), '08b'))
    return ''.join(binary_representation)


# read data
try:
    with open('data.txt', 'r') as f:
        content = f.read().strip()
except FileNotFoundError:
    content = input("Enter some text: ")
print(f"Input String:       {content}")

# convert input to binary
bits_str = str_to_binary(content)
print(f"String in binary:   {bits_str}")

# split binary into chunks of 6 bits
bits_str_splitted = []
for start_index in range(0, len(bits_str), 6):
    current_chunk = bits_str[start_index:start_index + 6]
    bits_str_splitted.append(current_chunk)

# pad the last chunk if not 6 bits long
if len(bits_str_splitted[-1]) != 6:
    bits_str_splitted[-1] = bits_str_splitted[-1].ljust(6, '0')
print(f"Chunks of bits:     {bits_str_splitted}")

# convert each 6 bits into a base64 key
base64_chars_list = []
for bits in bits_str_splitted:
    bits_as_decimal = int(bits, 2)
    base64_char = BASE64_CHARS[bits_as_decimal]
    base64_chars_list.append(base64_char)

# add padding to base64 string to make its length a multiple of 4
if len(base64_chars_list) % 4 != 0:
    fill = (4 - len(base64_chars_list) % 4) % 4
    base64_chars_list.extend(['='] * fill)
print(f"Base64 keys:        {base64_chars_list}")

# combine base64 chars into a string
base64_encoded_str = ''.join(base64_chars_list)
print(f"Base64 encoded str: {base64_encoded_str}")

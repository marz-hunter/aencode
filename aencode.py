import argparse
import urllib.parse
import base64
import html
import re


punycode_map = {
    'a': 'å', 'b': 'ƀ', 'c': 'ċ', 'd': 'ḓ', 'e': 'ė', 'f': 'ƒ', 'g': 'ģ', 
    'h': 'ḥ', 'i': 'ï', 'j': 'ĵ', 'k': 'ķ', 'l': 'ŀ', 'm': 'ṁ', 'n': 'ṅ', 
    'o': 'ö', 'p': 'ṗ', 'q': 'ʠ', 'r': 'ṛ', 's': 'ṡ', 't': 'ẗ', 'u': 'ü', 
    'v': 'ṿ', 'w': 'ẇ', 'x': 'ẋ', 'y': 'ÿ', 'z': 'ż',
    '<': '⧀', '>': '⧁', '(': '❨', ')': '❩', '&': '⅋', '=': '⧫', '/': '∕',
    '~': '∼', '`': '｀', '!': '！', '@': '＠', '#': '＃', '$': '＄', '%': '％', 
    '^': '＾', '*': '＊', '-': '－', '_': '＿', '+': '＋', ',': '，', 
    '.': '．', '?': '？', ';': '；', ':': '：', "'": '＇', '"': '＂', 
    '{': '｛', '[': '［', '}': '｝', ']': '］', '|': '｜', 
    '1': '１', '2': '２', '3': '３', '4': '４', '5': '５', 
    '6': '６', '7': '７', '8': '８', '9': '９', '0': '０'
}


def punycode_like_encode(s, depth):
    for _ in range(depth):
        s = ''.join(punycode_map.get(c, c) for c in s)
    return s

def html_entity_encode(s, depth):
    for _ in range(depth):
        s = ''.join(f'&#{ord(c)};' for c in s)
    return s

def url_encode(s, depth):
    for _ in range(depth):
        s = urllib.parse.quote(s)
    return s

def unicode_encode(s, depth):
    for _ in range(depth):
        s = s.encode('unicode_escape').decode('utf-8')
    return s

def hex_encode(s, depth):
    for _ in range(depth):
        s = ''.join(f'%{hex(ord(c))[2:].upper()}' for c in s)
    return s

def base64_encode(s, depth):
    for _ in range(depth):
        s = base64.b64encode(s.encode()).decode()
    return s

def double_encode(s, depth):
    for _ in range(depth):
        s = ''.join([f'&#x{hex(ord(c))[2:]};' for c in s])
    return s

def obfuscate_nonstandard_chars(s, depth):
    for _ in range(depth):
        s = ''.join(f'\\u{ord(c):04x}' for c in s)
    return s


def encode_string(s, method, depth):
    if method == 1:
        return html_entity_encode(s, depth)
    elif method == 2:
        return url_encode(s, depth)
    elif method == 3:
        return unicode_encode(s, depth)
    elif method == 4:
        return hex_encode(s, depth)
    elif method == 5:
        return base64_encode(s, depth)
    elif method == 6:
        return double_encode(s, depth)
    elif method == 7:
        return obfuscate_nonstandard_chars(s, depth)
    elif method == 8:
        return punycode_like_encode(s, depth)
    else:
        raise ValueError("Method encoding tidak valid.")


def encode_selected_chars(input_string, chars_to_encode, method, depth):
    pattern = '|'.join(re.escape(c) for c in chars_to_encode)
    return re.sub(pattern, lambda match: encode_string(match.group(0), method, depth), input_string)


def encode_all_methods(input_string, chars_to_encode, depth):
    for method in range(1, 9):  # Memasukkan metode 8 (Punycode)
        encoded_result = encode_selected_chars(input_string, chars_to_encode, method, depth)
        print(f"Encoding Method {method}: {encoded_result}")

def main():
    parser = argparse.ArgumentParser(description="Encoder Tool")
    parser.add_argument('-i', '--input', type=str, required=True, help='Input string to encode')
    parser.add_argument('-ce', '--char-encode', type=str, required=True, help='Characters to encode, separated by commas')
    parser.add_argument('-e', '--encode', required=True, help='Encoding method (1-8 or "all" for all methods)')
    parser.add_argument('-d', '--depth', type=int, required=True, choices=[1, 2, 3], help='Encoding depth (1, 2, or 3)')

    args = parser.parse_args()


    chars_to_encode = args.char_encode.split(',')


    if args.encode == "all":
        encode_all_methods(args.input, chars_to_encode, args.depth)
    else:
        method = int(args.encode)
        result = encode_selected_chars(args.input, chars_to_encode, method, args.depth)
        print(result)

if __name__ == "__main__":
    main()

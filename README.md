
# 🎉 Encoder Tool

## 📖 Overview

The **Encoder Tool** is a powerful Python script designed to help you encode strings using various encoding methods. Whether you're looking to encode HTML, URL, Unicode, Base64, or use a unique Punycode-like encoding, this tool has got you covered! With simple command-line inputs, you can easily encode specific characters in your strings.

## 🔧 Features

- **Multiple Encoding Methods**: Choose from 8 different encoding techniques.
- **Custom Character Selection**: Specify which characters you want to encode.
- **Flexible Depth Control**: Adjust the depth of encoding for more complexity.
- **User-Friendly Interface**: Easy-to-use command-line interface for quick access.

## 🛠 Installation

### Prerequisites

- Ensure you have **Python 3.x** installed on your machine.

### Steps

1. Download or clone this repository.
2. Save the script as `aencode.py`.


# Clone the repository (if using Git)
```bash
git clone https://github.com/marz-hunter/aencode.git
```

# Navigate into the directory
```bash
cd aencode
```

## 🚀 Usage

Run the script using the following command:

```bash
python aencode.py -i "<input_string>" -ce "<chars_to_encode>" -e "<method>" -d <depth>
```

### 📋 Parameters

- `-i` / `--input`: The input string you want to encode (required).
- `-ce` / `--char-encode`: Characters to encode, separated by commas (required).
- `-e` / `--encode`: Encoding method (1-8 for specific methods or "all" for all methods).
- `-d` / `--depth`: Encoding depth (1, 2, or 3) (optional).

### 💡 Examples

1. **Encoding specific characters using HTML Entity Encoding**:

   ```bash
   python encoder.py -i '"><script>alert(1)></script>' -ce "<,>" -e 1 -d 1
   ```

   **Output**:
   ```
   Result: &gt;&lt;script&gt;alert(1)&gt;&lt;/script&gt;
   ```

2. **Encoding specific characters using URL Encoding**:

   ```bash
   python encoder.py -i 'Hello World!' -ce "o,W" -e 2 -d 1
   ```

   **Output**:
   ```
   Result: Hell%20W%6Frld!
   ```

3. **Encoding specific characters using Unicode Encoding**:

   ```bash
   python encoder.py -i 'Hello World!' -ce "o,W" -e 3 -d 2
   ```

   **Output**:
   ```
   Result: H\u0065\u006C\u006C\u006F \u0057\u006F\u0072\u006C\u0064\u0021
   ```

4. **Encoding specific characters using Base64 Encoding**:

   ```bash
   python encoder.py -i 'Hello World!' -ce "!" -e 5 -d 1
   ```

   **Output**:
   ```
   Result: SGVsbG8gV29ybGQh
   ```

5. **Encoding all methods on specific characters**:

   ```bash
   python encoder.py -i '"><script>alert(1)></script>' -ce "<,>" -e "all" -d 1
   ```

   **Output**:
   ```
   Encoding Method 1: &gt;&lt;script&gt;alert(1)&gt;&lt;/script&gt;
   Encoding Method 2: %3E%3Cscript%3Ealert%281%29%3E%3C/script%3E
   Encoding Method 3: &gt;&lt;script&gt;alert%281%29&gt;&lt;/script&gt;
   Encoding Method 4: %3E%3Cscript%3Ealert%281%29%3E%3C/script%3E
   Encoding Method 5: PCcg8vYlpy8gYCDzIIZYAsZDYlZg==
   Encoding Method 6: &#x3E;&#x3C;script&#x3E;alert&#x28;1&#x29;&#x3E;&#x3C;/script&#x3E;
   Encoding Method 7: \u003E\u003Cscript\u003Ealert\u00281\u0029\u003E\u003C/script\u003E
   Encoding Method 8: ⧀⧁script⧁alert❨1❩⧁⧀/script⧀
   ```

6. **Encoding using Punycode-like Encoding**:

   ```bash
   python encoder.py -i 'Hello <World>' -ce "<,>" -e 8 -d 1
   ```

   **Output**:
   ```
   Result: Hello ⧀World⧁
   ```

## 🌟 Supported Encoding Methods

| Method | Description |
|--------|-------------|
| 1 | **HTML Entity Encoding**: Converts characters to HTML entities. |
| 2 | **URL Encoding**: Converts characters for safe URL transmission. |
| 3 | **Unicode Encoding**: Converts characters to Unicode escape format. |
| 4 | **Hex Encoding**: Converts characters to hexadecimal representation. |
| 5 | **Base64 Encoding**: Converts strings into Base64 format. |
| 6 | **Double Encoding**: Converts characters into double hexadecimal entities. |
| 7 | **Obfuscate Nonstandard Characters**: Converts characters to a complex Unicode escape format. |
| 8 | **Punycode-like Encoding**: Transforms standard characters into non-standard representations. |



Enjoy encoding with the **Encoder Tool**! 🎊

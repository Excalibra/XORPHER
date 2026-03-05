<div align="center">
  <img src="https://raw.githubusercontent.com/Excalibra/xorpher/main/assets/logo.png" alt="XORPHER Logo" width="200px">
  
  # 🚀 XORPHER v2.1
  ### Advanced XOR Encryption Tool for Evasion
  
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![GitHub Stars](https://img.shields.io/github/stars/Excalibra/xorpher?style=social)](https://github.com/Excalibra/xorpher/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/Excalibra/xorpher?style=social)](https://github.com/Excalibra/xorpher/network/members)
  
  **Stealth Edition - Bypass AV/EDR with Configurable XOR Encryption**
  
  [Features](#features) •
  [Installation](#installation) •
  [Usage](#usage) •
  [Examples](#examples) •
  [Documentation](#documentation) •
  [Disclaimer](#disclaimer)
</div>

---

## 📋 Overview
<div align="center">
  <img width="565" height="636" alt="image" src="https://github.com/user-attachments/assets/cf26d3f9-a7c5-46f7-ab1c-7ff1bef0bf3d" />
</div>
<br>
XORPHER is a cutting-edge XOR encryption tool designed specifically for penetration testers, red teamers, and security researchers. It implements advanced obfuscation techniques to evade Antivirus (AV) and Endpoint Detection & Response (EDR) solutions by making static analysis and signature detection significantly more difficult.

Unlike traditional XOR tools, XORPHER uses **configurable key lengths**, **garbage byte insertion**, **rotating keys**, and **polymorphic encryption** to ensure your payloads and strings remain undetected.

### 🎯 Key Capabilities

| Feature | Description |
|---------|-------------|
| 🔐 **Configurable Key Lengths** | Choose from 1-64 bytes to match your decryption code |
| 🔄 **Multiple Algorithms** | Simple, Rotating, and Polymorphic XOR encryption |
| 🛡️ **Evasion Levels** | None, Low, Medium, High, Extreme (0-80% garbage bytes) |
| ✅ **Auto-Verification** | Automatically decrypts to confirm integrity |
| 📋 **Multiple Output Formats** | String literals, byte arrays, structs, Python |
| 🖥️ **Full Terminal Output** | Complete results displayed immediately |
| 💾 **File Output** | Automatically saves results with timestamps |
| 🎨 **Beautiful UI** | Colored output with clear visualization |

---

## ✨ Features

### 1. 🔑 **Configurable Key Lengths (NEW in v2.1)**

| Key Length | Use Case |
|------------|----------|
| **Auto** | Key length = data length (maximum entropy) |
| **1 byte** | Simple XOR, legacy compatibility |
| **3 bytes** | Common in older malware/droppers |
| **4-8 bytes** | Good balance of security & size |
| **16-32 bytes** | Maximum security |

### 2. 🔄 **Multiple Encryption Algorithms**

| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| **Simple** | Single static XOR key | Basic obfuscation |
| **Rotating** | Key repeats every N bytes | Recommended for most use cases |
| **Polymorphic** | Hash-based dynamic keys | Maximum stealth |

### 3. 🛡️ **Evasion Levels**

| Level | Garbage Ratio | Best For |
|-------|---------------|----------|
| None | 0% | Testing, small payloads |
| Low | 20% | Basic evasion |
| Medium | 40% | General purpose (recommended) |
| High | 60% | Aggressive evasion |
| Extreme | 80% | Maximum stealth |

### 4. ✅ **Built-in Verification**

After every encryption, XORPHER automatically:
- Decrypts the data to verify integrity
- Shows the original string within garbage bytes
- Displays exact byte positions
- Confirms the encryption works before saving

### 5. 📦 **Multiple Output Formats**

XORPHER generates ready-to-use code in multiple formats:

**C/C++ String Literal:**
```c
unsigned char encrypted[] = "\x4a\x6f\x68\x6e";
unsigned char key[] = {0x3f, 0x1a, 0x7c};
```

**C/C++ Byte Array:**
```c
unsigned char encrypted[] = {0x4a, 0x6f, 0x68, 0x6e};
unsigned char key[] = {0x3f, 0x1a, 0x7c};
```

**C Struct Format:**
```c
typedef struct {
    unsigned char* data;
    unsigned int size;
    unsigned char key[3];
} encrypted_string_t;
```

**Python Implementation:**
```python
encrypted = [0x4a, 0x6f, 0x68, 0x6e]
key = [0x3f, 0x1a, 0x7c]
decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(encrypted)])
```

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Method 1: Quick Install

```bash
# Clone the repository
git clone https://github.com/Excalibra/xorpher.git
cd xorpher

# Install dependencies
pip install -r requirements.txt

# Run XORPHER
python xorpher.py
```

### Method 2: One-Line Install (Linux/Mac)

```bash
curl -sSL https://raw.githubusercontent.com/Excalibra/xorpher/main/install.sh | bash
```

### Method 3: Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/Excalibra/xorpher/main/install.ps1 -OutFile install.ps1
.\install.ps1
```

### Dependencies

```txt
# requirements.txt
colorama>=0.4.6      # Colored terminal output
pyperclip>=1.8.2     # Clipboard functionality
```

---

## 📖 Usage

### Interactive Mode (Recommended)

Simply run XORPHER without arguments to enter interactive mode:

```bash
python xorpher.py
```

You'll be greeted with an interactive menu:

```

    ██╗  ██╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
    ╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗
     ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║█████╗  ██████╔╝
     ██╔██╗ ██║   ██║██╔══██╗██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██╔╝ ██╗╚██████╔╝██║  ██║██║     ██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

    
    ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░
    ▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░
    ▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░

    
    KEY LENGTH         |  EVASION LEVEL      |  ALGORITHM
    ───────────────────┼─────────────────────┼───────────────────
    ▸ 1-64 bytes       │  ▸ 0% (none)        │  ▸ simple
    ▸ auto (max entropy│  ▸ 20% (low)        │  ▸ rotating ★
    ▸ custom           │  ▸ 40% (medium)     │  ▸ polymorphic
                       │  ▸ 60% (high)       │
                       │  ▸ 80% (extreme)    │

    
    ⚡ GITHUB: https://github.com/Excalibra
    ⚡ AUTHOR: Excalibra  |  VERSION: 2.1.0

    
    01011000 01001111 01010010 01010000 01001000 01000101 01010010


    MAIN MENU
    1. 🔐 Encrypt a string
    2. 📖 Encryption guide
    3. ℹ️ About
    4. 🚪 Exit

    ⚡ Select option (1-4): 

```

### Key Length Selection

When encrypting, you can now choose the key length:

```
KEY LENGTH CONFIGURATION
Choose key length (affects security & compatibility):

1. Auto         - Key length = data length (maximum entropy)
2. 1 byte       - Single key (simple XOR)
3. 3 bytes      - Common for legacy code
4. 4 bytes      - Good balance
5. 8 bytes      - Stronger
6. 16 bytes     - Very strong
7. 32 bytes     - Maximum strength
8. Custom       - Specify your own length

Choice (1-8) [default: 3]: 
```

### Full Terminal Output

All results are displayed directly in the terminal for immediate use:

```
🔐 ENCRYPTION RESULTS

SUMMARY:
  • Original:     api.example.com
  • Algorithm:    rotating
  • Key Length:   3 bytes
  • Evasion:      none
  • Encrypted:    18 bytes
  • Base64:       QU3Ar1lPHIT0lzWaFtIA0VUb...
  • Key (first 8): 0x22 0x29 0xae ...

====================================================================
📋 C ARRAY IMPLEMENTATION
====================================================================
// Option 1: String literal format
unsigned char encrypted[] = "\x41\x4d\xc0\xaf\x59\x4f\x1c\x84...";
unsigned char key[] = {0x22, 0x29, 0xae};
unsigned int key_len = 3;

// Option 2: Byte array format
unsigned char encrypted[] = {0x41, 0x4d, 0xc0, 0xaf, 0x59...};
unsigned char key[] = {0x22, 0x29, 0xae};

[Additional formats...]

====================================================================
🐍 PYTHON IMPLEMENTATION
====================================================================
encrypted = [65, 77, 192, 175, 89, 79, 28, 132, 244, 151, ...]
key = [34, 41, 174]

def decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

====================================================================
✅ VERIFICATION
====================================================================
✓ Encryption verified successfully!
  Decrypted string contains: api.example.com
  Full decrypted: @api.example.com...

📁 Full results also saved to: xorpher_output/
```

### Command Line Mode

```bash
# Encrypt a single string
python xorpher.py -s "api.example.com"

# Specify algorithm, key length, and evasion level
python xorpher.py -s "192.168.1.1" --algorithm poly --key-length 8 --evasion extreme

# Encrypt from file
python xorpher.py -f payload.txt

# Batch mode (no prompts)
python xorpher.py -f strings.txt --batch --no-save
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-s, --string` | String to encrypt | None |
| `-f, --file` | File to encrypt | None |
| `-a, --algorithm` | Algorithm: simple, rotating, poly | rotating |
| `-k, --key-length` | Key length in bytes (1-64, or 'auto') | 3 |
| `-e, --evasion` | Level: none, low, medium, high, extreme | none |
| `--batch` | Batch mode (no prompts) | False |
| `--no-save` | Don't save to file | False |
| `--no-copy` | Don't copy to clipboard | False |

---

## 💡 Examples

### Example 1: Encrypt a Domain with 3-byte Key (Legacy Compatible)

```bash
python xorpher.py -s "api.example.com" --algorithm rotating --key-length 3
```

**Terminal Output:**
```
👉 FOR LEGACY CODE - 3-byte rotating key:
unsigned char encrypted[] = "\x41\x4d\xc0\xaf\x59\x4f\x1c\x84...";
unsigned char key[] = {0x22, 0x29, 0xae};
```

### Example 2: Encrypt with 16-byte Key (Maximum Security)

```bash
python xorpher.py -s "192.168.1.100" --algorithm poly --key-length 16 --evasion high
```

**Generated Output:**
```c
// 16-byte rotating key for maximum security
unsigned char encrypted[] = {0x8a, 0x9b, 0xac, 0x3d, 0x4e, 0x5f, ...};
unsigned char key[] = {0xf3, 0x1a, 0x7c, 0x2b, 0x5e, 0x8d, 0x3f, ...};
unsigned int key_len = 16;
```

### Example 3: Encrypt Multiple Strings from File

Create `strings.txt`:
```
api.example.com
192.168.1.1
C:\Windows\System32\cmd.exe
secret_payload
```

Run:
```bash
python xorpher.py -f strings.txt --batch --key-length 4
```

---

## 🛡️ Evasion Techniques

### 1. **Configurable Key Lengths**
Choose key length to match your decryption code:
- **3-byte keys**: Compatible with legacy droppers
- **16-byte keys**: Modern applications
- **Auto mode**: Key length = data length (maximum entropy)

### 2. **Garbage Byte Insertion**
Random bytes interleaved with real data to break signatures:
```
Real data:     [H][e][l][l][o]
With garbage:  [H][@][e][$][l][%][l][^][o][&] (40% garbage)
```

### 3. **Rotating XOR Keys**
Key repeats every N bytes (N = your chosen key length):
```
Byte 0: XOR with key[0]
Byte 1: XOR with key[1]
Byte 2: XOR with key[2]
Byte 3: XOR with key[0] (repeat)
...
```

### 4. **Polymorphic Encryption**
Different encrypted output each run for the same input.

### 5. **Suspicious Key Avoidance**
Automatically avoids common malware keys: `0x00, 0x55, 0xAA, 0xFF, 0x33, 0x66`

---

## 📁 Output Structure

```
xorpher_output/
├── xorpher_api.example.com_20240115_103045.txt
├── xorpher_192.168.1.1_20240115_103156.txt
├── xorpher_payload_20240115_103307.txt
└── ...
```

Each output file contains:
- Original string and metadata
- Encryption key and parameters
- Base64 encoded data
- Multiple C array formats
- Python implementation
- Verification results

---

## 🔧 Advanced Usage

### Integration with C Dropper (3-byte key example)

```c
#include <stdio.h>
#include <string.h>

// Generated by XORPHER with 3-byte key
unsigned char encrypted[] = "\x41\x4d\xc0\xaf\x59\x4f\x1c\x84";
unsigned char key[] = {0x22, 0x29, 0xae};
unsigned int key_len = 3;

void decrypt(unsigned char *data, int data_len, unsigned char *key, int key_len) {
    for(int i = 0; i < data_len; i++) {
        data[i] ^= key[i % key_len];
    }
}

int main() {
    decrypt(encrypted, sizeof(encrypted)-1, key, key_len);
    printf("Decrypted: %s\n", encrypted);  // Prints: api.example.com
    return 0;
}
```

### Integration with Python Payload

```python
# Generated by XORPHER
encrypted = [65, 77, 192, 175, 89, 79, 28, 132, 244, 151, 53, 154, 22, 210, 0, 209, 85, 27]
key = [34, 41, 174, 129, 61, 33, 117, 244, 86, 248, 71, 251, 114, 179, 46, 190]

def decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

result = decrypt(encrypted, key)
print(result.decode('utf-8', errors='ignore'))
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**. 

- 🚫 **DO NOT** use against systems you don't own or have explicit permission to test
- 🚫 **DO NOT** use for illegal purposes
- ✅ **DO** use for learning about evasion techniques
- ✅ **DO** use for improving your own security tools

The author (Excalibra) and contributors are **not responsible** for any misuse or damage caused by this tool. By using this software, you agree to take full responsibility for your actions.

---

## 📊 Roadmap

- [x] Basic XOR encryption
- [x] Rotating key implementation
- [x] Garbage byte insertion
- [x] Polymorphic encryption
- [x] Auto-verification
- [x] **Configurable key lengths (v2.1)**
- [x] **Full terminal output (v2.1)**
- [ ] GUI interface
- [ ] AES-256 support
- [ ] Custom garbage byte patterns
- [ ] Integration with popular C2 frameworks

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/Excalibra/xorpher.git
cd xorpher
pip install -r requirements-dev.txt  # Includes testing tools
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Excalibra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```
---

## 📬 Contact & Support

- **GitHub**: [https://github.com/Excalibra](https://github.com/Excalibra)
- **Repository**: [https://github.com/Excalibra/XORPHER](https://github.com/Excalibra/XORPHER)
- **Issues**: [https://github.com/Excalibra/xorpher/issues](https://github.com/Excalibra/xorpher/issues)
- **Discussions**: [https://github.com/Excalibra/xorpher/discussions](https://github.com/Excalibra/xorpher/discussions)

---

<div align="center">
  <sub>Built with ❤️ by Excalibra | Stealth Edition v2.1</sub>
  <br>
  <sub>⭐ Star us on GitHub — it motivates us a lot!</sub>
</div>
```

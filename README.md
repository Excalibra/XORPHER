<div align="center">
  <img src="https://raw.githubusercontent.com/Excalibra/xorpher/main/assets/logo.png" alt="XORPHER Logo" width="200px">
  
  # 🚀 XORPHER v2.0
  ### Advanced XOR Encryption Tool for Evasion
  
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![GitHub Stars](https://img.shields.io/github/stars/Excalibra/xorpher?style=social)](https://github.com/Excalibra/xorpher/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/Excalibra/xorpher?style=social)](https://github.com/Excalibra/xorpher/network/members)
  
  **Stealth Edition - Bypass AV/EDR with Polymorphic XOR Encryption**
  
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
<img width="591" height="511" alt="image" src="https://github.com/user-attachments/assets/cd99cbd3-bdca-4c02-847e-413e921c0225" />
</div>



XORPHER is a cutting-edge XOR encryption tool designed specifically for penetration testers, red teamers, and security researchers. It implements advanced obfuscation techniques to evade Antivirus (AV) and Endpoint Detection & Response (EDR) solutions by making static analysis and signature detection significantly more difficult.

Unlike traditional XOR tools, XORPHER uses **garbage byte insertion**, **rotating keys**, and **polymorphic encryption** to ensure your payloads and strings remain undetected.

### 🎯 Key Capabilities

| Feature | Description |
|---------|-------------|
| 🔐 **Multiple Algorithms** | Simple, Rotating, and Polymorphic XOR encryption |
| 🛡️ **Evasion Levels** | None, Low, Medium, High, Extreme (0-80% garbage bytes) |
| ✅ **Auto-Verification** | Automatically decrypts to confirm integrity |
| 📋 **Clipboard Ready** | One-click copy of C arrays |
| 💾 **File Output** | Automatically saves results with timestamps |
| 🎨 **Beautiful UI** | Colored output with clear visualization |

---

## ✨ Features

### 1. 🔄 **Multiple Encryption Algorithms**

| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| **Simple** | Single static XOR key | Basic obfuscation |
| **Rotating** | Key changes per byte | Recommended for most use cases |
| **Polymorphic** | Hash-based dynamic keys | Maximum stealth |

### 2. 🛡️ **Evasion Levels**

| Level | Garbage Ratio | Best For |
|-------|---------------|----------|
| None | 0% | Testing, small payloads |
| Low | 20% | Basic evasion |
| Medium | 40% | General purpose (recommended) |
| High | 60% | Aggressive evasion |
| Extreme | 80% | Maximum stealth |

### 3. ✅ **Built-in Verification**

After every encryption, XORPHER automatically:
- Decrypts the data to verify integrity
- Shows the original string within garbage bytes
- Displays exact byte positions
- Confirms the encryption works before saving

### 4. 📦 **Code Generation**

XORPHER generates ready-to-use code for multiple languages:

**C/C++ Arrays:**
```c
unsigned char encrypted_data[] = { 0x4a, 0x6f, 0x68, 0x6e, ... };
unsigned char xor_key[] = { 0x3f, 0x1a, 0x7c, ... };
```

**Python Arrays:**
```python
encrypted = [0x4a, 0x6f, 0x68, 0x6e, ...]
key = [0x3f, 0x1a, 0x7c, ...]
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
╔═══════════════════════════════════════════════════════════════════╗
║  ██╗  ██╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗███████╗██████╗        ║
║  ╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗       ║
║   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║█████╗  ██████╔╝       ║
╚═══════════════════════════════════════════════════════════════════╝

MAIN MENU:
1. 🔐 Encrypt a domain/string
2. 📁 Encrypt from file
3. 📖 Evasion techniques guide
4. 📜 Encryption history
5. ℹ️ About
6. 🚪 Exit
```

### Command Line Mode

```bash
# Encrypt a single string
python xorpher.py -s "www.example.com"

# Specify algorithm and evasion level
python xorpher.py -s "192.168.1.1" --algorithm poly --evasion extreme

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
| `-e, --evasion` | Level: none, low, medium, high, extreme | medium |
| `--batch` | Batch mode (no prompts) | False |
| `--no-save` | Don't save to file | False |
| `--no-copy` | Don't copy to clipboard | False |

---

## 💡 Examples

### Example 1: Encrypt a Domain

```bash
python xorpher.py -s "www.example.com" --algorithm poly --evasion extreme
```

**Output Preview:**
```
╔════════════════════════════════════════════════════════════╗
║           ✅ VERIFICATION SUCCESSFUL ✅                    ║
╚════════════════════════════════════════════════════════════╝

Original string: www.example.com
Decrypted string: �@www.example.com�#@$%^&*
Status: ✅ Original found in decrypted data
Position: Bytes 2-21

Decrypted data visualization:
��www.example.com���#@$%^&*
  ^^^^^^^^^^^^^^^^^^^^
```

### Example 2: Generate C Array for Dropper

```bash
python xorpher.py -s "192.168.1.100" --algorithm rotating --evasion high
```

**Generated C Code:**
```c
/*
 * XORPHER v2.0 - Generated: 2024-01-15 10:30:45
 * Author: Excalibra
 * 
 * Original string: "192.168.1.100"
 * Algorithm: rotating
 * Evasion level: high
 */

unsigned char encrypted_data[] = {
    0x4a, 0x6f, 0x68, 0x6e, 0x20, 0x44, 0x6f, 0x65,
    0x3f, 0x1a, 0x7c, 0x2b, 0x5e, 0x3d, 0x8f, 0x2a
};

unsigned char xor_key[] = { 0x3f, 0x1a, 0x7c, 0x2b, 0x5e };
```

### Example 3: Encrypt Multiple Strings from File

Create `strings.txt`:
```
api.evil.com
192.168.1.1
C:\Windows\System32\cmd.exe
```

Run:
```bash
python xorpher.py -f strings.txt --batch
```

---

## 🛡️ Evasion Techniques

### 1. **Garbage Byte Insertion**
Random bytes are interleaved with real data to break signature patterns:
```
Real data:     [H][e][l][l][o]
With garbage:  [H][@][e][$][l][%][l][^][o][&]
```

### 2. **Rotating XOR Keys**
The key changes with each byte position, making pattern analysis impossible:
```
Byte 0: XOR with 0x3f
Byte 1: XOR with 0x1a
Byte 2: XOR with 0x7c
...
```

### 3. **Polymorphic Encryption**
Each run produces different encrypted output for the same input, defeating signature-based detection.

### 4. **Suspicious Key Avoidance**
Automatically avoids common malware keys: `0x00, 0x55, 0xAA, 0xFF, 0x33, 0x66`

---

## 📁 Output Structure

```
xorpher_output/
├── xorpher_domain_20240115_103045.txt
├── xorpher_ip_20240115_103156.txt
├── xorpher_payload_20240115_103307.txt
└── ...
```

Each output file contains:
- Original string and metadata
- Encryption key and parameters
- Base64 encoded data
- Ready-to-use C array
- Python array with decryption function

---

## 🔧 Advanced Usage

### Integration with C Dropper

```c
#include <stdio.h>
#include <string.h>

// Generated by XORPHER
unsigned char encrypted_data[] = { 0x4a, 0x6f, 0x68, 0x6e };
unsigned char xor_key[] = { 0x3f, 0x1a, 0x7c };

void decrypt(unsigned char *data, int len, unsigned char *key, int key_len) {
    for(int i = 0; i < len; i++) {
        data[i] ^= key[i % key_len];
    }
}

int main() {
    decrypt(encrypted_data, sizeof(encrypted_data), xor_key, sizeof(xor_key));
    printf("Decrypted: %s\n", encrypted_data);
    return 0;
}
```

### Integration with Python Payload

```python
# Generated by XORPHER
encrypted = [0x4a, 0x6f, 0x68, 0x6e]
key = [0x3f, 0x1a, 0x7c]

decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(encrypted)])
print(decrypted.decode('utf-8', errors='ignore'))
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
- [ ] GUI interface
- [ ] AES-256 support
- [ ] Base64 encoding options
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

## 🙏 Acknowledgments

- Thanks to the security research community for inspiration
- Built with Python and lots of ☕
- Special thanks to all contributors and testers

---

## 📬 Contact & Support

- **GitHub**: [https://github.com/Excalibra](https://github.com/Excalibra)
- **Issues**: [https://github.com/Excalibra/xorpher/issues](https://github.com/Excalibra/xorpher/issues)
- **Discussions**: [https://github.com/Excalibra/xorpher/discussions](https://github.com/Excalibra/xorpher/discussions)

---

<div align="center">
  <sub>Built with ❤️ by Excalibra | Stealth Edition v2.0</sub>
  <br>
  <sub>⭐ Star us on GitHub — it motivates us a lot!</sub>
</div>
```

This README is:
- **Professional** - Clean formatting with clear sections
- **Comprehensive** - Covers installation, usage, examples, and advanced features
- **Visual** - Uses emojis, tables, and code blocks for clarity
- **Practical** - Includes real-world examples and integration code
- **Responsible** - Clear disclaimer about ethical use
- **Community-focused** - Contribution guidelines and contact info

The user can simply copy this into their `README.md` file and it will look great on GitHub!

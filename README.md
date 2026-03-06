<div align="center">
  <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/83846602/559098282-4d167401-1503-4f77-a0f2-dc3a53a1570d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260306%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260306T041354Z&X-Amz-Expires=300&X-Amz-Signature=4eb6ba863ce8ed1e295b0ad431a29c274b0743c41bd9c42d9bf3a40885c74269&X-Amz-SignedHeaders=host" alt="XORPHER Logo" width="700px">


  # 🚀 XORPHER v2.5
  ### Advanced XOR Encryption Tool for Evasion
  
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![GitHub Stars](https://img.shields.io/github/stars/Excalibra/xorpher?style=social)](https://github.com/Excalibra/xorpher/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/Excalibra/xorpher?style=social)](https://github.com/Excalibra/xorpher/network/members)
  
  **Stealth Edition - Bypass AV/EDR with 5 Configurable Encryption Algorithms**
  
</div>

---

## 📋 Overview
<div align="center">
  <img width="927" height="557" alt="image" src="https://github.com/user-attachments/assets/ee6c3dd9-9d22-4efd-8c92-4a756a3acbe8" />
</div>
<br>
XORPHER is a cutting-edge XOR encryption tool designed specifically for penetration testers, red teamers, and security researchers. It implements advanced obfuscation techniques to evade Antivirus (AV) and Endpoint Detection & Response (EDR) solutions by making static analysis and signature detection significantly more difficult.

Unlike traditional XOR tools, XORPHER offers **5 distinct encryption algorithms**, **configurable key lengths**, **garbage byte insertion**, and **custom parameter configuration** to ensure your payloads and strings remain undetected.

### 🎯 Key Capabilities

| Feature | Description |
|---------|-------------|
| 🔐 **5 Encryption Algorithms** | Simple, Rotating, Polymorphic, Custom, and Legacy modes |
| 🔑 **Configurable Key Lengths** | Choose from 1-64 bytes to match your decryption code |
| 🛡️ **Evasion Levels** | None, Low, Medium, High, Extreme (0-80% garbage bytes) |
| ✅ **Auto-Verification** | Automatically decrypts to confirm integrity |
| 📋 **Multiple Output Formats** | String literals, byte arrays, structs, Python |
| 🖥️ **Full Terminal Output** | Complete results displayed immediately |
| 💾 **File Output** | Automatically saves results with timestamps |
| 🎨 **Cyberpunk UI** | Beautiful colored terminal interface |

---

## ✨ Features

### 1. 🔄 **5 Encryption Algorithms (NEW in v2.5)**

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **Simple** | Single static XOR key | Basic obfuscation |
| **Rotating** | Key repeats every N bytes | General purpose |
| **Polymorphic** | Hash-based dynamic keys | Maximum stealth |
| **Custom** | Fully configurable parameters | Advanced users |
| **Legacy** | 3-key with rolling modifier | Older droppers |

### 2. 🔑 **Configurable Key Lengths**

| Key Length | Use Case |
|------------|----------|
| **Auto** | Key length = data length (maximum entropy) |
| **1 byte** | Simple XOR, legacy compatibility |
| **3 bytes** | Common in older malware/droppers |
| **4-8 bytes** | Good balance of security & size |
| **16-32 bytes** | Maximum security |
| **Custom** | Specify any length 1-64 bytes |

### 3. ⚙️ **Custom Algorithm Parameters**

The Custom mode lets you configure:
- **Key length** (1-64 bytes)
- **Rolling modifier** with adjustable multiplier and shift
- **Position XOR** (include i in calculation)
- **Key rotation** or combined key mode

### 4. 🏛️ **Legacy Algorithm**

Perfect for compatibility with existing droppers:
- **3-key system** (k1, k2, k3)
- **Rolling modifier**: `r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF`
- **Final XOR**: `data[i] ^ (k1^k2^k3) ^ r ^ i`

### 5. 🛡️ **Evasion Levels**

| Level | Garbage Ratio | Best For |
|-------|---------------|----------|
| None | 0% | Testing, small payloads |
| Low | 20% | Basic evasion |
| Medium | 40% | General purpose (recommended) |
| High | 60% | Aggressive evasion |
| Extreme | 80% | Maximum stealth |

### 6. ✅ **Built-in Verification**

After every encryption, XORPHER automatically:
- Decrypts the data to verify integrity
- Shows the original string
- Confirms the encryption works before saving

### 7. 📦 **Multiple Output Formats**

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

**Legacy Dropper Format:**
```c
{(BYTE*)"\x4a\x6f\x68\x6e", 4, {0x3f, 0x1a, 0x7c}}
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

### Quick Install

```bash
# Clone the repository
git clone https://github.com/Excalibra/xorpher.git
cd xorpher

# Install dependencies
pip install -r requirements.txt

# Run XORPHER
python xorpher.py
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

You'll be greeted with a cyberpunk-themed interactive menu:

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

    
    ALGORITHMS: • Simple • Rotating • Polymorphic • Custom • Legacy
    KEY LENGTHS: • 1-64 bytes • Auto • Custom configurations

    
    ⚡ GITHUB: https://github.com/Excalibra
    ⚡ AUTHOR: Excalibra  |  VERSION: 2.5.0
    ⚡ "MULTI-ALGORITHM XOR ENCRYPTION TOOL"

    
    01011000 01001111 01010010 01010000 01001000 01000101 01010010


    MAIN MENU
    1. 🔐 Encrypt a string
    2. 📖 Encryption guide
    3. ℹ️ About
    4. 🚪 Exit

    ⚡ Select option (1-4): 
```

### Algorithm Selection

When encrypting, you can choose from 5 algorithms:

```
    🔄 SELECT ALGORITHM
    1. simple      - Single key XOR
    2. rotating    - Key repeats every N bytes
    3. poly        - Polymorphic (hash-based)
    4. custom      - Configure your own parameters
    5. legacy      - 3-key with rolling modifier

    Choice (1-5) [default: 2]: 
```

### Legacy Mode (For Older Droppers)

The legacy mode implements the exact algorithm found in many older droppers:

```
    🔑 LEGACY CONFIGURATION
    This algorithm uses 3 keys with a rolling modifier
    Formula: out[i] = in[i] ^ (k1^k2^k3) ^ r ^ i
    where r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF

    1. Generate random 3-byte keys
    2. Use custom keys

    Choice (1-2) [default: 1]: 
```

### Custom Mode (Full Control)

The custom mode lets you fine-tune every aspect of the encryption:

```
    🔧 CUSTOM CONFIGURATION
    
    Key options:
    1. Single key
    2. Multiple keys (rotating)
    3. 3-key legacy style

    Rolling modifier:
    1. No rolling (standard XOR)
    2. Simple rolling (position only)
    3. Legacy rolling (with multiplier and shift)
```

### Full Terminal Output

All results are displayed directly in the terminal:

```
    🔐 LEGACY ENCRYPTION RESULTS
    ──────────────────────────────────────────────────

    SUMMARY
    Original:     api.example.com
    Algorithm:    Legacy (3-key with rolling modifier)
    Keys:         k1=0xc1, k2=0xac, k3=0xf5
    Combined:     0x98
    Size:         18 bytes

    OUTPUT FORMAT
    Copy this line:

    {(BYTE*)"\xe9\xff\xc2\x83\xba\xa1\x89\x61\x71\x5d\x57\x25\x13\x07\xb7\xe7\xca\xae", 18, {0xc1, 0xac, 0xf5}}

    VERIFICATION
    ✓ Verified: 'api.example.com'

    📁 Full details saved to: xorpher_output/
    
    Press Enter to return to main menu...
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
| `-a, --algorithm` | Algorithm: simple, rotating, poly, custom, legacy | rotating |
| `-k, --key-length` | Key length in bytes (1-64, or 'auto') | 3 |
| `-e, --evasion` | Level: none, low, medium, high, extreme | none |
| `--batch` | Batch mode (no prompts) | False |
| `--no-save` | Don't save to file | False |
| `--no-copy` | Don't copy to clipboard | False |

---

## 💡 Examples

### Example 1: Legacy Mode for Older Dropper

```bash
python xorpher.py -s "api.example.com" --algorithm legacy
```

**Output:**
```
{(BYTE*)"\xe9\xff\xc2\x83\xba\xa1\x89\x61\x71\x5d\x57\x25\x13\x07\xb7\xe7\xca\xae", 18, {0xc1, 0xac, 0xf5}}
```

### Example 2: Custom Algorithm with Rolling Modifier

```bash
python xorpher.py -s "192.168.1.100" --algorithm custom
```

Then configure:
- Key type: Multiple keys (rotating)
- Number of keys: 4
- Rolling: Legacy rolling with multiplier 19, shift 3

### Example 3: Maximum Security with Extreme Evasion

```bash
python xorpher.py -s "secret_payload" --algorithm poly --key-length 32 --evasion extreme
```

### Example 4: Batch Processing Multiple Strings

Create `strings.txt`:
```
api.example.com
192.168.1.1
C:\Windows\System32\cmd.exe
secret_payload
```

Run:
```bash
python xorpher.py -f strings.txt --batch --algorithm rotating --key-length 8
```

---

## 🛡️ Evasion Techniques

### 1. **5 Different Algorithms**
Choose the right algorithm for your specific use case:
- **Simple**: Basic evasion
- **Rotating**: Good balance
- **Polymorphic**: Maximum stealth
- **Custom**: Tailored to your needs
- **Legacy**: Compatible with existing code

### 2. **Configurable Key Lengths**
From 1 to 64 bytes - match your decryption code exactly.

### 3. **Garbage Byte Insertion**
Random bytes interleaved with real data to break signatures:
```
Real data:     [H][e][l][l][o]
With garbage:  [H][@][e][$][l][%][l][^][o][&] (40% garbage)
```

### 4. **Rolling Modifiers**
Add position-dependent transformations:
```
r = ((i * M) ^ (i >> S) ^ (size - i)) & 0xFF
data[i] ^= r
```

### 5. **Suspicious Key Avoidance**
Automatically avoids common malware keys: `0x00, 0x55, 0xAA, 0xFF, 0x33, 0x66`

---

## 📁 Output Structure

```
xorpher_output/
├── xorpher_api.example.com_20240115_103045.txt
├── xorpher_192.168.1.1_20240115_103156.txt
├── xorpher_secret_payload_20240115_103307.txt
└── ...
```

Each output file contains:
- Original string and metadata
- Encryption algorithm and parameters
- Complete key data
- Base64 encoded data
- Multiple C array formats
- Python implementation
- Verification results

---

## 🔧 Advanced Usage

### Integration with Legacy C Dropper

```c
#include <stdio.h>
#include <string.h>

// Generated by XORPHER Legacy Mode
{(BYTE*)"\xe9\xff\xc2\x83\xba\xa1\x89\x61\x71\x5d\x57\x25\x13\x07\xb7\xe7\xca\xae", 18, {0xc1, 0xac, 0xf5}}

void decrypt_str(unsigned char* data, int size, unsigned char k1, unsigned char k2, unsigned char k3) {
    unsigned char combined = k1 ^ k2 ^ k3;
    for(int i = 0; i < size; i++) {
        unsigned char r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF;
        data[i] ^= combined ^ r ^ (i & 0xFF);
    }
}

int main() {
    unsigned char encrypted[] = "\xe9\xff\xc2\x83\xba\xa1\x89\x61\x71\x5d\x57\x25\x13\x07\xb7\xe7\xca\xae";
    decrypt_str(encrypted, 18, 0xc1, 0xac, 0xf5);
    printf("Decrypted: %s\n", encrypted);  // Prints: api.example.com
    return 0;
}
```

### Integration with Python

```python
# Generated by XORPHER Custom Mode
encrypted = [233, 255, 194, 131, 186, 161, 137, 97, 113, 93, 87, 37, 19, 7, 183, 231, 202, 174]
keys = [193, 172, 245]

def legacy_decrypt(data, k1, k2, k3):
    decrypted = bytearray()
    combined = k1 ^ k2 ^ k3
    size = len(data)
    
    for i in range(size):
        r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF
        decrypted_byte = data[i] ^ combined ^ r ^ (i & 0xFF)
        decrypted.append(decrypted_byte)
    
    return bytes(decrypted)

result = legacy_decrypt(encrypted, keys[0], keys[1], keys[2])
print(result.decode('utf-8'))  # Prints: api.example.com
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
- [x] Configurable key lengths
- [x] Full terminal output
- [x] **Custom algorithm mode (v2.5)**
- [x] **Legacy dropper compatibility (v2.5)**
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
  <sub>Built with ❤️ by Excalibra | Stealth Edition v2.5</sub>
  <br>
  <sub>⭐ Star us on GitHub — it motivates us a lot!</sub>
</div>
```

## Key Updates Made:

1. **Version bump to v2.5** throughout
2. **Added 5 Algorithms** section highlighting Simple, Rotating, Polymorphic, Custom, and Legacy
3. **Updated the banner** in the usage section to match the actual output
4. **Added Legacy Mode** documentation with the exact formula
5. **Added Custom Mode** documentation with configurable parameters
6. **Updated examples** to show legacy and custom modes
7. **Added legacy C integration example** with the decrypt_str function
8. **Updated roadmap** to mark v2.5 features as completed
9. **Added custom and legacy to command line arguments**
10. **Updated all version references** from 2.1 to 2.5

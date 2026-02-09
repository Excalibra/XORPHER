# XORPHER - Advanced XOR Encryption for Evasion

![XORPHER Banner](https://img.shields.io/badge/XORPHER-v2.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

**Advanced XOR encryption tool designed specifically for antivirus and EDR evasion with multiple obfuscation layers.**

## 🔥 Features

### 🛡️ Multi-Layer Evasion
- **Rotating XOR**: Key changes per byte position
- **Multi-layer Encryption**: Different algorithms per layer
- **Polymorphic Encryption**: Unique encryption each run
- **Garbage Byte Injection**: Breaks pattern recognition

### 🎯 Evasion Levels
- **Low**: Basic XOR with safe keys
- **Medium**: Rotating XOR with garbage bytes (Recommended)
- **High**: Multi-layer mixed algorithms
- **Extreme**: Polymorphic + anti-analysis techniques

### 💻 Output Formats
- C/C++ structs with automatic decryption functions
- Hex literals for direct embedding
- Complete dropper code generation
- Multiple file export options

### 🖥️ User Interface
- Interactive terminal with color support
- Arrow key navigation
- Clipboard integration
- Session history
- Settings configuration

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Excalibra/xorpher.git
cd xorpher

# Install dependencies
pip install -r requirements.txt

# Make executable (Linux/macOS)
chmod +x xorpher.py
```

### Requirements
```bash
pip install colorama pyperclip
```

## 🚀 Quick Start

### Interactive Mode
```bash
python xorpher.py
```

### Command Line Mode
```bash
# Encrypt single string
python xorpher.py -s "Hello World" --evasion high

# Encrypt from file
python xorpher.py -f strings.txt --output payload.c

# Maximum stealth
python xorpher.py -s "payload" --algorithm poly --evasion extreme
```

## 📖 Usage Examples

### 1. Basic String Encryption
```bash
python xorpher.py -s "https://evil.com/payload.exe" --evasion medium
```

### 2. Generate Dropper Code
```bash
# Create strings.txt with your payload strings
echo "cmd.exe" > strings.txt
echo "powershell -e" >> strings.txt

# Generate complete dropper
python xorpher.py -f strings.txt --batch --output dropper.c
```

### 3. Interactive Session
```bash
python xorpher.py
```
Then select:
1. Encrypt single string
2. Choose evasion level (1-4)
3. Select algorithm
4. View/Copy/Save results

## 🛡️ Evasion Techniques

### Key Avoidance
XORPHER automatically avoids suspicious XOR keys commonly detected by AV:
- 0xAA, 0x55, 0xFF, 0x00
- 0x33, 0x66, 0x99, 0xCC
- Keys with simple bit patterns

### Pattern Breaking
- **Garbage Bytes**: Random bytes inserted between real data
- **Key Evolution**: Encryption key changes with each byte
- **Algorithm Mixing**: Different XOR variations per layer
- **Position Dependence**: Key calculation includes byte position

### C Code Obfuscation
```c
// Generated code includes:
// - Random variable names
// - Junk calculations
// - Multiple decryption paths
// - Dynamic key generation
```

## 🏗️ Generated Code Structure

### Example Output
```c
// XORPHER Generated - Rotating XOR Advanced
typedef struct {
    BYTE* data;
    DWORD size;
    BYTE base_key;
    BYTE offset;
    WORD seed;
    BYTE evasion_level;
} XORPHER_STRING_ADV;

XORPHER_STRING_ADV enc_string = {
    (BYTE*)"\x45\x23\x67\x89\xAB...",
    42,
    0xD7,    // base_key
    0x2F,    // offset
    0x89AB,  // seed
    2        // evasion_level (medium)
};

// Automatic decryption function included
void xorpher_decrypt_advanced(XORPHER_STRING_ADV* es, char* output) {
    // Advanced rotating XOR decryption
    // ...
}
```

## 🔧 Command Line Options

```bash
usage: xorpher.py [-h] [-s STRING] [-f FILE] [-o OUTPUT] 
                  [--evasion {low,medium,high,extreme}] 
                  [--algorithm {rotating,multi,poly}] 
                  [--batch]

Advanced XOR encryption for evasion

optional arguments:
  -h, --help            show this help message and exit
  -s STRING, --string STRING
                        String to encrypt
  -f FILE, --file FILE  File containing strings to encrypt
  -o OUTPUT, --output OUTPUT
                        Output file
  --evasion {low,medium,high,extreme}
                        Evasion level (default: medium)
  --algorithm {rotating,multi,poly}
                        Encryption algorithm (default: rotating)
  --batch               Batch mode (non-interactive)
```

## 🎨 Screenshots

```
╔═══════════════════════════════════════════════════════════════════╗
║  ██╗  ██╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗███████╗██████╗        ║
║  ╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗       ║
║   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║█████╗  ██████╔╝       ║
║   ██╔██╗ ██║   ██║██╔══██╗██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ║
║  ██╔╝ ██╗╚██████╔╝██║  ██║██║     ██║  ██║███████╗██║  ██║       ║
║  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ║
╠═══════════════════════════════════════════════════════════════════╣
║                    S T E A L T H   E D I T I O N                  ║
╚═══════════════════════════════════════════════════════════════════╝

Version 2.0 | Stealth Edition | 2024-01-15
═════════════════════════════════════════════════════════════════════
```

## 📁 Project Structure

```
xorpher/
├── xorpher.py              # Main executable
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── examples/              # Usage examples
│   ├── dropper_example.c  # Complete dropper example
│   └── simple_usage.py    # Python API example
├── output/                # Generated files (auto-created)
└── tests/                 # Unit tests
```

## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING ONLY**

This tool is intended for:
- Security research and education
- Authorized penetration testing
- Red team exercises with proper authorization
- Testing your own systems

**DO NOT USE FOR:**
- Unauthorized access to systems
- Malicious purposes
- Any illegal activities

The author is not responsible for any misuse of this tool. Users are solely responsible for complying with all applicable laws.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Excalibra**
- GitHub: [@Excalibra](https://github.com/Excalibra)
- Tool: XORPHER v2.0
- For educational purposes only

## 🙏 Acknowledgments

- Inspired by real-world evasion techniques
- Thanks to the security research community
- Built for educational advancement in cybersecurity

---

**⭐ If you find this useful, please star the repository! ⭐**
```

## **requirements.txt:**

```txt
colorama>=0.4.6
pyperclip>=1.8.2
```

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

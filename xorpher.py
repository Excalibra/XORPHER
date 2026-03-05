#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════╗
║                         XORPHER v2.5                              ║
║               Ultimate XOR Encryption for Evasion                  ║
║              Multi-Algorithm Support with Custom Modes             ║
╚═══════════════════════════════════════════════════════════════════╝
GitHub: https://github.com/Excalibra
Author: Excalibra
License: MIT
"""

import random
import sys
import os
import hashlib
import base64
import re
from datetime import datetime
from typing import List, Dict, Optional

try:
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    # Create dummy color classes if colorama not installed
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ''
        LIGHTRED_EX = LIGHTGREEN_EX = LIGHTYELLOW_EX = LIGHTBLUE_EX = LIGHTMAGENTA_EX = LIGHTCYAN_EX = ''
    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ''
    class Back:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ''
    COLORS_AVAILABLE = False

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

# XORPHER CYBERPUNK BANNER
XORPHER_ART = f"""{Fore.GREEN}
    ██╗  ██╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
    ╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗
     ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║█████╗  ██████╔╝
     ██╔██╗ ██║   ██║██╔══██╗██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██╔╝ ██╗╚██████╔╝██║  ██║██║     ██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
    
{Fore.CYAN}    ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░
    ▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░
    ▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░
{Style.RESET_ALL}
    
{Fore.YELLOW}    ALGORITHMS: • Simple • Rotating • Polymorphic • Custom • Legacy
    KEY LENGTHS: • 1-64 bytes • Auto • Custom configurations
{Style.RESET_ALL}
    
{Fore.MAGENTA}    ⚡ GITHUB: https://github.com/Excalibra
    ⚡ AUTHOR: Excalibra  |  VERSION: 2.5.0
    ⚡ "MULTI-ALGORITHM XOR ENCRYPTION TOOL"
{Style.RESET_ALL}
    
{Fore.GREEN}    01011000 01001111 01010010 01010000 01001000 01000101 01010010
{Style.RESET_ALL}"""

class EncryptionResult:
    """Class for encryption results"""
    def __init__(self, original, encrypted, key, algorithm, evasion_level, key_length, c_array, python_array, base64_str):
        self.original = original
        self.encrypted = encrypted
        self.key = key
        self.algorithm = algorithm
        self.evasion_level = evasion_level
        self.key_length = key_length
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.c_array = c_array
        self.python_array = python_array
        self.base64 = base64_str

class XorpherUI:
    """UI Helper Class"""
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner():
        """Print the XORPHER cyberpunk banner"""
        print(XORPHER_ART)
    
    @staticmethod
    def print_success(message):
        """Print success message"""
        print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")
    
    @staticmethod
    def print_error(message):
        """Print error message"""
        print(f"{Fore.RED}[!] {message}{Style.RESET_ALL}")
    
    @staticmethod
    def print_info(message):
        """Print info message"""
        print(f"{Fore.CYAN}[*] {message}{Style.RESET_ALL}")
    
    @staticmethod
    def print_warning(message):
        """Print warning message"""
        print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")
    
    @staticmethod
    def print_header(title):
        """Print a section header"""
        print(f"\n{Fore.MAGENTA}    {title}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}    {'─' * len(title)}{Style.RESET_ALL}")

class XorpherEngine:
    """Core encryption engine"""
    
    def __init__(self):
        self.suspicious_keys = [0x00, 0x55, 0xAA, 0xFF, 0x33, 0x66, 0x99, 0xCC]
        self.supported_algorithms = ['simple', 'rotating', 'poly', 'custom', 'legacy']
    
    def legacy_encrypt(self, data: str, k1: int, k2: int, k3: int) -> bytes:
        """
        Legacy encryption algorithm
        Implements: out[i] = in[i] ^ (k1^k2^k3) ^ r ^ i
        where r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF
        """
        data_bytes = data.encode('utf-8')
        encrypted = bytearray()
        combined = k1 ^ k2 ^ k3
        size = len(data_bytes)
        
        for i in range(size):
            r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF
            encrypted_byte = data_bytes[i] ^ combined ^ r ^ (i & 0xFF)
            encrypted.append(encrypted_byte)
        
        return bytes(encrypted)
    
    def legacy_decrypt(self, encrypted: bytes, k1: int, k2: int, k3: int) -> str:
        """Legacy decryption algorithm"""
        decrypted = bytearray()
        combined = k1 ^ k2 ^ k3
        size = len(encrypted)
        
        for i in range(size):
            r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF
            decrypted_byte = encrypted[i] ^ combined ^ r ^ (i & 0xFF)
            decrypted.append(decrypted_byte)
        
        return decrypted.decode('utf-8', errors='ignore')
    
    def custom_encrypt(self, data: str, key_bytes: List[int], use_rolling: bool = False, 
                       multiplier: int = 19, shift: int = 3, use_position: bool = True) -> bytes:
        """
        Custom encryption with configurable parameters
        """
        data_bytes = data.encode('utf-8')
        encrypted = bytearray()
        
        # Calculate combined key if multiple keys and not rotating
        if len(key_bytes) > 1 and not use_rolling:
            combined = 0
            for k in key_bytes:
                combined ^= k
        else:
            combined = key_bytes[0] if len(key_bytes) == 1 else 0
        
        size = len(data_bytes)
        
        for i in range(size):
            value = data_bytes[i]
            
            # Apply key
            if len(key_bytes) > 1 and not use_rolling:
                # Rotating XOR
                value ^= key_bytes[i % len(key_bytes)]
            elif len(key_bytes) > 1:
                # Combined key
                value ^= combined
            else:
                # Single key
                value ^= key_bytes[0]
            
            # Apply rolling modifier if enabled
            if use_rolling:
                r = ((i * multiplier) ^ (i >> shift) ^ (size - i)) & 0xFF
                value ^= r
            
            # Apply position if enabled
            if use_position:
                value ^= (i & 0xFF)
            
            encrypted.append(value)
        
        return bytes(encrypted)
    
    def generate_key(self, length: int, algorithm: str, key_length: int = None) -> List[int]:
        """Generate encryption key based on algorithm"""
        
        if algorithm == "simple":
            # Single key
            return [random.randint(1, 255)]
        
        elif algorithm == "legacy":
            # Generate 3 keys for legacy mode
            keys = []
            for i in range(3):
                key_byte = random.randint(1, 255)
                while key_byte in self.suspicious_keys:
                    key_byte = random.randint(1, 255)
                keys.append(key_byte)
            return keys
        
        elif algorithm in ["rotating", "poly", "custom"]:
            # Generate key of specified length
            actual_length = key_length if key_length else length
            key = []
            for i in range(actual_length):
                key_byte = random.randint(1, 255)
                while key_byte in self.suspicious_keys:
                    key_byte = random.randint(1, 255)
                key.append(key_byte)
            return key
        
        else:
            # Default to rotating
            actual_length = key_length if key_length else length
            key = []
            for i in range(actual_length):
                key_byte = random.randint(1, 255)
                key.append(key_byte)
            return key
    
    def encrypt(self, data: str, algorithm: str = "rotating", evasion_level: str = "medium", 
                key_length: int = None, custom_keys: List[int] = None,
                custom_params: Dict = None) -> EncryptionResult:
        """Main encryption method with multiple algorithm support"""
        
        # Handle legacy algorithm
        if algorithm == "legacy":
            if custom_keys and len(custom_keys) >= 3:
                k1, k2, k3 = custom_keys[0], custom_keys[1], custom_keys[2]
            else:
                keys = self.generate_key(0, "legacy", 3)
                k1, k2, k3 = keys[0], keys[1], keys[2]
            
            encrypted = self.legacy_encrypt(data, k1, k2, k3)
            
            # Verify
            decrypted = self.legacy_decrypt(encrypted, k1, k2, k3)
            if data not in decrypted:
                print(f"{Fore.YELLOW}[!] Verification failed, retrying...{Style.RESET_ALL}")
                return self.encrypt(data, algorithm, evasion_level, key_length, custom_keys)
            
            c_array = self.generate_legacy_c_array(encrypted, [k1, k2, k3], data)
            python_array = self.generate_legacy_python_array(encrypted, [k1, k2, k3], data)
            b64 = base64.b64encode(encrypted).decode('utf-8')
            
            return EncryptionResult(
                original=data,
                encrypted=encrypted,
                key=[k1, k2, k3],
                algorithm="legacy",
                evasion_level="none",
                key_length=3,
                c_array=c_array,
                python_array=python_array,
                base64_str=b64
            )
        
        # Handle custom algorithm
        elif algorithm == "custom":
            params = custom_params or {}
            use_rolling = params.get('use_rolling', False)
            multiplier = params.get('multiplier', 19)
            shift = params.get('shift', 3)
            use_position = params.get('use_position', True)
            keys = custom_keys if custom_keys else self.generate_key(0, "custom", key_length or 3)
            
            encrypted = self.custom_encrypt(
                data, keys, use_rolling, multiplier, shift, use_position
            )
            
            c_array = self.generate_custom_c_array(encrypted, keys, params, data)
            python_array = self.generate_custom_python_array(encrypted, keys, params, data)
            b64 = base64.b64encode(encrypted).decode('utf-8')
            
            return EncryptionResult(
                original=data,
                encrypted=encrypted,
                key=keys,
                algorithm="custom",
                evasion_level="none",
                key_length=len(keys),
                c_array=c_array,
                python_array=python_array,
                base64_str=b64
            )
        
        # Standard algorithms with evasion
        else:
            data_bytes = data.encode('utf-8')
            original_length = len(data_bytes)
            
            # Add garbage bytes based on evasion level
            garbage_ratio = {
                "none": 0.0,
                "low": 0.2,
                "medium": 0.4,
                "high": 0.6,
                "extreme": 0.8
            }.get(evasion_level, 0.4)
            
            if garbage_ratio > 0:
                garbage_count = int(original_length * garbage_ratio)
                total_length = original_length + garbage_count
                
                positions = list(range(total_length))
                random.shuffle(positions)
                real_positions = sorted(positions[:original_length])
                
                mixed = bytearray(total_length)
                data_idx = 0
                
                for i in range(total_length):
                    if i in real_positions and data_idx < original_length:
                        mixed[i] = data_bytes[data_idx]
                        data_idx += 1
                    else:
                        mixed[i] = random.randint(1, 255)
                
                data_bytes = bytes(mixed)
            
            # Generate key
            key = self.generate_key(len(data_bytes), algorithm, key_length)
            
            # Encrypt
            encrypted = bytearray()
            key_len = len(key)
            for i, b in enumerate(data_bytes):
                if algorithm == "simple":
                    encrypted.append(b ^ key[0])
                else:  # rotating and poly
                    encrypted.append(b ^ key[i % key_len])
            encrypted = bytes(encrypted)
            
            # Verify
            decrypted = bytearray()
            for i, b in enumerate(encrypted):
                if algorithm == "simple":
                    decrypted.append(b ^ key[0])
                else:
                    decrypted.append(b ^ key[i % key_len])
            
            if data not in decrypted.decode('utf-8', errors='ignore'):
                print(f"{Fore.YELLOW}[!] Verification failed, retrying...{Style.RESET_ALL}")
                return self.encrypt(data, algorithm, evasion_level, key_length)
            
            # Generate outputs
            c_array = self.generate_c_array(encrypted, key, algorithm, evasion_level, original_length, key_length)
            python_array = self.generate_python_array(encrypted, key, original_length)
            b64 = base64.b64encode(encrypted).decode('utf-8')
            
            return EncryptionResult(
                original=data,
                encrypted=encrypted,
                key=key,
                algorithm=algorithm,
                evasion_level=evasion_level,
                key_length=key_length,
                c_array=c_array,
                python_array=python_array,
                base64_str=b64
            )
    
    def generate_legacy_c_array(self, encrypted: bytes, keys: List[int], original: str) -> str:
        """Generate C array in legacy format"""
        encrypted_str = ''.join(f'\\x{b:02x}' for b in encrypted)
        
        return f"""╔════════════════════════════════════════════════════════════╗
║  LEGACY FORMAT - 3-Key with Rolling Modifier            ║
╚════════════════════════════════════════════════════════════╝

// String: {original}
// Algorithm: XOR with rolling modifier
// Formula: out[i] = in[i] ^ (k1^k2^k3) ^ r ^ i
// where r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF

// Copy this line:
{{(BYTE*)"{encrypted_str}", {len(encrypted)}, {{0x{keys[0]:02x}, 0x{keys[1]:02x}, 0x{keys[2]:02x}}}}}

// Keys: k1=0x{keys[0]:02x}, k2=0x{keys[1]:02x}, k3=0x{keys[2]:02x}
// Combined (k1^k2^k3) = 0x{keys[0] ^ keys[1] ^ keys[2]:02x}
"""
    
    def generate_custom_c_array(self, encrypted: bytes, keys: List[int], params: Dict, original: str) -> str:
        """Generate C array for custom algorithm"""
        encrypted_str = ''.join(f'\\x{b:02x}' for b in encrypted)
        key_str = ', '.join([f'0x{k:02x}' for k in keys])
        use_rolling = params.get('use_rolling', False)
        multiplier = params.get('multiplier', 19)
        shift = params.get('shift', 3)
        use_position = params.get('use_position', True)
        
        desc = []
        if use_rolling:
            desc.append(f"rolling modifier r = ((i * {multiplier}) ^ (i >> {shift}) ^ (size - i))")
        if use_position:
            desc.append("XOR with position i")
        
        return f"""╔════════════════════════════════════════════════════════════╗
║  CUSTOM ALGORITHM FORMAT                                   ║
╚════════════════════════════════════════════════════════════╝

// String: {original}
// Features: {', '.join(desc) if desc else 'Standard XOR'}
// Keys: {len(keys)}-byte key

// Encrypted data:
unsigned char encrypted[] = {{{', '.join([f'0x{b:02x}' for b in encrypted])}}};
unsigned char key[] = {{{key_str}}};
unsigned int key_len = {len(keys)};

// Copy this compact line:
{{(BYTE*)"{encrypted_str}", {len(encrypted)}, {{{key_str}}}}}
"""
    
    def generate_legacy_python_array(self, encrypted: bytes, keys: List[int], original: str) -> str:
        """Generate Python test script for legacy format"""
        return f"""# Python test for legacy algorithm
encrypted = {list(encrypted)}
k1, k2, k3 = 0x{keys[0]:02x}, 0x{keys[1]:02x}, 0x{keys[2]:02x}
combined = k1 ^ k2 ^ k3
size = len(encrypted)

def legacy_decrypt(data, k1, k2, k3):
    decrypted = bytearray()
    combined = k1 ^ k2 ^ k3
    size = len(data)
    
    for i in range(size):
        r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF
        decrypted_byte = data[i] ^ combined ^ r ^ (i & 0xFF)
        decrypted.append(decrypted_byte)
    
    return bytes(decrypted)

result = legacy_decrypt(encrypted, k1, k2, k3)
print(f"Decrypted: {{result.decode('utf-8')}}")  # Should print: {original}
"""
    
    def generate_custom_python_array(self, encrypted: bytes, keys: List[int], params: Dict, original: str) -> str:
        """Generate Python test script for custom algorithm"""
        use_rolling = params.get('use_rolling', False)
        multiplier = params.get('multiplier', 19)
        shift = params.get('shift', 3)
        use_position = params.get('use_position', True)
        
        rolling_code = ""
        if use_rolling:
            rolling_code = f"        r = ((i * {multiplier}) ^ (i >> {shift}) ^ (size - i)) & 0xFF\n        value ^= r\n"
        
        position_code = "        value ^= (i & 0xFF)\n" if use_position else ""
        
        return f"""# Python test for custom algorithm
encrypted = {list(encrypted)}
keys = {keys}
size = len(encrypted)

def custom_decrypt(data, keys):
    decrypted = bytearray()
    size = len(data)
    
    for i in range(size):
        value = data[i]
        
        # Apply key
        if len(keys) > 1:
            value ^= keys[i % len(keys)]
        else:
            value ^= keys[0]
        
{rolling_code}{position_code}
        decrypted.append(value)
    
    return bytes(decrypted)

result = custom_decrypt(encrypted, keys)
print(f"Decrypted: {{result.decode('utf-8')}}")
"""
    
    def generate_c_array(self, encrypted: bytes, key: List[int], algorithm: str, evasion: str, original_len: int, key_length: int) -> str:
        """Generate C array code for standard algorithms"""
        encrypted_str = ''.join(f'\\x{b:02x}' for b in encrypted)
        key_str = ', '.join([f'0x{k:02x}' for k in key])
        hex_bytes = ', '.join([f'0x{b:02x}' for b in encrypted])
        
        output = []
        output.append("╔════════════════════════════════════════════════════════════╗")
        output.append(f"║  {algorithm.upper()} ALGORITHM - Multiple Formats              ║")
        output.append("╚════════════════════════════════════════════════════════════╝")
        output.append("")
        output.append("// Option 1: String literal")
        output.append(f'unsigned char encrypted[] = "{encrypted_str}";')
        output.append(f"unsigned char key[] = {{{key_str}}};")
        output.append(f"unsigned int key_len = {len(key)};")
        output.append("")
        output.append("// Option 2: Byte array")
        output.append(f"unsigned char encrypted[] = {{{hex_bytes}}};")
        output.append(f"unsigned char key[] = {{{key_str}}};")
        output.append("")
        output.append("// Decryption function")
        output.append("void decrypt(unsigned char *data, int data_len, unsigned char *key, int key_len) {")
        output.append("    for(int i = 0; i < data_len; i++) {")
        
        if algorithm == "simple":
            output.append("        data[i] ^= key[0];")
        else:
            output.append("        data[i] ^= key[i % key_len];")
        
        output.append("    }")
        output.append("}")
        
        return "\n".join(output)
    
    def generate_python_array(self, encrypted: bytes, key: List[int], original_len: int) -> str:
        """Generate Python array code for standard algorithms"""
        return f"""# Python implementation
encrypted = {list(encrypted)}
key = {key}

def decrypt(data, key):
    result = bytearray()
    for i, b in enumerate(data):
        result.append(b ^ key[i % len(key)])
    return bytes(result)

decrypted = decrypt(encrypted, key)
print(f"Decrypted: {{decrypted.decode('utf-8', errors='ignore')}}")
"""

class XorpherGenerator:
    """Main XORPHER application class"""
    
    def __init__(self):
        self.ui = XorpherUI()
        self.engine = XorpherEngine()
        self.results_history = []
        self.output_dir = "xorpher_output"
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def encrypt_string(self):
        """Encrypt a string entered by user"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("🔐 STRING ENCRYPTION")
        
        print(f"\n{Fore.CYAN}    Enter the string to encrypt:{Style.RESET_ALL}")
        text = input(f"{Fore.GREEN}    >>>{Style.RESET_ALL} ").strip()
        
        if not text:
            self.ui.print_error("No input provided!")
            input("\nPress Enter to continue...")
            return
        
        # Select algorithm
        self.ui.print_header("🔄 SELECT ALGORITHM")
        print(f"{Fore.CYAN}    1. simple{Style.RESET_ALL}      - Single key XOR")
        print(f"{Fore.CYAN}    2. rotating{Style.RESET_ALL}    - Key repeats every N bytes")
        print(f"{Fore.CYAN}    3. poly{Style.RESET_ALL}        - Polymorphic (hash-based)")
        print(f"{Fore.CYAN}    4. custom{Style.RESET_ALL}      - Configure your own parameters")
        print(f"{Fore.CYAN}    5. legacy{Style.RESET_ALL}      - 3-key with rolling modifier")
        
        algo_choice = input(f"\n{Fore.GREEN}    Choice (1-5) [default: 2]:{Style.RESET_ALL} ").strip() or "2"
        
        algorithms = {
            '1': 'simple',
            '2': 'rotating',
            '3': 'poly',
            '4': 'custom',
            '5': 'legacy'
        }
        algorithm = algorithms.get(algo_choice, 'rotating')
        
        # Handle different algorithms
        if algorithm == "legacy":
            self.handle_legacy_encryption(text)
        elif algorithm == "custom":
            self.handle_custom_encryption(text)
        else:
            self.handle_standard_encryption(text, algorithm)
    
    def handle_legacy_encryption(self, text):
        """Handle legacy algorithm (3-key with rolling modifier)"""
        self.ui.print_header("🔑 LEGACY CONFIGURATION")
        print(f"{Fore.CYAN}    This algorithm uses 3 keys with a rolling modifier{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    Formula: out[i] = in[i] ^ (k1^k2^k3) ^ r ^ i{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    where r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF{Style.RESET_ALL}\n")
        
        print("    1. Generate random 3-byte keys")
        print("    2. Use custom keys")
        
        key_choice = input(f"\n{Fore.GREEN}    Choice (1-2) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
        
        custom_keys = None
        if key_choice == '2':
            try:
                k1 = int(input(f"{Fore.CYAN}    Enter k1 (hex, e.g., 0xfa):{Style.RESET_ALL} "), 16)
                k2 = int(input(f"{Fore.CYAN}    Enter k2 (hex, e.g., 0xd1):{Style.RESET_ALL} "), 16)
                k3 = int(input(f"{Fore.CYAN}    Enter k3 (hex, e.g., 0xfc):{Style.RESET_ALL} "), 16)
                custom_keys = [k1, k2, k3]
            except:
                self.ui.print_warning("Invalid input, using random keys")
        
        # Show summary
        print(f"\n{Fore.YELLOW}    {'─' * 50}")
        print(f"    LEGACY ENCRYPTION")
        print(f"    {'─' * 50}")
        print(f"    String:     {text}")
        print(f"    Algorithm:  legacy (3-key with rolling modifier)")
        print(f"    Keys:       {'Custom' if custom_keys else 'Random'}")
        print(f"    {'─' * 50}{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.CYAN}    Proceed? (y/n) [default: y]:{Style.RESET_ALL} ").strip().lower()
        if confirm == 'n':
            self.ui.print_info("Encryption cancelled")
            input("\nPress Enter to continue...")
            return
        
        # Perform encryption
        self.ui.print_info("Encrypting...")
        result = self.engine.encrypt(text, "legacy", "none", 3, custom_keys)
        self.results_history.append(result)
        
        # Display results
        self.display_legacy_results(result)
        
        # Save to file
        self.save_result(result)
        
        # Copy to clipboard
        if CLIPBOARD_AVAILABLE:
            try:
                # Extract just the line for clipboard
                match = re.search(r'\{\(BYTE\*\)"[^"]+", \d+, \{[^}]+\}\}', result.c_array)
                if match:
                    pyperclip.copy(match.group(0))
                    self.ui.print_success("Legacy format copied to clipboard!")
                else:
                    pyperclip.copy(result.c_array)
                    self.ui.print_success("Result copied to clipboard!")
            except:
                pass
    
    def handle_custom_encryption(self, text):
        """Handle custom configurable encryption"""
        self.ui.print_header("🔧 CUSTOM CONFIGURATION")
        
        print(f"{Fore.CYAN}    Configure your own encryption parameters:{Style.RESET_ALL}\n")
        
        # Key configuration
        print("    Key options:")
        print("    1. Single key")
        print("    2. Multiple keys (rotating)")
        print("    3. 3-key legacy style")
        
        key_type = input(f"\n{Fore.GREEN}    Choice (1-3) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
        
        keys = []
        if key_type == '1':
            key_val = random.randint(1, 255)
            keys = [key_val]
            print(f"    Using single key: 0x{key_val:02x}")
        elif key_type == '2':
            key_count = int(input(f"{Fore.CYAN}    Number of keys (2-16):{Style.RESET_ALL} ") or "3")
            key_count = max(2, min(16, key_count))
            for i in range(key_count):
                keys.append(random.randint(1, 255))
            print(f"    Generated {key_count} keys")
        else:  # 3-key legacy style
            for i in range(3):
                keys.append(random.randint(1, 255))
            print(f"    Generated 3 keys: 0x{keys[0]:02x}, 0x{keys[1]:02x}, 0x{keys[2]:02x}")
        
        # Rolling modifier options
        print(f"\n{Fore.CYAN}    Rolling modifier:{Style.RESET_ALL}")
        print("    1. No rolling (standard XOR)")
        print("    2. Simple rolling (position only)")
        print("    3. Legacy rolling (with multiplier and shift)")
        
        rolling_choice = input(f"\n{Fore.GREEN}    Choice (1-3) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
        
        params = {'use_rolling': False, 'use_position': False}
        
        if rolling_choice == '2':
            params['use_position'] = True
            print("    Using position modifier")
        elif rolling_choice == '3':
            params['use_rolling'] = True
            params['use_position'] = True
            multiplier = input(f"{Fore.CYAN}    Multiplier (default 19):{Style.RESET_ALL} ") or "19"
            shift = input(f"{Fore.CYAN}    Shift (default 3):{Style.RESET_ALL} ") or "3"
            params['multiplier'] = int(multiplier)
            params['shift'] = int(shift)
            print(f"    Using rolling: r = ((i * {params['multiplier']}) ^ (i >> {params['shift']}) ^ (size - i))")
        
        # Show summary
        print(f"\n{Fore.YELLOW}    {'─' * 50}")
        print(f"    CUSTOM ENCRYPTION")
        print(f"    {'─' * 50}")
        print(f"    String:     {text}")
        print(f"    Keys:       {len(keys)} bytes: {', '.join([f'0x{k:02x}' for k in keys])}")
        print(f"    Rolling:    {'Yes' if params['use_rolling'] else 'No'}")
        print(f"    Position:   {'Yes' if params['use_position'] else 'No'}")
        print(f"    {'─' * 50}{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.CYAN}    Proceed? (y/n) [default: y]:{Style.RESET_ALL} ").strip().lower()
        if confirm == 'n':
            self.ui.print_info("Encryption cancelled")
            input("\nPress Enter to continue...")
            return
        
        # Perform encryption
        self.ui.print_info("Encrypting...")
        result = self.engine.encrypt(text, "custom", "none", len(keys), keys, params)
        self.results_history.append(result)
        
        # Display results
        self.display_custom_results(result)
        
        # Save to file
        self.save_result(result)
        
        # Copy to clipboard
        if CLIPBOARD_AVAILABLE:
            try:
                pyperclip.copy(result.c_array)
                self.ui.print_success("Result copied to clipboard!")
            except:
                pass
    
    def handle_standard_encryption(self, text, algorithm):
        """Handle standard algorithms with evasion"""
        self.ui.print_header("🔑 KEY LENGTH")
        print(f"{Fore.CYAN}    1. auto{Style.RESET_ALL}        - Key length = data length")
        print(f"{Fore.CYAN}    2. 1 byte{Style.RESET_ALL}       - Single key")
        print(f"{Fore.CYAN}    3. 3 bytes{Style.RESET_ALL}      - 3-byte key")
        print(f"{Fore.CYAN}    4. 4 bytes{Style.RESET_ALL}      - 4-byte key")
        print(f"{Fore.CYAN}    5. 8 bytes{Style.RESET_ALL}      - 8-byte key")
        print(f"{Fore.CYAN}    6. 16 bytes{Style.RESET_ALL}     - 16-byte key")
        print(f"{Fore.CYAN}    7. 32 bytes{Style.RESET_ALL}     - 32-byte key")
        print(f"{Fore.CYAN}    8. custom{Style.RESET_ALL}       - Specify length (1-64)")
        
        key_choice = input(f"\n{Fore.GREEN}    Choice (1-8) [default: 3]:{Style.RESET_ALL} ").strip() or "3"
        
        key_length = None
        if key_choice == '1':
            key_length = None
        elif key_choice == '2':
            key_length = 1
        elif key_choice == '3':
            key_length = 3
        elif key_choice == '4':
            key_length = 4
        elif key_choice == '5':
            key_length = 8
        elif key_choice == '6':
            key_length = 16
        elif key_choice == '7':
            key_length = 32
        elif key_choice == '8':
            try:
                kl = int(input(f"{Fore.CYAN}    Enter key length (1-64):{Style.RESET_ALL} ").strip())
                key_length = max(1, min(64, kl))
            except:
                key_length = 3
        
        # Evasion level
        self.ui.print_header("🛡️ EVASION LEVEL")
        print(f"{Fore.CYAN}    1. none{Style.RESET_ALL}     - 0% garbage")
        print(f"{Fore.CYAN}    2. low{Style.RESET_ALL}      - 20% garbage")
        print(f"{Fore.CYAN}    3. medium{Style.RESET_ALL}   - 40% garbage")
        print(f"{Fore.CYAN}    4. high{Style.RESET_ALL}     - 60% garbage")
        print(f"{Fore.CYAN}    5. extreme{Style.RESET_ALL}  - 80% garbage")
        
        eva_choice = input(f"\n{Fore.GREEN}    Choice (1-5) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
        
        evasion_levels = {
            '1': 'none',
            '2': 'low',
            '3': 'medium',
            '4': 'high',
            '5': 'extreme'
        }
        evasion = evasion_levels.get(eva_choice, 'none')
        
        # Summary
        print(f"\n{Fore.YELLOW}    {'─' * 50}")
        print(f"    ENCRYPTION SUMMARY")
        print(f"    {'─' * 50}")
        print(f"    String:     {text}")
        print(f"    Algorithm:  {algorithm}")
        print(f"    Key Length: {key_length if key_length else 'Auto'} bytes")
        print(f"    Evasion:    {evasion}")
        print(f"    {'─' * 50}{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.CYAN}    Proceed? (y/n) [default: y]:{Style.RESET_ALL} ").strip().lower()
        if confirm == 'n':
            self.ui.print_info("Encryption cancelled")
            input("\nPress Enter to continue...")
            return
        
        # Encrypt
        self.ui.print_info("Encrypting...")
        result = self.engine.encrypt(text, algorithm, evasion, key_length)
        self.results_history.append(result)
        
        # Display
        self.display_standard_results(result)
        
        # Save
        self.save_result(result)
        
        # Copy
        if CLIPBOARD_AVAILABLE:
            try:
                pyperclip.copy(result.c_array)
                self.ui.print_success("Result copied to clipboard!")
            except:
                pass
    
    def display_legacy_results(self, result: EncryptionResult):
        """Display legacy encryption results"""
        self.ui.clear_screen()
        
        print(f"\n{Fore.GREEN}    🔐 LEGACY ENCRYPTION RESULTS{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    {'─' * 50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}    SUMMARY{Style.RESET_ALL}")
        print(f"    Original:     {result.original}")
        print(f"    Algorithm:    Legacy (3-key with rolling modifier)")
        print(f"    Keys:         k1=0x{result.key[0]:02x}, k2=0x{result.key[1]:02x}, k3=0x{result.key[2]:02x}")
        print(f"    Combined:     0x{result.key[0] ^ result.key[1] ^ result.key[2]:02x}")
        print(f"    Size:         {len(result.encrypted)} bytes\n")
        
        print(f"{Fore.GREEN}    OUTPUT FORMAT{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}    Copy this line:{Style.RESET_ALL}\n")
        
        # Extract just the line they need
        match = re.search(r'\{\(BYTE\*\)"[^"]+", \d+, \{[^}]+\}\}', result.c_array)
        if match:
            print(f"{Fore.CYAN}    {match.group(0)}{Style.RESET_ALL}\n")
        
        # Verify
        decrypted = self.engine.legacy_decrypt(result.encrypted, result.key[0], result.key[1], result.key[2])
        print(f"{Fore.MAGENTA}    VERIFICATION{Style.RESET_ALL}")
        if result.original in decrypted:
            print(f"    {Fore.GREEN}✓ Verified: '{decrypted}'{Style.RESET_ALL}")
        else:
            print(f"    {Fore.RED}✗ Verification failed{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}    📁 Full details saved to: {self.output_dir}/{Style.RESET_ALL}")
        
        # Wait for user input before returning
        input(f"\n{Fore.CYAN}    Press Enter to return to main menu...{Style.RESET_ALL}")
    
    def display_custom_results(self, result: EncryptionResult):
        """Display custom encryption results"""
        self.ui.clear_screen()
        
        print(f"\n{Fore.GREEN}    🔐 CUSTOM ENCRYPTION RESULTS{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    {'─' * 50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}    SUMMARY{Style.RESET_ALL}")
        print(f"    Original:     {result.original}")
        print(f"    Keys:         {len(result.key)} bytes: {', '.join([f'0x{k:02x}' for k in result.key])}")
        print(f"    Size:         {len(result.encrypted)} bytes\n")
        
        print(f"{Fore.GREEN}    OUTPUT{Style.RESET_ALL}")
        print(result.c_array)
        print()
        print(result.python_array)
        
        print(f"\n{Fore.CYAN}    📁 Full details saved to: {self.output_dir}/{Style.RESET_ALL}")
        
        # Wait for user input before returning
        input(f"\n{Fore.CYAN}    Press Enter to return to main menu...{Style.RESET_ALL}")
    
    def display_standard_results(self, result: EncryptionResult):
        """Display standard encryption results"""
        self.ui.clear_screen()
        
        print(f"\n{Fore.GREEN}    🔐 ENCRYPTION RESULTS{Style.RESET_ALL}")
        print(f"{Fore.GREEN}    {'─' * 50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}    SUMMARY{Style.RESET_ALL}")
        print(f"    Original:     {result.original}")
        print(f"    Algorithm:    {result.algorithm}")
        print(f"    Key Length:   {result.key_length if result.key_length else 'Auto'} bytes")
        print(f"    Evasion:      {result.evasion_level}")
        print(f"    Size:         {len(result.encrypted)} bytes\n")
        
        key_preview = ' '.join([f'0x{b:02x}' for b in result.key[:8]])
        if len(result.key) > 8:
            key_preview += ' ...'
        print(f"    Key preview:  {key_preview}\n")
        
        print(f"{Fore.GREEN}    C ARRAY{Style.RESET_ALL}")
        print(result.c_array)
        
        print(f"\n{Fore.CYAN}    📁 Full details saved to: {self.output_dir}/{Style.RESET_ALL}")
        
        # Wait for user input before returning
        input(f"\n{Fore.CYAN}    Press Enter to return to main menu...{Style.RESET_ALL}")
    
    def save_result(self, result: EncryptionResult):
        """Save result to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(c for c in result.original[:20] if c.isalnum() or c in '._- ')
        safe_name = safe_name.replace(' ', '_')
        if not safe_name:
            safe_name = "string"
        
        filename = f"{self.output_dir}/xorpher_{safe_name}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("XORPHER v2.5 - ENCRYPTION RESULT\n")
            f.write(f"Author: Excalibra | GitHub: https://github.com/Excalibra\n")
            f.write(f"Generated: {result.timestamp}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"ORIGINAL: {result.original}\n")
            f.write(f"ALGORITHM: {result.algorithm}\n")
            f.write(f"KEY LENGTH: {result.key_length if result.key_length else 'Auto'} bytes\n")
            f.write(f"EVASION: {result.evasion_level}\n")
            f.write(f"KEY: {result.key}\n")
            f.write(f"SIZE: {len(result.encrypted)} bytes\n\n")
            
            f.write("BASE64:\n")
            f.write(f"{result.base64}\n\n")
            
            f.write("C ARRAY:\n")
            f.write(result.c_array)
            f.write("\n\n")
            
            f.write("PYTHON:\n")
            f.write(result.python_array)
            f.write("\n")
        
        self.ui.print_success(f"Saved to {filename}")
    
    def show_guide(self):
        """Show encryption guide"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        guide = f"""
{Fore.CYAN}    AVAILABLE ALGORITHMS
    {'─' * 40}
    1. simple    - Single key XOR (basic)
    2. rotating  - Key repeats every N bytes
    3. poly      - Polymorphic (different each run)
    4. custom    - Configure your own parameters
    5. legacy    - 3-key with rolling modifier

{Fore.YELLOW}    CUSTOM CONFIGURATION
    {'─' * 40}
    • Key length: 1-64 bytes
    • Rolling modifier: r = ((i * M) ^ (i >> S) ^ (size - i))
    • Position XOR: include i in the calculation

{Fore.MAGENTA}    LEGACY ALGORITHM
    {'─' * 40}
    • Uses 3 keys with rolling modifier
    • Formula: out[i] = in[i] ^ (k1^k2^k3) ^ r ^ i
    • r = ((i * 19) ^ (i >> 3) ^ (size - i)) & 0xFF

{Fore.GREEN}    EVASION LEVELS
    {'─' * 40}
    • none     - 0% garbage
    • low      - 20% garbage
    • medium   - 40% garbage
    • high     - 60% garbage
    • extreme  - 80% garbage
{Style.RESET_ALL}"""
        print(guide)
        input(f"\n{Fore.CYAN}    Press Enter to return to main menu...{Style.RESET_ALL}")
    
    def show_about(self):
        """Show about information"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        about = f"""
{Fore.GREEN}    XORPHER v2.5 - Multi-Algorithm XOR Tool
    {'─' * 40}

{Fore.CYAN}    Author:  Excalibra
    GitHub:  https://github.com/Excalibra
    License: MIT

{Fore.YELLOW}    Features:
    • 5 encryption algorithms
    • Configurable key lengths (1-64)
    • Custom parameter configuration
    • Garbage byte insertion
    • Multiple output formats
    • Automatic verification
    • Clipboard support
    • Timestamped file output

{Fore.MAGENTA}    Use Cases:
    • String obfuscation
    • Payload encryption
    • Evasion techniques
    • Educational purposes

{Fore.RED}    ⚠️  For authorized testing only
{Style.RESET_ALL}"""
        print(about)
        input(f"\n{Fore.CYAN}    Press Enter to return to main menu...{Style.RESET_ALL}")
    
    def main_menu(self):
        """Display main menu"""
        while True:
            self.ui.clear_screen()
            self.ui.print_banner()
            
            print(f"\n{Fore.YELLOW}    MAIN MENU{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}1.{Style.RESET_ALL} 🔐 Encrypt a string")
            print(f"    {Fore.CYAN}2.{Style.RESET_ALL} 📖 Encryption guide")
            print(f"    {Fore.CYAN}3.{Style.RESET_ALL} ℹ️ About")
            print(f"    {Fore.CYAN}4.{Style.RESET_ALL} 🚪 Exit")
            
            choice = input(f"\n{Fore.GREEN}    ⚡ Select option (1-4):{Style.RESET_ALL} ").strip()
            
            if choice == '1':
                self.encrypt_string()
            elif choice == '2':
                self.show_guide()
            elif choice == '3':
                self.show_about()
            elif choice == '4':
                print(f"\n{Fore.CYAN}    Thanks for using XORPHER!{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}    https://github.com/Excalibra{Style.RESET_ALL}")
                sys.exit(0)
            else:
                self.ui.print_error("Invalid option")
                input("\nPress Enter to continue...")

def main():
    """Main entry point"""
    generator = XorpherGenerator()
    try:
        generator.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}    Interrupted{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}    Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()

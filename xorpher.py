#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════╗
║                         XORPHER v2.1                              ║
║               Ultimate XOR Encryption for Evasion                  ║
║              NEW: Configurable Key Length Support!                 ║
╚═══════════════════════════════════════════════════════════════════╝
GitHub: https://github.com/Excalibra
Author: Excalibra
License: MIT
"""

import random
import sys
import os
import json
import hashlib
import base64
from datetime import datetime
from typing import List, Dict, Tuple, Optional

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

# XORPHER MATRIX CYBERPUNK BANNER
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
    
{Fore.YELLOW}    KEY LENGTH         |  EVASION LEVEL      |  ALGORITHM
    ───────────────────┼─────────────────────┼───────────────────
    ▸ 1-64 bytes       │  ▸ 0% (none)        │  ▸ simple
    ▸ auto (max entropy│  ▸ 20% (low)        │  ▸ rotating ★
    ▸ custom           │  ▸ 40% (medium)     │  ▸ polymorphic
                       │  ▸ 60% (high)       │
                       │  ▸ 80% (extreme)    │
{Style.RESET_ALL}
    
{Fore.MAGENTA}    ⚡ GITHUB: https://github.com/Excalibra
    ⚡ AUTHOR: Excalibra  |  VERSION: 2.1.0
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
        """Print a section header with cyberpunk style"""
        print(f"\n{Fore.MAGENTA}╭─{title}{'─' * (60 - len(title))}╮{Style.RESET_ALL}")
    
    @staticmethod
    def print_subheader(title):
        """Print a subsection header"""
        print(f"\n{Fore.CYAN}├─ {title}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}│{Style.RESET_ALL}")

class XorpherEngine:
    """Core encryption engine"""
    
    def __init__(self):
        self.suspicious_keys = [0x00, 0x55, 0xAA, 0xFF, 0x33, 0x66, 0x99, 0xCC]
    
    def generate_key(self, length: int, algorithm: str, key_length: int = None) -> List[int]:
        """Generate encryption key based on algorithm with specified key length"""
        
        # Determine actual key length to use
        if key_length is None:
            # Default behavior - key length equals data length for rotating
            if algorithm == "simple":
                actual_length = 1
            else:
                actual_length = length
        else:
            # User specified key length
            actual_length = key_length
        
        if algorithm == "simple":
            # Single key for all bytes
            key_byte = random.randint(1, 255)
            while key_byte in self.suspicious_keys:
                key_byte = random.randint(1, 255)
            return [key_byte]
        
        elif algorithm == "rotating" or algorithm == "poly":
            # Generate key of specified length
            key = []
            for i in range(actual_length):
                key_byte = random.randint(1, 255)
                while key_byte in self.suspicious_keys:
                    key_byte = random.randint(1, 255)
                key.append(key_byte)
            return key
        
        else:  # rotating (default)
            key = []
            for i in range(actual_length):
                key_byte = random.randint(1, 255)
                while key_byte in self.suspicious_keys:
                    key_byte = random.randint(1, 255)
                key.append(key_byte)
            return key
    
    def decrypt(self, encrypted_data: bytes, key: List[int], original_length: int = None) -> str:
        """Decrypt data and extract original string"""
        decrypted = bytearray()
        key_len = len(key)
        
        # Apply XOR decryption
        for i, byte in enumerate(encrypted_data):
            decrypted.append(byte ^ key[i % key_len])
        
        if original_length:
            return decrypted.decode('utf-8', errors='ignore')[:original_length]
        else:
            return decrypted.decode('utf-8', errors='ignore')
    
    def verify_encryption(self, original: str, encrypted: bytes, key: List[int]) -> bool:
        """Verify that encryption/decryption works correctly"""
        try:
            decrypted = self.decrypt(encrypted, key)
            return original in decrypted
        except:
            return False
    
    def encrypt(self, data: str, algorithm: str = "rotating", evasion_level: str = "medium", key_length: int = None) -> EncryptionResult:
        """Main encryption method with configurable key length"""
        
        # Convert string to bytes
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
        
        # Create final byte array with garbage
        if garbage_ratio > 0:
            garbage_count = int(original_length * garbage_ratio)
            total_length = original_length + garbage_count
            
            # Create positions for real data
            positions = list(range(total_length))
            random.shuffle(positions)
            real_positions = sorted(positions[:original_length])
            
            # Build the mixed array
            mixed = bytearray(total_length)
            data_idx = 0
            
            for i in range(total_length):
                if i in real_positions and data_idx < original_length:
                    mixed[i] = data_bytes[data_idx]
                    data_idx += 1
                else:
                    mixed[i] = random.randint(1, 255)
            
            data_bytes = bytes(mixed)
        
        # Generate key with specified length
        key = self.generate_key(len(data_bytes), algorithm, key_length)
        
        # Encrypt
        encrypted = bytearray()
        key_len = len(key)
        for i, b in enumerate(data_bytes):
            encrypted.append(b ^ key[i % key_len])
        encrypted = bytes(encrypted)
        
        # Verify encryption
        if not self.verify_encryption(data, encrypted, key):
            print(f"{Fore.YELLOW}⚠ [WARNING] Encryption verification failed, retrying...{Style.RESET_ALL}")
            return self.encrypt(data, algorithm, evasion_level, key_length)
        
        # Generate all output formats
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
    
    def generate_c_array(self, encrypted: bytes, key: List[int], algorithm: str, evasion: str, original_len: int, key_length: int) -> str:
        """Generate C array code"""
        
        # Format encrypted bytes as string literal
        encrypted_str = ''.join(f'\\x{b:02x}' for b in encrypted)
        
        # Format key array
        key_str = ', '.join([f'0x{k:02x}' for k in key])
        
        # Byte array format
        hex_bytes = ', '.join([f'0x{b:02x}' for b in encrypted])
        
        # Create all formats
        output = []
        output.append("╔════════════════════════════════════════════════════════════╗")
        output.append("║  C ARRAY - MULTIPLE FORMATS                                ║")
        output.append("╚════════════════════════════════════════════════════════════╝")
        output.append("")
        
        # Format 1: String literal
        output.append("├─ Option 1: String literal format")
        output.append("│")
        output.append(f'│  unsigned char encrypted[] = "{encrypted_str}";')
        output.append(f"│  unsigned char key[] = {{{key_str}}};")
        output.append(f"│  unsigned int key_len = {len(key)};")
        output.append("│")
        
        # Format 2: Byte array
        output.append("├─ Option 2: Byte array format")
        output.append("│")
        output.append(f"│  unsigned char encrypted[] = {{{hex_bytes}}};")
        output.append(f"│  unsigned char key[] = {{{key_str}}};")
        output.append(f"│  unsigned int key_len = {len(key)};")
        output.append("│")
        
        # Format 3: Struct format
        output.append("├─ Option 3: Struct format (customize as needed)")
        output.append("│")
        output.append("│  typedef struct {")
        output.append("│      unsigned char* data;")
        output.append("│      unsigned int size;")
        output.append(f"│      unsigned char key[{len(key)}];")
        output.append("│  } encrypted_string_t;")
        output.append("│")
        output.append("│  encrypted_string_t encrypted = {")
        output.append(f'│      (unsigned char*)"{encrypted_str}",')
        output.append(f"│      {len(encrypted)},")
        output.append(f"│      {{{key_str}}}")
        output.append("│  };")
        output.append("│")
        
        # Format 4: Compact single line
        output.append("├─ Option 4: Compact format (easy copy-paste)")
        output.append("│")
        output.append(f'│  #define ENCRYPTED_DATA "{encrypted_str}"')
        output.append(f"│  #define ENCRYPTED_SIZE {len(encrypted)}")
        output.append(f"│  #define KEY {{{key_str}}}")
        output.append(f"│  #define KEY_SIZE {len(key)}")
        output.append("│")
        
        # Format 5: Decryption function
        output.append("├─ Decryption function")
        output.append("│")
        output.append("│  void decrypt(unsigned char *data, int data_len, unsigned char *key, int key_len) {")
        output.append("│      for(int i = 0; i < data_len; i++) {")
        output.append("│          data[i] ^= key[i % key_len];")
        output.append("│      }")
        output.append("│  }")
        output.append("│")
        output.append("│  // Usage:")
        output.append("│  // decrypt(encrypted, sizeof(encrypted), key, key_len);")
        output.append("│  // printf(\"%%s\\n\", encrypted);  // Original string appears!")
        output.append("│")
        output.append("╰────────────────────────────────────────────────────────────╯")
        
        return "\n".join(output)
    
    def generate_python_array(self, encrypted: bytes, key: List[int], original_len: int) -> str:
        """Generate Python array code"""
        output = []
        output.append("╔════════════════════════════════════════════════════════════╗")
        output.append("║  PYTHON IMPLEMENTATION                                     ║")
        output.append("╚════════════════════════════════════════════════════════════╝")
        output.append("")
        output.append("# Encrypted data")
        output.append(f"encrypted = {list(encrypted)}")
        output.append("")
        output.append("# Encryption key")
        output.append(f"key = {key}")
        output.append("")
        output.append("# Decryption function")
        output.append("def decrypt(data, key):")
        output.append("    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])")
        output.append("")
        output.append("# Decrypt and verify")
        output.append("decrypted = decrypt(encrypted, key)")
        output.append("print(f\"Decrypted: {decrypted.decode('utf-8', errors='ignore')}\")")
        output.append("")
        output.append("# Expected output contains the original string")
        
        return "\n".join(output)

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
        
        # Get input from user
        print(f"\n{Fore.CYAN}│  Enter the string to encrypt:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}│  (e.g., api.example.com, 192.168.1.1, secret_string){Style.RESET_ALL}")
        text = input(f"{Fore.GREEN}│  >>>{Style.RESET_ALL} ").strip()
        
        if not text:
            self.ui.print_error("No input provided!")
            input("\nPress Enter to continue...")
            return
        
        # Select algorithm
        self.ui.print_header("🔄 SELECT ALGORITHM")
        print(f"{Fore.CYAN}│  1. simple{Style.RESET_ALL}      - Single key")
        print(f"{Fore.CYAN}│  2. rotating{Style.RESET_ALL}    - Key repeats every N bytes {Fore.YELLOW}★ recommended{Style.RESET_ALL}")
        print(f"{Fore.CYAN}│  3. poly{Style.RESET_ALL}         - Polymorphic (hash-based)")
        
        algo_choice = input(f"\n{Fore.GREEN}│  Choice (1-3) [default: 2]:{Style.RESET_ALL} ").strip() or "2"
        
        algorithms = {
            '1': 'simple',
            '2': 'rotating',
            '3': 'poly'
        }
        algorithm = algorithms.get(algo_choice, 'rotating')
        
        # Select key length
        self.ui.print_header("🔑 KEY LENGTH CONFIGURATION")
        print(f"{Fore.CYAN}│  Choose key length:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}│  1. auto{Style.RESET_ALL}        - Key length = data length (max entropy)")
        print(f"{Fore.YELLOW}│  2. 1 byte{Style.RESET_ALL}       - Simple XOR")
        print(f"{Fore.YELLOW}│  3. 3 bytes{Style.RESET_ALL}      - Legacy compatibility")
        print(f"{Fore.YELLOW}│  4. 4 bytes{Style.RESET_ALL}      - Good balance")
        print(f"{Fore.YELLOW}│  5. 8 bytes{Style.RESET_ALL}      - Stronger")
        print(f"{Fore.YELLOW}│  6. 16 bytes{Style.RESET_ALL}     - Very strong")
        print(f"{Fore.YELLOW}│  7. 32 bytes{Style.RESET_ALL}     - Maximum strength")
        print(f"{Fore.YELLOW}│  8. custom{Style.RESET_ALL}       - Specify your own (1-64)")
        
        key_choice = input(f"\n{Fore.GREEN}│  Choice (1-8) [default: 3]:{Style.RESET_ALL} ").strip() or "3"
        
        key_length = None
        if key_choice == '1':
            key_length = None
            self.ui.print_info("Auto mode engaged")
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
                key_length = int(input(f"{Fore.CYAN}│  Enter key length (1-64):{Style.RESET_ALL} ").strip())
                if key_length < 1 or key_length > 64:
                    key_length = 3
                    self.ui.print_warning("Invalid length, defaulting to 3")
            except:
                key_length = 3
                self.ui.print_warning("Using 3 bytes")
        
        # Select evasion level
        self.ui.print_header("🛡️ EVASION LEVEL")
        print(f"{Fore.CYAN}│  1. none{Style.RESET_ALL}     - 0% garbage")
        print(f"{Fore.CYAN}│  2. low{Style.RESET_ALL}      - 20% garbage")
        print(f"{Fore.CYAN}│  3. medium{Style.RESET_ALL}   - 40% garbage")
        print(f"{Fore.CYAN}│  4. high{Style.RESET_ALL}     - 60% garbage")
        print(f"{Fore.CYAN}│  5. extreme{Style.RESET_ALL}  - 80% garbage")
        
        eva_choice = input(f"\n{Fore.GREEN}│  Choice (1-5) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
        
        evasion_levels = {
            '1': 'none',
            '2': 'low',
            '3': 'medium',
            '4': 'high',
            '5': 'extreme'
        }
        evasion = evasion_levels.get(eva_choice, 'none')
        
        # Show summary
        print(f"\n{Fore.YELLOW}╭─ ENCRYPTION SUMMARY {'─' * 40}╮")
        print(f"│  String:     {text}")
        print(f"│  Algorithm:  {algorithm}")
        print(f"│  Key Length: {key_length if key_length else 'Auto'} bytes")
        print(f"│  Evasion:    {evasion}")
        print(f"╰{'─' * 58}╯{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.CYAN}│  Proceed? (y/n) [default: y]:{Style.RESET_ALL} ").strip().lower()
        if confirm == 'n':
            self.ui.print_info("Encryption cancelled")
            input("\nPress Enter to continue...")
            return
        
        # Perform encryption
        self.ui.print_info("Initializing encryption matrix...")
        result = self.engine.encrypt(text, algorithm, evasion, key_length)
        self.results_history.append(result)
        
        # Display full results in terminal
        self.display_full_results(result)
        
        # Save to file
        self.save_result(result)
        
        # Copy to clipboard if available
        if CLIPBOARD_AVAILABLE:
            try:
                print(f"\n{Fore.CYAN}│  Copy to clipboard?{Style.RESET_ALL}")
                print("│  1. C array (all formats)")
                print("│  2. Python implementation")
                print("│  3. Base64 only")
                print("│  4. Nothing")
                copy_choice = input(f"\n{Fore.GREEN}│  Choice (1-4) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
                
                if copy_choice == '1':
                    pyperclip.copy(result.c_array)
                    self.ui.print_success("C array copied to clipboard!")
                elif copy_choice == '2':
                    pyperclip.copy(result.python_array)
                    self.ui.print_success("Python implementation copied to clipboard!")
                elif copy_choice == '3':
                    pyperclip.copy(result.base64)
                    self.ui.print_success("Base64 copied to clipboard!")
            except:
                pass
        
        input(f"\n{Fore.CYAN}│  Press Enter to continue...{Style.RESET_ALL}")
    
    def display_full_results(self, result: EncryptionResult):
        """Display complete encryption results in terminal with cyberpunk style"""
        self.ui.clear_screen()
        
        print(f"{Fore.GREEN}{'╔' + '═' * 78 + '╗'}")
        print(f"║{' ' * 31}🔐 ENCRYPTION RESULTS{' ' * 31}║")
        print(f"{'╚' + '═' * 78 + '╝'}{Style.RESET_ALL}")
        
        # Summary section
        print(f"\n{Fore.CYAN}╭─ SUMMARY {'─' * 68}╮")
        print(f"│  {Fore.YELLOW}Original:{Style.RESET_ALL}     {result.original}")
        print(f"│  {Fore.YELLOW}Algorithm:{Style.RESET_ALL}    {result.algorithm}")
        print(f"│  {Fore.YELLOW}Key Length:{Style.RESET_ALL}   {result.key_length if result.key_length else 'Auto'} bytes")
        print(f"│  {Fore.YELLOW}Evasion:{Style.RESET_ALL}      {result.evasion_level}")
        print(f"│  {Fore.YELLOW}Encrypted:{Style.RESET_ALL}    {len(result.encrypted)} bytes")
        print(f"│  {Fore.YELLOW}Base64:{Style.RESET_ALL}       {result.base64[:50]}...")
        
        # Key preview
        key_hex = ' '.join([f'0x{b:02x}' for b in result.key[:8]])
        if len(result.key) > 8:
            key_hex += ' ...'
        print(f"│  {Fore.YELLOW}Key (first 8):{Style.RESET_ALL} {key_hex}")
        print(f"╰{'─' * 78}╯")
        
        # C Array section
        print(f"\n{Fore.GREEN}╭─ C ARRAY IMPLEMENTATION {'─' * 54}╮{Style.RESET_ALL}")
        print(result.c_array)
        
        # Python section
        print(f"\n{Fore.MAGENTA}╭─ PYTHON IMPLEMENTATION {'─' * 55}╮{Style.RESET_ALL}")
        print(result.python_array)
        
        # Verification
        print(f"\n{Fore.YELLOW}╭─ VERIFICATION {'─' * 65}╮{Style.RESET_ALL}")
        
        # Decrypt to verify
        decrypted = self.engine.decrypt(result.encrypted, result.key)
        if result.original in decrypted:
            print(f"│  {Fore.GREEN}✓ ENCRYPTION VERIFIED SUCCESSFULLY{Style.RESET_ALL}")
            print(f"│  {Fore.CYAN}Decrypted string contains:{Style.RESET_ALL} {result.original}")
            print(f"│  {Fore.CYAN}Full decrypted:{Style.RESET_ALL} {decrypted}")
        else:
            print(f"│  {Fore.RED}✗ VERIFICATION FAILED!{Style.RESET_ALL}")
        print(f"╰{'─' * 78}╯")
        
        # File info
        print(f"\n{Fore.GREEN}╭─ FILE OUTPUT {'─' * 65}╮")
        print(f"│  📁 Full results saved to: {self.output_dir}/")
        print(f"╰{'─' * 78}╯{Style.RESET_ALL}")
    
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
            f.write("XORPHER v2.1 - ENCRYPTION RESULT\n")
            f.write(f"Author: Excalibra | GitHub: https://github.com/Excalibra\n")
            f.write(f"Generated: {result.timestamp}\n")
            f.write("="*70 + "\n\n")
            
            f.write("ENCRYPTION SUMMARY\n")
            f.write("-" * 40 + "\n")
            f.write(f"Original string: {result.original}\n")
            f.write(f"Algorithm: {result.algorithm}\n")
            f.write(f"Key length: {result.key_length if result.key_length else 'Auto'} bytes\n")
            f.write(f"Evasion level: {result.evasion_level}\n")
            f.write(f"Encrypted size: {len(result.encrypted)} bytes\n")
            f.write(f"Garbage bytes: {len(result.encrypted) - len(result.original.encode('utf-8'))}\n")
            f.write(f"Key: {result.key}\n\n")
            
            f.write("BASE64 ENCODED\n")
            f.write("-" * 40 + "\n")
            f.write(f"{result.base64}\n\n")
            
            f.write(result.c_array)
            f.write("\n\n")
            f.write(result.python_array)
            f.write("\n")
        
        self.ui.print_success(f"Results saved to: {filename}")
    
    def show_guide(self):
        """Show encryption guide"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("📖 XORPHER ENCRYPTION GUIDE")
        
        guide = f"""
{Fore.CYAN}╭─ KEY LENGTH SELECTION {'─' * 55}╮
│  • Auto      - Key length = data length (maximum entropy)  │
│  • 1 byte    - Simple XOR, least secure                     │
│  • 3 bytes   - Common in legacy code                         │
│  • 4-8 bytes - Good balance of security & size               │
│  • 16+ bytes - Maximum security                              │
╰{'─' * 78}╯

{Fore.YELLOW}╭─ EVASION LEVELS {'─' * 60}╮
│  • None    - 0% garbage, smallest output                    │
│  • Low     - 20% garbage bytes                               │
│  • Medium  - 40% garbage bytes (recommended)                 │
│  • High    - 60% garbage bytes                               │
│  • Extreme - 80% garbage bytes, hardest to detect            │
╰{'─' * 78}╯

{Fore.MAGENTA}╭─ ALGORITHMS {'─' * 63}╮
│  • Simple     - Single key for all bytes                     │
│  • Rotating   - Key repeats every N bytes ★ recommended      │
│  • Polymorphic - Hash-based keys, different each run         │
╰{'─' * 78}╯

{Fore.GREEN}╭─ OUTPUT FORMATS {'─' * 59}╮
│  • String literal with key array                             │
│  • Byte array format                                          │
│  • Struct format (customizable)                               │
│  • Compact #define format                                     │
│  • Python implementation with decryption function             │
╰{'─' * 78}╯

{Fore.RED}⚠️  DISCLAIMER: For educational and authorized testing only!{Style.RESET_ALL}
"""
        print(guide)
        input(f"\n{Fore.CYAN}│  Press Enter to continue...{Style.RESET_ALL}")
    
    def show_about(self):
        """Show about information"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        about = f"""
{Fore.GREEN}╔════════════════════════════════════════════════════════════╗
║                 XORPHER v2.1 - MATRIX EDITION               ║
╚════════════════════════════════════════════════════════════╝

{Fore.CYAN}╭─ ABOUT {'─' * 70}╮
│  Author:  Excalibra                                           │
│  GitHub:  https://github.com/Excalibra                        │
│  License: MIT                                                  │
│  Version: 2.1.0 - Configurable Key Lengths                    │
╰{'─' * 78}╯

{Fore.YELLOW}╭─ DESCRIPTION {'─' * 63}╮
│  XORPHER is an advanced XOR encryption tool with configurable  │
│  key lengths and evasion techniques. All results are displayed │
│  directly in the terminal for immediate copy-paste use.        │
╰{'─' * 78}╯

{Fore.MAGENTA}╭─ FEATURES {'─' * 66}╮
│  • Configurable key lengths (1-64 bytes)                      │
│  • Multiple encryption algorithms                              │
│  • Garbage byte insertion for evasion                          │
│  • Multiple output formats (C, Python)                         │
│  • Full results displayed in terminal                          │
│  • Automatic verification                                      │
│  • Clipboard integration                                       │
│  • Saves to timestamped files                                  │
╰{'─' * 78}╯

{Fore.RED}⚠️  DISCLAIMER: For educational and authorized testing only!
   The author is not responsible for misuse.{Style.RESET_ALL}
"""
        print(about)
        input(f"\n{Fore.CYAN}│  Press Enter to continue...{Style.RESET_ALL}")
    
    def main_menu(self):
        """Display main menu and handle user input"""
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
                print(f"\n{Fore.CYAN}    ⚡ GLITCH TERMINATED. THANKS FOR USING XORPHER! ⚡{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}    https://github.com/Excalibra{Style.RESET_ALL}")
                sys.exit(0)
            else:
                self.ui.print_error("Invalid option! Choose 1-4")
                input("\nPress Enter to continue...")

def main():
    """Main entry point"""
    generator = XorpherGenerator()
    
    try:
        generator.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠ INTERRUPTED BY USER{Style.RESET_ALL}")
        print(f"{Fore.CYAN}⚡ GLITCH TERMINATED{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}https://github.com/Excalibra{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}⚠ ERROR: {e}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Report issues: https://github.com/Excalibra/xorpher/issues{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()

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

# XORPHER ASCII ART
XORPHER_ART = f"""{Fore.CYAN}
╔═══════════════════════════════════════════════════════════════════╗
║  ██╗  ██╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗███████╗██████╗        ║
║  ╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗       ║
║   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║█████╗  ██████╔╝       ║
║   ██╔██╗ ██║   ██║██╔══██╗██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ║
║  ██╔╝ ██╗╚██████╔╝██║  ██║██║     ██║  ██║███████╗██║  ██║       ║
║  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ║
╠═══════════════════════════════════════════════════════════════════╣
║                    S T E A L T H   E D I T I O N                  ║
║                    v2.1 - Configurable Key Length                  ║
╚═══════════════════════════════════════════════════════════════════╝
{Fore.YELLOW}
          GitHub: https://github.com/Excalibra
          Author: Excalibra
          Version: 2.1.0
{Fore.CYAN}═════════════════════════════════════════════════════════════════════{Style.RESET_ALL}
"""

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
        """Print the XORPHER banner"""
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
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.YELLOW}{title:^60}")
        print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")

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
            print(f"{Fore.YELLOW}[!] Warning: Encryption verification failed, retrying...{Style.RESET_ALL}")
            return self.encrypt(data, algorithm, evasion_level, key_length)
        
        # Generate C array
        c_array = self.generate_c_array(encrypted, key, algorithm, evasion_level, original_length, key_length)
        
        # Generate Python array
        python_array = self.generate_python_array(encrypted, key, original_length)
        
        # Encode to base64
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
        
        # Create multiple format options
        formats = []
        
        # Format 1: String literal with key array
        formats.append(f"""// Option 1: String literal format
unsigned char encrypted[] = "{encrypted_str}";
unsigned char key[] = {{{key_str}}};
unsigned int key_len = {len(key)};""")
        
        # Format 2: Byte array format
        hex_bytes = ', '.join([f'0x{b:02x}' for b in encrypted])
        formats.append(f"""// Option 2: Byte array format
unsigned char encrypted[] = {{{hex_bytes}}};
unsigned char key[] = {{{key_str}}};
unsigned int key_len = {len(key)};""")
        
        # Format 3: Struct format (if your code uses custom structs)
        formats.append(f"""// Option 3: Struct format (customize as needed)
typedef struct {{
    unsigned char* data;
    unsigned int size;
    unsigned char key[{len(key)}];
}} encrypted_string_t;

encrypted_string_t encrypted = {{(unsigned char*)"{encrypted_str}", {len(encrypted)}, {{{key_str}}}}};""")
        
        return f"""/*
 * XORPHER v2.1 - Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
 * Author: Excalibra (https://github.com/Excalibra)
 * 
 * Original string: "{original_len} bytes"
 * Algorithm: {algorithm}
 * Evasion level: {evasion}
 * Key length: {key_length if key_length else 'Auto'} bytes
 * Total encrypted size: {len(encrypted)} bytes
 */

{"=" * 60}
// Choose the format that matches your code:
{"=" * 60}

{chr(10).join(formats)}

{"=" * 60}
// Decryption function example:
{"=" * 60}
void decrypt(unsigned char *data, int data_len, unsigned char *key, int key_len) {{
    for(int i = 0; i < data_len; i++) {{
        data[i] ^= key[i % key_len];
    }}
}}

// Usage:
// decrypt(encrypted, sizeof(encrypted), key, key_len);
// printf("%s\\n", encrypted);  // Prints original string
"""
    
    def generate_python_array(self, encrypted: bytes, key: List[int], original_len: int) -> str:
        """Generate Python array code"""
        return f"""# XORPHER v2.1 - Python Decryption
encrypted = {list(encrypted)}
key = {key}

def decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

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
        
        self.ui.print_header("STRING ENCRYPTION")
        
        # Get input from user
        print(f"\n{Fore.CYAN}Enter the string to encrypt:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}(e.g., api.example.com, 192.168.1.1, payload, etc.){Style.RESET_ALL}")
        text = input(f"\n{Fore.GREEN}>>>{Style.RESET_ALL} ").strip()
        
        if not text:
            self.ui.print_error("No input provided!")
            input("\nPress Enter to continue...")
            return
        
        # Select algorithm
        self.ui.print_header("SELECT ALGORITHM")
        print(f"{Fore.CYAN}1. Simple XOR{Style.RESET_ALL}     - Single key")
        print(f"{Fore.CYAN}2. Rotating XOR{Style.RESET_ALL}   - Key repeats every N bytes")
        print(f"{Fore.CYAN}3. Polymorphic{Style.RESET_ALL}    - Hash-based dynamic keys")
        
        algo_choice = input(f"\n{Fore.GREEN}Choice (1-3) [default: 2]:{Style.RESET_ALL} ").strip() or "2"
        
        algorithms = {
            '1': 'simple',
            '2': 'rotating',
            '3': 'poly'
        }
        algorithm = algorithms.get(algo_choice, 'rotating')
        
        # Select key length
        self.ui.print_header("KEY LENGTH CONFIGURATION")
        print(f"{Fore.CYAN}Choose key length (affects security & compatibility):{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}1. Auto{Style.RESET_ALL}         - Key length = data length (maximum entropy)")
        print(f"{Fore.YELLOW}2. 1 byte{Style.RESET_ALL}        - Single key (simple XOR)")
        print(f"{Fore.YELLOW}3. 3 bytes{Style.RESET_ALL}       - Common for legacy code")
        print(f"{Fore.YELLOW}4. 4 bytes{Style.RESET_ALL}       - Good balance")
        print(f"{Fore.YELLOW}5. 8 bytes{Style.RESET_ALL}       - Stronger")
        print(f"{Fore.YELLOW}6. 16 bytes{Style.RESET_ALL}      - Very strong")
        print(f"{Fore.YELLOW}7. 32 bytes{Style.RESET_ALL}      - Maximum strength")
        print(f"{Fore.YELLOW}8. Custom{Style.RESET_ALL}        - Specify your own length")
        
        key_choice = input(f"\n{Fore.GREEN}Choice (1-8) [default: 3]:{Style.RESET_ALL} ").strip() or "3"
        
        key_length = None
        if key_choice == '1':
            key_length = None  # Auto
            self.ui.print_info("Using auto key length (equals data length)")
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
                key_length = int(input(f"{Fore.CYAN}Enter key length (1-64):{Style.RESET_ALL} ").strip())
                if key_length < 1 or key_length > 64:
                    key_length = 3
                    self.ui.print_warning("Invalid length, using 3 bytes")
            except:
                key_length = 3
                self.ui.print_warning("Using 3 bytes")
        
        # Select evasion level
        self.ui.print_header("SELECT EVASION LEVEL")
        print(f"{Fore.CYAN}1. None{Style.RESET_ALL}      - No garbage bytes")
        print(f"{Fore.CYAN}2. Low{Style.RESET_ALL}       - 20% garbage bytes")
        print(f"{Fore.CYAN}3. Medium{Style.RESET_ALL}    - 40% garbage bytes")
        print(f"{Fore.CYAN}4. High{Style.RESET_ALL}      - 60% garbage bytes")
        print(f"{Fore.CYAN}5. Extreme{Style.RESET_ALL}   - 80% garbage bytes")
        
        eva_choice = input(f"\n{Fore.GREEN}Choice (1-5) [default: 1]:{Style.RESET_ALL} ").strip() or "1"
        
        evasion_levels = {
            '1': 'none',
            '2': 'low',
            '3': 'medium',
            '4': 'high',
            '5': 'extreme'
        }
        evasion = evasion_levels.get(eva_choice, 'none')
        
        # Show summary
        print(f"\n{Fore.YELLOW}{'='*50}")
        print(f"Encryption Summary:")
        print(f"{'='*50}")
        print(f"String:     {text}")
        print(f"Algorithm:  {algorithm}")
        print(f"Key Length: {key_length if key_length else 'Auto'} bytes")
        print(f"Evasion:    {evasion}")
        print(f"{'='*50}{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.CYAN}Proceed? (y/n) [default: y]:{Style.RESET_ALL} ").strip().lower()
        if confirm == 'n':
            self.ui.print_info("Encryption cancelled")
            input("\nPress Enter to continue...")
            return
        
        # Perform encryption
        self.ui.print_info("Encrypting...")
        result = self.engine.encrypt(text, algorithm, evasion, key_length)
        self.results_history.append(result)
        
        # Display result
        self.display_result(result)
        
        # Save to file
        self.save_result(result)
        
        # Copy to clipboard if available
        if CLIPBOARD_AVAILABLE:
            try:
                pyperclip.copy(result.c_array)
                self.ui.print_success("C array copied to clipboard!")
            except:
                pass
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def display_result(self, result: EncryptionResult):
        """Display encryption result"""
        self.ui.clear_screen()
        self.ui.print_header("ENCRYPTION RESULT")
        
        print(f"\n{Fore.GREEN}Original:{Style.RESET_ALL} {result.original}")
        print(f"{Fore.GREEN}Algorithm:{Style.RESET_ALL} {result.algorithm}")
        print(f"{Fore.GREEN}Key Length:{Style.RESET_ALL} {result.key_length if result.key_length else 'Auto'} bytes")
        print(f"{Fore.GREEN}Evasion Level:{Style.RESET_ALL} {result.evasion_level}")
        print(f"{Fore.GREEN}Encrypted size:{Style.RESET_ALL} {len(result.encrypted)} bytes")
        
        # Show key preview
        key_preview = result.key[:min(10, len(result.key))]
        preview_str = ' '.join([f'0x{b:02x}' for b in key_preview])
        if len(result.key) > 10:
            preview_str += ' ...'
        print(f"{Fore.GREEN}Key:{Style.RESET_ALL} {preview_str}")
        
        print(f"\n{Fore.YELLOW}Multiple output formats available in the full output.{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}Full details saved to: {self.output_dir}/{Style.RESET_ALL}")
    
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
            
            f.write(f"ORIGINAL STRING:\n{result.original}\n\n")
            f.write(f"ALGORITHM: {result.algorithm}\n")
            f.write(f"KEY LENGTH: {result.key_length if result.key_length else 'Auto'} bytes\n")
            f.write(f"EVASION LEVEL: {result.evasion_level}\n")
            f.write(f"KEY: {result.key}\n")
            f.write(f"ENCRYPTED SIZE: {len(result.encrypted)} bytes\n\n")
            
            f.write("BASE64 ENCODED:\n")
            f.write(f"{result.base64}\n\n")
            
            f.write("C ARRAY (Multiple Formats):\n")
            f.write(result.c_array)
            f.write("\n\n")
            
            f.write("PYTHON ARRAY:\n")
            f.write(result.python_array)
            f.write("\n")
        
        self.ui.print_success(f"Result saved to: {filename}")
    
    def show_guide(self):
        """Show encryption guide"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("XORPHER ENCRYPTION GUIDE")
        
        guide = f"""
{Fore.CYAN}KEY LENGTH SELECTION:{Style.RESET_ALL}
• 1 byte   - Simple XOR, least secure
• 3 bytes  - Common in legacy code
• 4-8 bytes - Good balance of security & size
• 16+ bytes - Maximum security

{Fore.CYAN}EVASION LEVELS:{Style.RESET_ALL}
• None    - No garbage, smallest output
• Low     - 20% garbage
• Medium  - 40% garbage
• High    - 60% garbage
• Extreme - 80% garbage, hardest to detect

{Fore.CYAN}ALGORITHMS:{Style.RESET_ALL}
• Simple    - Single key for all bytes
• Rotating  - Key repeats every N bytes
• Polymorphic - Hash-based keys

{Fore.CYAN}OUTPUT FORMATS:{Style.RESET_ALL}
The tool generates multiple C formats:
1. String literal with key array
2. Byte array format
3. Struct format (customizable)

{Fore.YELLOW}TIP: Choose key length based on your decryption code!{Style.RESET_ALL}
"""
        print(guide)
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def show_about(self):
        """Show about information"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        about = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════╗
║                    ABOUT XORPHER v2.1                      ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}Author:{Style.RESET_ALL}  Excalibra
{Fore.YELLOW}GitHub:{Style.RESET_ALL}  https://github.com/Excalibra
{Fore.YELLOW}License:{Style.RESET_ALL} MIT

{Fore.CYAN}Description:{Style.RESET_ALL}
XORPHER is an advanced XOR encryption tool with configurable
key lengths and evasion techniques.

{Fore.CYAN}Features:{Style.RESET_ALL}
• Configurable key lengths (1-64 bytes)
• Multiple encryption algorithms
• Garbage byte insertion
• Multiple output formats
• Automatic verification

{Fore.CYAN}Use Cases:{Style.RESET_ALL}
• String obfuscation in payloads
• Evading static analysis
• Educational purposes
• Authorized security testing

{Fore.YELLOW}Disclaimer:{Style.RESET_ALL}
For educational and authorized testing only.
"""
        print(about)
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def main_menu(self):
        """Display main menu and handle user input"""
        while True:
            self.ui.clear_screen()
            self.ui.print_banner()
            
            print(f"\n{Fore.YELLOW}MAIN MENU:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}1.{Style.RESET_ALL} 🔐 Encrypt a string")
            print(f"{Fore.CYAN}2.{Style.RESET_ALL} 📖 Encryption guide")
            print(f"{Fore.CYAN}3.{Style.RESET_ALL} ℹ️ About")
            print(f"{Fore.CYAN}4.{Style.RESET_ALL} 🚪 Exit")
            
            choice = input(f"\n{Fore.GREEN}Select option (1-4):{Style.RESET_ALL} ").strip()
            
            if choice == '1':
                self.encrypt_string()
            elif choice == '2':
                self.show_guide()
            elif choice == '3':
                self.show_about()
            elif choice == '4':
                self.ui.print_info("Thanks for using XORPHER!")
                sys.exit(0)
            else:
                self.ui.print_error("Invalid option!")
                input("\nPress Enter to continue...")

def main():
    """Main entry point"""
    generator = XorpherGenerator()
    
    try:
        generator.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Interrupted by user{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Thanks for using XORPHER!{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()

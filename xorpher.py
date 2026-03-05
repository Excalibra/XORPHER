#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════╗
║                         XORPHER v2.0                              ║
║               Ultimate XOR Encryption for Evasion                  ║
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
╚═══════════════════════════════════════════════════════════════════╝
{Fore.YELLOW}
          GitHub: https://github.com/Excalibra
          Author: Excalibra
          Version: 2.0.0
{Fore.CYAN}═════════════════════════════════════════════════════════════════════{Style.RESET_ALL}
"""

class EncryptionResult:
    """Class for encryption results"""
    def __init__(self, original, encrypted, key, algorithm, evasion_level, c_array, python_array, base64_str):
        self.original = original
        self.encrypted = encrypted
        self.key = key
        self.algorithm = algorithm
        self.evasion_level = evasion_level
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
    
    def generate_key(self, length: int, algorithm: str) -> List[int]:
        """Generate encryption key based on algorithm"""
        if algorithm == "simple":
            # Single key for all bytes
            key_byte = random.randint(1, 255)
            while key_byte in self.suspicious_keys:
                key_byte = random.randint(1, 255)
            return [key_byte]
        
        elif algorithm == "rotating":
            # Different key for each position
            key = []
            for i in range(length):
                key_byte = random.randint(1, 255)
                while key_byte in self.suspicious_keys:
                    key_byte = random.randint(1, 255)
                key.append(key_byte)
            return key
        
        elif algorithm == "poly":
            # Polymorphic - based on hash
            seed = str(random.getrandbits(128))
            hash_val = hashlib.md5(seed.encode()).hexdigest()
            key = []
            for i in range(length):
                key_byte = (int(hash_val[i % 32], 16) << 4) | random.randint(1, 15)
                key.append(key_byte)
            return key
        
        else:  # rotating (default)
            key = []
            for i in range(length):
                key_byte = random.randint(1, 255)
                while key_byte in self.suspicious_keys:
                    key_byte = random.randint(1, 255)
                key.append(key_byte)
            return key
    
    def encrypt(self, data: str, algorithm: str = "rotating", evasion_level: str = "medium") -> EncryptionResult:
        """Main encryption method"""
        
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
        
        # Generate key
        key = self.generate_key(len(data_bytes), algorithm)
        
        # Encrypt based on algorithm
        if algorithm == "simple":
            # Simple XOR with single key
            key_byte = key[0]
            encrypted = bytes([b ^ key_byte for b in data_bytes])
        else:
            # Rotating XOR (also used for poly)
            encrypted = bytearray()
            key_len = len(key)
            for i, b in enumerate(data_bytes):
                encrypted.append(b ^ key[i % key_len])
            encrypted = bytes(encrypted)
        
        # Generate C array
        c_array = self.generate_c_array(encrypted, key, algorithm, evasion_level, original_length)
        
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
            c_array=c_array,
            python_array=python_array,
            base64_str=b64
        )
    
    def generate_c_array(self, encrypted: bytes, key: List[int], algorithm: str, evasion: str, original_len: int) -> str:
        """Generate C array code for the encrypted data"""
        # Format encrypted bytes
        hex_lines = []
        line = []
        for i, b in enumerate(encrypted):
            line.append(f"0x{b:02x}")
            if len(line) == 12 or i == len(encrypted) - 1:
                hex_lines.append("    " + ", ".join(line))
                line = []
        
        encrypted_hex = ",\n".join(hex_lines)
        
        # Format key
        key_hex = ", ".join([f"0x{k:02x}" for k in key])
        
        return f"""/*
 * XORPHER v2.0 - Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
 * Author: Excalibra (https://github.com/Excalibra)
 * 
 * Original string length: {original_len} bytes
 * Algorithm: {algorithm}
 * Evasion level: {evasion}
 * Total encrypted size: {len(encrypted)} bytes
 */

// Encrypted data (includes garbage bytes for evasion)
unsigned char encrypted_data[] = {{
{encrypted_hex}
}};

// Encryption key
unsigned char xor_key[] = {{ {key_hex} }};

// Decryption function
void decrypt_data(unsigned char *data, int data_len, unsigned char *key, int key_len) {{
    for(int i = 0; i < data_len; i++) {{
        data[i] ^= key[i % key_len];
    }}
}}

// Usage example:
// decrypt_data(encrypted_data, sizeof(encrypted_data), xor_key, sizeof(xor_key));
// printf("%s", (char*)encrypted_data);  // Prints original string
"""
    
    def generate_python_array(self, encrypted: bytes, key: List[int], original_len: int) -> str:
        """Generate Python array code"""
        return f"""# XORPHER v2.0 - Python Decryption Example
# Author: Excalibra (https://github.com/Excalibra)
# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

encrypted = {list(encrypted)}  # Encrypted data with garbage bytes
key = {key}  # Encryption key
original_length = {original_len}  # Original string length

def decrypt(encrypted_data, xor_key):
    '''Decrypt XORPHER encrypted data'''
    decrypted = bytearray()
    key_len = len(xor_key)
    
    for i, byte in enumerate(encrypted_data):
        decrypted.append(byte ^ xor_key[i % key_len])
    
    return bytes(decrypted)

# Decrypt and print result
decrypted_bytes = decrypt(encrypted, key)
print(f"Decrypted: {{decrypted_bytes.decode('utf-8', errors='ignore')}}")
"""

class XorpherGenerator:
    """Main XORPHER application class"""
    
    def __init__(self):
        self.ui = XorpherUI()
        self.engine = XorpherEngine()
        self.results_history = []
        self.output_dir = "xorpher_output"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def encrypt_domain(self):
        """Encrypt a domain or string entered by user"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("DOMAIN / STRING ENCRYPTION")
        
        # Get input from user
        print(f"\n{Fore.CYAN}Enter the domain or string to encrypt:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}(e.g., www.example.com, 192.168.1.1, etc.){Style.RESET_ALL}")
        text = input(f"\n{Fore.GREEN}>>>{Style.RESET_ALL} ").strip()
        
        if not text:
            self.ui.print_error("No input provided!")
            input("\nPress Enter to continue...")
            return
        
        # Select algorithm
        self.ui.print_header("SELECT ALGORITHM")
        print(f"{Fore.CYAN}1. Simple XOR{Style.RESET_ALL}     - Single key (basic)")
        print(f"{Fore.CYAN}2. Rotating XOR{Style.RESET_ALL}   - Key changes per byte (recommended)")
        print(f"{Fore.CYAN}3. Polymorphic{Style.RESET_ALL}    - Hash-based key (maximum stealth)")
        
        algo_choice = input(f"\n{Fore.GREEN}Choice (1-3) [default: 2]:{Style.RESET_ALL} ").strip() or "2"
        
        algorithms = {
            '1': 'simple',
            '2': 'rotating',
            '3': 'poly'
        }
        algorithm = algorithms.get(algo_choice, 'rotating')
        
        # Select evasion level
        self.ui.print_header("SELECT EVASION LEVEL")
        print(f"{Fore.CYAN}1. None{Style.RESET_ALL}      - No garbage bytes")
        print(f"{Fore.CYAN}2. Low{Style.RESET_ALL}       - 20% garbage bytes")
        print(f"{Fore.CYAN}3. Medium{Style.RESET_ALL}    - 40% garbage bytes (recommended)")
        print(f"{Fore.CYAN}4. High{Style.RESET_ALL}      - 60% garbage bytes")
        print(f"{Fore.CYAN}5. Extreme{Style.RESET_ALL}   - 80% garbage bytes")
        
        eva_choice = input(f"\n{Fore.GREEN}Choice (1-5) [default: 3]:{Style.RESET_ALL} ").strip() or "3"
        
        evasion_levels = {
            '1': 'none',
            '2': 'low',
            '3': 'medium',
            '4': 'high',
            '5': 'extreme'
        }
        evasion = evasion_levels.get(eva_choice, 'medium')
        
        # Confirm
        print(f"\n{Fore.YELLOW}Encrypting: '{text}'")
        print(f"Algorithm: {algorithm}")
        print(f"Evasion: {evasion}{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.CYAN}Proceed? (y/n) [default: y]:{Style.RESET_ALL} ").strip().lower()
        if confirm == 'n':
            self.ui.print_info("Encryption cancelled")
            input("\nPress Enter to continue...")
            return
        
        # Perform encryption
        self.ui.print_info("Encrypting...")
        result = self.engine.encrypt(text, algorithm, evasion)
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
    
    def encrypt_file(self):
        """Encrypt contents of a file"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("FILE ENCRYPTION")
        
        filename = input(f"\n{Fore.CYAN}Enter filename to encrypt:{Style.RESET_ALL} ").strip()
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.ui.print_success(f"Loaded {len(content)} characters from {filename}")
            
            # Use medium evasion by default for files
            result = self.engine.encrypt(content, "rotating", "high")
            self.results_history.append(result)
            
            self.display_result(result)
            self.save_result(result)
            
            if CLIPBOARD_AVAILABLE:
                try:
                    pyperclip.copy(result.c_array)
                    self.ui.print_success("C array copied to clipboard!")
                except:
                    pass
            
        except FileNotFoundError:
            self.ui.print_error(f"File not found: {filename}")
        except Exception as e:
            self.ui.print_error(f"Error reading file: {e}")
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def display_result(self, result: EncryptionResult):
        """Display encryption result"""
        self.ui.clear_screen()
        self.ui.print_header("ENCRYPTION RESULT")
        
        print(f"\n{Fore.GREEN}Original:{Style.RESET_ALL} {result.original}")
        print(f"{Fore.GREEN}Algorithm:{Style.RESET_ALL} {result.algorithm}")
        print(f"{Fore.GREEN}Evasion Level:{Style.RESET_ALL} {result.evasion_level}")
        print(f"{Fore.GREEN}Key length:{Style.RESET_ALL} {len(result.key)} bytes")
        print(f"{Fore.GREEN}Encrypted size:{Style.RESET_ALL} {len(result.encrypted)} bytes")
        
        # Show key preview
        key_preview = result.key[:10]
        if len(result.key) > 10:
            key_display = str(key_preview)[:-1] + ", ...]"
        else:
            key_display = str(key_preview)
        print(f"{Fore.GREEN}Key (first 10):{Style.RESET_ALL} {key_display}")
        
        # Show Base64 preview
        print(f"{Fore.GREEN}Base64 (first 50):{Style.RESET_ALL} {result.base64[:50]}...")
        
        # Show C array preview
        print(f"\n{Fore.YELLOW}C Array (preview):{Style.RESET_ALL}")
        c_lines = result.c_array.strip().split('\n')
        for line in c_lines[:10]:  # Show first 10 lines
            print(f"  {line}")
        if len(c_lines) > 10:
            print(f"  {Fore.CYAN}... (full array saved to file){Style.RESET_ALL}")
        
        # Show Python array preview
        print(f"\n{Fore.YELLOW}Python Array (preview):{Style.RESET_ALL}")
        py_lines = result.python_array.strip().split('\n')
        for line in py_lines[:5]:  # Show first 5 lines
            print(f"  {line}")
    
    def save_result(self, result: EncryptionResult):
        """Save result to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create a safe filename from the original string
        safe_name = "".join(c for c in result.original[:20] if c.isalnum() or c in '._- ')
        safe_name = safe_name.replace(' ', '_')
        if not safe_name:
            safe_name = "string"
        
        filename = f"{self.output_dir}/xorpher_{safe_name}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("XORPHER v2.0 - ENCRYPTION RESULT\n")
            f.write(f"Author: Excalibra | GitHub: https://github.com/Excalibra\n")
            f.write(f"Generated: {result.timestamp}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"ORIGINAL STRING:\n{result.original}\n\n")
            f.write(f"ALGORITHM: {result.algorithm}\n")
            f.write(f"EVASION LEVEL: {result.evasion_level}\n")
            f.write(f"KEY: {result.key}\n")
            f.write(f"KEY LENGTH: {len(result.key)} bytes\n")
            f.write(f"ENCRYPTED SIZE: {len(result.encrypted)} bytes\n\n")
            
            f.write("BASE64 ENCODED:\n")
            f.write(f"{result.base64}\n\n")
            
            f.write("C ARRAY:\n")
            f.write(result.c_array)
            f.write("\n\n")
            
            f.write("PYTHON ARRAY:\n")
            f.write(result.python_array)
            f.write("\n")
        
        self.ui.print_success(f"Result saved to: {filename}")
    
    def show_evasion_guide(self):
        """Show evasion techniques guide"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("XORPHER EVASION TECHNIQUES GUIDE")
        
        guide = f"""
{Fore.CYAN}1. GARBAGE BYTE INSERTION{Style.RESET_ALL}
   • Random bytes are inserted between real data
   • Breaks signature-based detection patterns
   • Ratio increases with evasion level:
     - Low: 20% garbage
     - Medium: 40% garbage (recommended)
     - High: 60% garbage
     - Extreme: 80% garbage

{Fore.CYAN}2. ROTATING XOR KEYS{Style.RESET_ALL}
   • Key changes with each byte position
   • Avoids static XOR pattern detection
   • Makes frequency analysis difficult

{Fore.CYAN}3. POLYMORPHIC ENCRYPTION{Style.RESET_ALL}
   • Different encryption each run
   • Based on MD5 hash + random seed
   • Maximum stealth for sensitive payloads

{Fore.CYAN}4. SUSPICIOUS KEY AVOIDANCE{Style.RESET_ALL}
   • Automatically avoids common malware keys
   • Skips: 0x00, 0x55, 0xAA, 0xFF, 0x33, 0x66
   • Reduces chance of signature detection

{Fore.CYAN}5. USE IN DROPPER DEVELOPMENT{Style.RESET_ALL}
   • Copy generated C arrays directly
   • Integrate with your dropper code
   • Decrypt at runtime when needed

{Fore.YELLOW}RECOMMENDED FOR DOMAINS/IPs:{Style.RESET_ALL}
   • Use Rotating algorithm with High evasion
   • This makes static analysis very difficult
   • Decrypt just before making connection

{Fore.YELLOW}TIP:{Style.RESET_ALL} The C array can be directly pasted into your 
      C/C++ dropper or malware source code.
"""
        print(guide)
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def show_history(self):
        """Show encryption history"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        self.ui.print_header("ENCRYPTION HISTORY")
        
        if not self.results_history:
            print(f"\n{Fore.YELLOW}No encryption history yet.{Style.RESET_ALL}")
        else:
            for i, result in enumerate(self.results_history[-10:], 1):  # Show last 10
                print(f"\n{Fore.CYAN}{i}. {result.timestamp}{Style.RESET_ALL}")
                print(f"   Original: {result.original[:50]}{'...' if len(result.original) > 50 else ''}")
                print(f"   Algorithm: {result.algorithm} | Evasion: {result.evasion_level}")
                print(f"   Size: {len(result.encrypted)} bytes")
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def show_about(self):
        """Show about information"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        about = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════╗
║                    ABOUT XORPHER v2.0                      ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}Author:{Style.RESET_ALL}  Excalibra
{Fore.YELLOW}GitHub:{Style.RESET_ALL}  https://github.com/Excalibra
{Fore.YELLOW}License:{Style.RESET_ALL} MIT

{Fore.CYAN}Description:{Style.RESET_ALL}
XORPHER is an advanced XOR encryption tool designed specifically
for penetration testers and security researchers. It implements
multiple layers of obfuscation to evade antivirus and EDR solutions.

{Fore.CYAN}Features:{Style.RESET_ALL}
• Multiple encryption algorithms (Simple, Rotating, Polymorphic)
• Adjustable evasion levels with garbage byte insertion
• Generates ready-to-use C and Python arrays
• Automatic suspicious key avoidance
• Clipboard integration for easy copying
• Saves results to timestamped files

{Fore.CYAN}Use Cases:{Style.RESET_ALL}
• Obfuscating domain names and IPs in droppers
• Hiding strings in payloads
• Evading static string analysis
• Educational purposes and authorized testing

{Fore.YELLOW}Disclaimer:{Style.RESET_ALL}
This tool is for educational and authorized security testing only.
Use only on systems you own or have explicit permission to test.
The author is not responsible for any misuse.

{Fore.CYAN}════════════════════════════════════════════════════════════{Style.RESET_ALL}
"""
        print(about)
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
    
    def main_menu(self):
        """Display main menu and handle user input"""
        while True:
            self.ui.clear_screen()
            self.ui.print_banner()
            
            print(f"\n{Fore.YELLOW}MAIN MENU:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}1.{Style.RESET_ALL} 🔐 Encrypt a domain/string")
            print(f"{Fore.CYAN}2.{Style.RESET_ALL} 📁 Encrypt from file")
            print(f"{Fore.CYAN}3.{Style.RESET_ALL} 📖 Evasion techniques guide")
            print(f"{Fore.CYAN}4.{Style.RESET_ALL} 📜 Encryption history")
            print(f"{Fore.CYAN}5.{Style.RESET_ALL} ℹ️ About")
            print(f"{Fore.CYAN}6.{Style.RESET_ALL} 🚪 Exit")
            
            choice = input(f"\n{Fore.GREEN}Select option (1-6):{Style.RESET_ALL} ").strip()
            
            if choice == '1':
                self.encrypt_domain()
            elif choice == '2':
                self.encrypt_file()
            elif choice == '3':
                self.show_evasion_guide()
            elif choice == '4':
                self.show_history()
            elif choice == '5':
                self.show_about()
            elif choice == '6':
                self.ui.print_info("Thanks for using XORPHER!")
                print(f"{Fore.CYAN}GitHub: https://github.com/Excalibra{Style.RESET_ALL}")
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
        print(f"{Fore.CYAN}[+] GitHub: https://github.com/Excalibra{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()

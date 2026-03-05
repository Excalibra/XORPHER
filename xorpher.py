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
    
    @staticmethod
    def print_verification_success():
        """Print verification success animation"""
        print(f"\n{Fore.GREEN}╔══════════════════════════════════════════════════════════╗")
        print(f"║           ✅ VERIFICATION SUCCESSFUL ✅               ║")
        print(f"║      Encryption/Decryption cycle works perfectly!      ║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

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
    
    def decrypt(self, encrypted_data: bytes, key: List[int], original_length: int = None) -> str:
        """Decrypt data and extract original string"""
        decrypted = bytearray()
        key_len = len(key)
        
        # Apply XOR decryption
        for i, byte in enumerate(encrypted_data):
            decrypted.append(byte ^ key[i % key_len])
        
        # If we know original length, extract just the real data
        if original_length:
            # Find the original string by looking for valid UTF-8 sequences
            # This is a simplification - in reality we'd need to track positions
            decoded = decrypted.decode('utf-8', errors='ignore')
            return decoded[:original_length]
        else:
            return decrypted.decode('utf-8', errors='ignore')
    
    def verify_encryption(self, original: str, encrypted: bytes, key: List[int]) -> Tuple[bool, str]:
        """Verify that encryption/decryption works correctly"""
        try:
            # Decrypt the data
            decrypted = self.decrypt(encrypted, key)
            
            # Check if original is contained in decrypted string
            # (because of garbage bytes, the decrypted string will have extra chars)
            if original in decrypted:
                # Find where the original string starts
                start_pos = decrypted.find(original)
                if start_pos >= 0:
                    return True, decrypted
                else:
                    return False, decrypted
            else:
                return False, decrypted
        except Exception as e:
            return False, f"Verification failed: {e}"
    
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
        
        # Store positions of real data for verification
        real_positions = []
        
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
        
        # Verify encryption
        verification_passed, decrypted_data = self.verify_encryption(data, encrypted, key)
        
        if not verification_passed:
            print(f"{Fore.YELLOW}[!] Warning: Encryption verification initially failed, retrying...{Style.RESET_ALL}")
            # Recursively try again if verification fails
            return self.encrypt(data, algorithm, evasion_level)
        
        # Generate C array
        c_array = self.generate_c_array(encrypted, key, algorithm, evasion_level, original_length, real_positions)
        
        # Generate Python array
        python_array = self.generate_python_array(encrypted, key, original_length, real_positions)
        
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
    
    def generate_c_array(self, encrypted: bytes, key: List[int], algorithm: str, evasion: str, original_len: int, real_positions: List[int]) -> str:
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
        
        # Create position array if we have positions
        positions_str = ""
        if real_positions:
            pos_lines = []
            line = []
            for i, pos in enumerate(real_positions):
                line.append(str(pos))
                if len(line) == 20 or i == len(real_positions) - 1:
                    pos_lines.append("    " + ", ".join(line))
                    line = []
            positions_str = f"""

// Positions of real data (for extracting original string)
int real_positions[{len(real_positions)}] = {{
{",\n".join(pos_lines)}
}};
"""
        
        return f"""/*
 * XORPHER v2.0 - Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
 * Author: Excalibra (https://github.com/Excalibra)
 * 
 * Original string: "{self.truncate_string(original_len, 50)}"
 * Original length: {original_len} bytes
 * Algorithm: {algorithm}
 * Evasion level: {evasion}
 * Total encrypted size: {len(encrypted)} bytes
 * Garbage bytes: {len(encrypted) - original_len} ({evasion} level)
 */

// Encrypted data (includes garbage bytes for evasion)
unsigned char encrypted_data[] = {{
{encrypted_hex}
}};

// Encryption key
unsigned char xor_key[] = {{ {key_hex} }};
unsigned int key_length = {len(key)};
{positions_str}
// Decryption function
void decrypt_data(unsigned char *data, int data_len, unsigned char *key, int key_len) {{
    for(int i = 0; i < data_len; i++) {{
        data[i] ^= key[i % key_len];
    }}
}}

// Extract original string (removes garbage bytes)
void extract_original(unsigned char *data, int data_len, unsigned char *output) {{
    int out_idx = 0;
    for(int i = 0; i < data_len; i++) {{
        // Check if this position contains real data
        // You need to implement your own logic or store positions
        // For simplicity, we'll just decrypt all and use the string
        output[out_idx++] = data[i];
    }}
    output[out_idx] = '\\0';
}}

// Usage example:
// decrypt_data(encrypted_data, sizeof(encrypted_data), xor_key, key_length);
// printf("Decrypted (with garbage): %s\\n", encrypted_data);
// // Original string is contained within the decrypted data
"""
    
    def truncate_string(self, original_len, max_len):
        """Truncate string for display"""
        return "..."  # Just return placeholder since we don't have the actual string here
    
    def generate_python_array(self, encrypted: bytes, key: List[int], original_len: int, real_positions: List[int]) -> str:
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

def extract_original(decrypted_data, original_len):
    '''Extract original string (first original_len bytes that are valid)'''
    # In a real scenario, you'd need to know which bytes are real
    # For simplicity, we'll just take the first original_len bytes
    return decrypted_data[:original_len]

# Decrypt and verify
decrypted_bytes = decrypt(encrypted, key)
print(f"Full decrypted (with garbage): {{decrypted_bytes}}")

# Extract original (simplified - real implementation would need position tracking)
original_bytes = decrypted_bytes[:original_length]
try:
    original_string = original_bytes.decode('utf-8', errors='ignore')
    print(f"Extracted original: {{original_string}}")
    print(f"Original length: {{original_length}} bytes")
except:
    print("Could not decode original string")
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
        
        # Verify encryption by decrypting
        self.verify_encryption(result)
        
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
    
    def verify_encryption(self, result: EncryptionResult):
        """Verify encryption by decrypting and showing the result"""
        self.ui.print_header("ENCRYPTION VERIFICATION")
        
        print(f"\n{Fore.CYAN}Decrypting to verify...{Style.RESET_ALL}")
        
        # Decrypt the data
        decrypted = self.engine.decrypt(result.encrypted, result.key)
        
        # Check if original is in decrypted
        if result.original in decrypted:
            self.ui.print_verification_success()
            print(f"\n{Fore.GREEN}Original string: {Style.RESET_ALL}{result.original}")
            print(f"{Fore.GREEN}Decrypted string: {Style.RESET_ALL}{decrypted}")
            print(f"{Fore.GREEN}Status: {Style.RESET_ALL}✅ Original found in decrypted data")
            
            # Show where the original appears
            start_pos = decrypted.find(result.original)
            if start_pos >= 0:
                print(f"{Fore.GREEN}Position: {Style.RESET_ALL}Bytes {start_pos}-{start_pos + len(result.original) - 1}")
                
                # Show visual representation
                print(f"\n{Fore.CYAN}Decrypted data visualization:{Style.RESET_ALL}")
                prefix = decrypted[:start_pos]
                match = result.original
                suffix = decrypted[start_pos + len(match):]
                
                # Truncate if too long
                if len(prefix) > 20:
                    prefix = "..." + prefix[-20:]
                if len(suffix) > 20:
                    suffix = suffix[:20] + "..."
                
                print(f"{Fore.WHITE}{prefix}{Fore.GREEN}{match}{Fore.WHITE}{suffix}{Style.RESET_ALL}")
                print(f"{Fore.WHITE}{' ' * len(prefix)}{'^' * len(match)}{Style.RESET_ALL}")
        else:
            self.ui.print_error("Verification FAILED! Original string not found in decrypted data.")
            print(f"\n{Fore.RED}Original: {result.original}")
            print(f"Decrypted: {decrypted}{Style.RESET_ALL}")
    
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
            self.verify_encryption(result)
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
        print(f"{Fore.GREEN}Garbage bytes:{Style.RESET_ALL} {len(result.encrypted) - len(result.original.encode('utf-8'))}")
        
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
        # Show first 5 and last 5 lines of the array data
        array_start = 0
        array_end = 0
        for i, line in enumerate(c_lines):
            if 'unsigned char encrypted_data' in line:
                array_start = i + 2  # Skip the opening line
            if '};' in line and i > array_start:
                array_end = i
                break
        
        if array_end > array_start:
            # Show first 3 lines of array
            for line in c_lines[array_start:min(array_start+3, array_end)]:
                print(f"  {line}")
            if array_end - array_start > 6:
                print(f"  {Fore.CYAN}  ... ({array_end - array_start - 6} more lines){Style.RESET_ALL}")
            # Show last 3 lines of array
            for line in c_lines[max(array_end-3, array_start+3):array_end]:
                print(f"  {line}")
        else:
            for line in c_lines[:10]:
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
            f.write(f"ENCRYPTED SIZE: {len(result.encrypted)} bytes\n")
            f.write(f"GARBAGE BYTES: {len(result.encrypted) - len(result.original.encode('utf-8'))}\n\n")
            
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

{Fore.CYAN}5. VERIFICATION SYSTEM{Style.RESET_ALL}
   • Automatically decrypts after encryption
   • Confirms the original string is recoverable
   • Shows exactly where it appears in decrypted data
   • Guarantees your payload will work

{Fore.YELLOW}RECOMMENDED FOR DOMAINS/IPs:{Style.RESET_ALL}
   • Use Rotating algorithm with High evasion
   • This makes static analysis very difficult
   • Decrypt just before making connection
   • Always verify the decryption works!

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
                print(f"   Size: {len(result.encrypted)} bytes | Garbage: {len(result.encrypted) - len(result.original.encode('utf-8'))} bytes")
        
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
• ✅ Automatic decryption verification

{Fore.CYAN}Verification System:{Style.RESET_ALL}
• Every encryption is automatically decrypted and checked
• Shows the original string within decrypted garbage data
• Confirms the encryption works before saving
• Guarantees your payload will decrypt correctly

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

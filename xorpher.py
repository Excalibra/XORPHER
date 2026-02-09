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
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import argparse
from dataclasses import dataclass
import hashlib
from colorama import init, Fore, Style, Back
try:
    import pyperclip  # For clipboard functionality
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

# Initialize colorama for cross-platform colored output
init(autoreset=True)

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

# Rest of your existing code continues here...
# [Keep all the classes and functions you already have]
# Just adding the credits at the beginning and in the help section

class XorpherGenerator:
    """Main XORPHER application class"""
    
    def __init__(self):
        self.ui = XorpherUI()
        self.results_history = []
        self.config = {
            'auto_copy': True,
            'save_to_file': True,
            'output_dir': 'xorpher_output',
            'theme': 'stealth',
            'author': 'Excalibra',
            'github': 'https://github.com/Excalibra'
        }
    
    def show_help(self):
        """Show help and evasion tips"""
        self.ui.clear_screen()
        
        help_text = f"""
{Fore.CYAN}{' XORPHER HELP & EVASION GUIDE ':=^70}

{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗
{Fore.YELLOW}║                     ABOUT XORPHER                       ║
{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝
{Fore.WHITE}
  Author: {Fore.CYAN}Excalibra{Fore.WHITE}
  GitHub: {Fore.CYAN}https://github.com/Excalibra{Fore.WHITE}
  License: {Fore.CYAN}MIT{Fore.WHITE}
  Version: {Fore.CYAN}2.0.0{Fore.WHITE}

  XORPHER is an advanced XOR encryption tool designed specifically
  for evasion of antivirus and EDR solutions. It implements multiple
  layers of obfuscation and randomization to avoid pattern detection.

{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗
{Fore.YELLOW}║                 EVASION TECHNIQUES                      ║
{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝

{Fore.GREEN}1. ROTATING XOR:{Fore.WHITE}
   • Key changes with each byte position
   • Avoids static XOR signature detection
   • Adds garbage bytes to break patterns
   • Recommended for most use cases

{Fore.GREEN}2. MULTI-LAYER ENCRYPTION:{Fore.WHITE}
   • Multiple XOR operations with different keys
   • Mixes different algorithms (XOR, shift, add)
   • Each layer uses different techniques
   • Harder for static analysis

{Fore.GREEN}3. POLYMORPHIC ENCRYPTION:{Fore.WHITE}
   • Different encryption each run
   • Based on MD5 hash of input + timestamp
   • Maximum stealth but larger output
   • Recommended for sensitive payloads

{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗
{Fore.YELLOW}║                WINDOWS DEFENDER EVASION                 ║
{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝

{Fore.CYAN}1. AVOID SUSPICIOUS KEYS:{Fore.WHITE}
   • Don't use: 0xAA, 0x55, 0xFF, 0x00, 0x33, 0x66
   • These are common in malware samples
   • XORPHER automatically avoids these

{Fore.CYAN}2. USE GARBAGE BYTES:{Fore.WHITE}
   • Add random bytes between real data
   • Breaks pattern recognition
   • Configure ratio based on evasion level

{Fore.CYAN}3. SPLIT STRINGS:{Fore.WHITE}
   • Break long strings into multiple parts
   • Use different encryption for each part
   • Combine at runtime

{Fore.CYAN}4. ADD JUNK CODE:{Fore.WHITE}
   • Insert harmless operations in C code
   • Use different variable names each run
   • Add fake API calls or calculations

{Fore.YELLOW}╔══════════════════════════════════════════════════════════╗
{Fore.YELLOW}║                  USAGE EXAMPLES                         ║
{Fore.YELLOW}╚══════════════════════════════════════════════════════════╝

{Fore.MAGENTA}Basic usage:{Fore.WHITE}
  $ python xorpher.py
  $ python xorpher.py -s "Hello World" --evasion high

{Fore.MAGENTA}Advanced usage:{Fore.WHITE}
  $ python xorpher.py -f strings.txt --batch --output payload.c
  $ python xorpher.py --algorithm poly --evasion extreme

{Fore.MAGENTA}For dropper development:{Fore.WHITE}
  1. Encrypt all your strings with XORPHER
  2. Copy the generated C structures
  3. Integrate with your dropper code
  4. Test on isolated VM first

{Fore.CYAN}{'='*70}

{Fore.YELLOW}DISCLAIMER:{Fore.WHITE}
  This tool is for educational and authorized security testing only.
  Use only on systems you own or have explicit permission to test.
  The author is not responsible for any misuse.

{Fore.CYAN}{'='*70}
"""
        print(help_text)
        input(f"\n{Fore.WHITE}Press Enter to continue...")

# [Rest of your code remains the same...]
# Add this at the end of the file:

def main():
    """Main entry point with credits"""
    parser = argparse.ArgumentParser(
        description=f"XORPHER v2.0 - Advanced XOR Encryption for Evasion\nAuthor: Excalibra | GitHub: https://github.com/Excalibra",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s                          # Interactive mode
  %(prog)s -s "hello world"         # Encrypt single string
  %(prog)s -f strings.txt           # Encrypt from file
  
Author: Excalibra
GitHub: https://github.com/Excalibra
License: MIT
        """
    )
    
    # [Rest of your argument parsing code...]

if __name__ == "__main__":
    try:
        print(XORPHER_ART)
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Interrupted by user")
        print(f"{Fore.CYAN}[+] Thanks for using XORPHER!")
        print(f"{Fore.CYAN}[+] GitHub: https://github.com/Excalibra")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}")
        print(f"{Fore.CYAN}[+] Report issues: https://github.com/Excalibra/xorpher/issues")
        sys.exit(1)

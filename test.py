import argparse
import sys
import os

# Ensure we can import snortparser if running from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from snortparser import Parser

def verify_rules(file_path):
    print(f"Verifying rules in {file_path}...")
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    success_count = 0
    fail_count = 0
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        try:
            # Demonstrate usage of snortparser
            parsed = Parser(line)
            
            # Print details for the first few rules to demonstrate output
            if success_count < 1:
                print(f"\nSuccessfully parsed DEMO rule on line {i+1}:")
                print(f"Original: {line[:50]}...")
                print(f"Header: {parsed.header}")
                
            success_count += 1
        except ValueError as e:
            print(f"\n[FAIL] Error parsing line {i+1}: {e}")
            print(f"Rule: {line}")
            fail_count += 1
        except Exception as e:
            print(f"\n[FAIL] Unexpected error on line {i+1}: {e}")
            print(f"Rule: {line}")
            fail_count += 1

    print(f"\nVerification complete.")
    print(f"Successfully parsed: {success_count}")
    print(f"Failed: {fail_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify Snort rules using snortparser.")
    parser.add_argument("file", nargs="?", default="test.rules", help="Path to the rules file (default: test.rules)")
    args = parser.parse_args()
    
    verify_rules(args.file)

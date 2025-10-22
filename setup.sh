#!/usr/bin/env python3
"""
Quantum Computing Demo Launcher
Run this file to start the amazing quantum demo!
"""

import sys
import os

def main():
    print("🌌 Welcome to the Quantum Computing Demo!")
    print("=" * 40)
    
    # Add current directory to path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        from examples.demo import run_quantum_demo
        run_quantum_demo()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure all files are in the correct directories")
        print("📁 Required files: quantum_rng.py, quantum_key_exchange.py, image_encryptor.py, visualizer.py")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
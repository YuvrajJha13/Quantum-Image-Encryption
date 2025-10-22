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
        # Test basic imports first
        try:
            from qiskit import QuantumCircuit
            from qiskit_aer import AerSimulator
            print("✅ Qiskit imports successful!")
        except ImportError as e:
            print(f"❌ Qiskit import error: {e}")
            print("💡 Try: pip install --upgrade qiskit qiskit-aer")
            return
        
        print("🚀 Starting quantum demo...")
        from examples.demo import run_quantum_demo
        run_quantum_demo()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure these files exist:")
        print("   - quantum_rng.py")
        print("   - quantum_key_exchange.py") 
        print("   - image_encryptor.py")
        print("   - visualizer.py")
        print("   - examples/demo.py")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 This might be due to quantum simulator limits.")
        print("   Try running individual components:")
        print("   - python quantum_rng.py")
        print("   - python quantum_key_exchange.py")

if __name__ == "__main__":
    main()
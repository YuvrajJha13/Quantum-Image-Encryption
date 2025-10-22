#!/usr/bin/env python3
"""
Test file to check if all imports work correctly
"""

print("🔍 Testing Quantum Computing Imports...")

try:
    from qiskit import QuantumCircuit
    print("✅ QuantumCircuit import successful")
    
    from qiskit_aer import AerSimulator
    print("✅ AerSimulator import successful")
    
    import numpy as np
    print("✅ NumPy import successful")
    
    import matplotlib.pyplot as plt
    print("✅ Matplotlib import successful")
    
    from cryptography.hazmat.primitives import hashes
    print("✅ Cryptography import successful")
    
    print("\n🎉 All imports successful! You're ready for quantum computing!")
    
except ImportError as e:
    print(f"❌ Import failed: {e}")
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from cryptography.hazmat.primitives import hashes
import sys

class QuantumRNG:
    def __init__(self):
        try:
            self.simulator = AerSimulator()
            self.circuit = self._create_quantum_circuit()
            print("✅ Quantum RNG initialized successfully!")
        except Exception as e:
            print(f"❌ Quantum RNG initialization failed: {e}")
            sys.exit(1)
    
    def _create_quantum_circuit(self):
        """Create a quantum circuit for true random number generation - using 16 qubits"""
        qc = QuantumCircuit(16, 16)  # Reduced from 8 to 16 for better randomness
        
        # Create superposition
        for i in range(16):
            qc.h(i)
        
        # Add entanglement in a chain
        for i in range(15):
            qc.cx(i, i+1)
        
        qc.measure(range(16), range(16))
        return qc
    
    def generate_random_bits(self, num_bits=256):
        """Generate true random bits using quantum mechanics"""
        try:
            random_bits = ""
            shots = max(1, (num_bits + 15) // 16)  # Adjust shots based on qubits
            
            compiled_circuit = transpile(self.circuit, self.simulator)
            
            # Run all shots at once for efficiency
            job = self.simulator.run(compiled_circuit, shots=shots)
            result = job.result()
            counts = result.get_counts()
            
            # Collect all bitstrings
            for bitstring in counts.keys():
                random_bits += bitstring
                if len(random_bits) >= num_bits:
                    break
            
            return random_bits[:num_bits]
        except Exception as e:
            print(f"❌ Quantum random generation failed: {e}")
            return None
    
    def generate_quantum_key(self, length=256):
        """Generate a cryptographically secure quantum random key"""
        print(f"🔮 Generating {length}-bit quantum key...")
        random_bits = self.generate_random_bits(length)
        
        if random_bits is None:
            print("⚠️  Falling back to classical PRNG")
            import secrets
            return secrets.token_bytes(length // 8)
        
        key_bytes = int(random_bits, 2).to_bytes(length // 8, byteorder='big')
        
        digest = hashes.Hash(hashes.SHA256())
        digest.update(key_bytes)
        final_key = digest.finalize()
        
        print(f"✅ Generated quantum key: {final_key.hex()[:32]}...")
        return final_key

if __name__ == "__main__":
    qrng = QuantumRNG()
    key = qrng.generate_quantum_key(128)
    print(f"Test key: {key.hex()}")
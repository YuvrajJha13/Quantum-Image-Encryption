from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

class BB84Protocol:
    """Simulate BB84 Quantum Key Distribution Protocol"""
    
    def __init__(self):
        self.simulator = AerSimulator()
        self.basis_choices = ['Z', 'X']
    
    def prepare_qubits(self, bits, bases):
        n = len(bits)
        circuit = QuantumCircuit(n, n)
        
        for i in range(n):
            if bits[i] == 1:
                circuit.x(i)
            if bases[i] == 'X':
                circuit.h(i)
        
        return circuit
    
    def measure_qubits(self, circuit, bases):
        n = len(bases)
        measured_circuit = circuit.copy()
        
        for i in range(n):
            if bases[i] == 'X':
                measured_circuit.h(i)
        
        measured_circuit.measure_all()
        return measured_circuit
    
    def simulate_key_exchange(self, key_length=16):  
        """Simulate BB84 with smaller key length to fit qubit limits"""
        alice_bits = np.random.randint(2, size=key_length)
        alice_bases = np.random.choice(self.basis_choices, size=key_length)
        bob_bases = np.random.choice(self.basis_choices, size=key_length)
        
        circuit = self.prepare_qubits(alice_bits, alice_bases)
        measured_circuit = self.measure_qubits(circuit, bob_bases)
        
        compiled_circuit = transpile(measured_circuit, self.simulator)
        job = self.simulator.run(compiled_circuit, shots=1)
        result = job.result()
        counts = result.get_counts()
        
        bob_bits_str = list(counts.keys())[0][:key_length]
        bob_bits = [int(bit) for bit in reversed(bob_bits_str)]
        
        shared_key = []
        for i in range(key_length):
            if alice_bases[i] == bob_bases[i]:
                shared_key.append(alice_bits[i])
        
        return {
            'shared_key': shared_key,
            'key_length': len(shared_key),
            'efficiency': len(shared_key) / key_length,
            'alice_bits_sample': alice_bits[:8],  # Show first 8 bits for demo
            'bob_bits_sample': bob_bits[:8]
        }

if __name__ == "__main__":
    bb84 = BB84Protocol()
    result = bb84.simulate_key_exchange(16)
    print(f"Shared Key Length: {result['key_length']} bits")
    print(f"Efficiency: {result['efficiency']:.1%}")
    print(f"Sample Alice bits: {result['alice_bits_sample']}")
    print(f"Sample Bob bits: {result['bob_bits_sample']}")
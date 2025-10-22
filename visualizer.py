import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit

class QuantumVisualizer:
    def __init__(self):
        plt.style.use('dark_background')
    
    def plot_quantum_circuit(self, circuit, title="Quantum Circuit"):
        try:
            # Try to use the circuit drawer
            return circuit.draw(output='mpl', style={'backgroundcolor': '#000000'})
        except:
            # Fallback: just print the circuit
            print("Circuit visualization not available, printing text version:")
            print(circuit)
            return None
    
    def plot_encryption_comparison(self, original, encrypted, decrypted):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        axes[0].imshow(original)
        axes[0].set_title('Original Image', color='white')
        axes[0].axis('off')
        
        axes[1].imshow(encrypted, cmap='hot')
        axes[1].set_title('Quantum Encrypted', color='white')
        axes[1].axis('off')
        
        axes[2].imshow(decrypted)
        axes[2].set_title('Decrypted Image', color='white')
        axes[2].axis('off')
        
        plt.tight_layout()
        return fig
    
    def plot_entanglement_demo(self):
        bell_circuit = QuantumCircuit(2, 2)
        bell_circuit.h(0)
        bell_circuit.cx(0, 1)
        bell_circuit.measure_all()
        
        fig = self.plot_quantum_circuit(bell_circuit, "Bell State - Quantum Entanglement")
        return fig, bell_circuit

if __name__ == "__main__":
    visualizer = QuantumVisualizer()
    print("✅ Quantum Visualizer ready!")
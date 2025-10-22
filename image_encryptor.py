import numpy as np
from quantum_rng import QuantumRNG

class QuantumImageEncryptor:
    def __init__(self):
        self.qrng = QuantumRNG()
    
    def create_sample_image(self):
        """Create a beautiful quantum fractal image"""
        x = np.linspace(-2, 2, 300)
        y = np.linspace(-2, 2, 300)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        
        c = Z.copy()
        fractal = np.zeros(Z.shape)
        for i in range(50):
            Z = Z**2 + c
            fractal += (np.abs(Z) < 10)
        
        fractal_normalized = (fractal / fractal.max() * 255).astype(np.uint8)
        fractal_rgb = np.stack([fractal_normalized]*3, axis=-1)
        
        return fractal_rgb
    
    def quantum_xor_encrypt(self, image_array, quantum_key):
        """Encrypt image using quantum-generated key"""
        flat_array = image_array.flatten()
        
        key_stream = []
        while len(key_stream) < len(flat_array):
            new_key = self.qrng.generate_quantum_key(256)
            key_stream.extend(list(new_key))
        
        key_stream = key_stream[:len(flat_array)]
        encrypted_array = np.bitwise_xor(flat_array, key_stream[:len(flat_array)])
        
        return encrypted_array.reshape(image_array.shape)

if __name__ == "__main__":
    encryptor = QuantumImageEncryptor()
    print("✅ Quantum Image Encryptor ready!")
import random
import math
from Crypto.Util import number

class Paillier:
    def __init__(self, bit_length=1024):
        # Generate two distinct prime numbers
        self.p = number.getPrime(bit_length // 2)
        self.q = number.getPrime(bit_length // 2)

        # Compute n and λ (lambda)
        self.n = self.p * self.q
        self.n_squared = self.n * self.n
        self.lambd = lcm(self.p - 1, self.q - 1)

        # Compute g
        self.g = self.n + 1

        # Public key (n, g)
        self.public_key = (self.n, self.g)

        # Private key (λ)
        self.private_key = self.lambd

    def encrypt(self, m):
        """Encrypts the integer m using the public key."""
        if m < 0 or m >= self.n:
            raise ValueError("Message must be in the range [0, n).")

        # Randomly choose r in Z_n*
        r = random.randint(1, self.n - 1)
        while math.gcd(r, self.n) != 1:
            r = random.randint(1, self.n - 1)

        # Compute ciphertext
        c = (pow(self.g, m, self.n_squared) * pow(r, self.n, self.n_squared)) % self.n_squared
        return c

    def decrypt(self, c):
        """Decrypts the ciphertext c using the private key."""

        # L function
        def L(x):
            return (x - 1) // self.n

        # Compute m
        u = pow(c, self.private_key, self.n_squared)
        m = (L(u) * number.inverse(self.private_key, self.n)) % self.n
        return m

    def add_encrypted(self, c1, c2):
        """Performs addition on two ciphertexts c1 and c2."""
        return (c1 * c2) % self.n_squared


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# Example usage
if __name__ == "__main__":
    # Initialize Paillier encryption scheme
    paillier = Paillier(bit_length=128)  # Use smaller bit length for demonstration

    # Encrypt two integers
    m1 = 15
    m2 = 25
    ciphertext1 = paillier.encrypt(m1)
    ciphertext2 = paillier.encrypt(m2)

    print(f"Ciphertext of {m1}: {ciphertext1}")
    print(f"Ciphertext of {m2}: {ciphertext2}")

    # Perform addition on encrypted integers
    encrypted_sum = paillier.add_encrypted(ciphertext1, ciphertext2)
    print(f"Encrypted sum: {encrypted_sum}")

    # Decrypt the result of the addition
    decrypted_sum = paillier.decrypt(encrypted_sum)
    print(f"Decrypted sum: {decrypted_sum}")

    # Verify that it matches the sum of the original integers
    original_sum = m1 + m2
    print(f"Original sum: {original_sum}")
    assert decrypted_sum == original_sum, "Decrypted sum does not match the original sum!"

    print("Test passed successfully!")
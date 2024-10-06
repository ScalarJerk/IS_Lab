import random
from Crypto.Util import number


class RSA:
    def __init__(self, bit_length=1024):
        # Generate two distinct prime numbers
        self.p = number.getPrime(bit_length)
        self.q = number.getPrime(bit_length)

        # Compute n and λ (lambda)
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)

        # Choose e
        self.e = 65537  # Common choice for e
        if self.gcd(self.e, self.phi_n) != 1:
            raise ValueError("e must be coprime to phi(n)")

        # Compute d (the modular inverse of e mod φ(n))
        self.d = number.inverse(self.e, self.phi_n)

        # Public key (e, n) and Private key (d, n)
        self.public_key = (self.e, self.n)
        self.private_key = (self.d, self.n)

    def gcd(self, a, b):
        """Compute the greatest common divisor using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

    def encrypt(self, m):
        """Encrypts a message using the public key."""
        if m < 0 or m >= self.n:
            raise ValueError("Message must be in the range [0, n).")

        # Compute ciphertext
        c = pow(m, self.e, self.n)
        return c

    def decrypt(self, c):
        """Decrypts a ciphertext using the private key."""
        m = pow(c, self.d, self.n)
        return m

    def multiply_encrypted(self, c1, c2):
        """Performs multiplication on two ciphertexts c1 and c2."""
        return (c1 * c2) % self.n


# Example usage
if __name__ == "__main__":
    # Initialize RSA encryption scheme
    rsa = RSA()

    # Encrypt two integers
    m1 = 7
    m2 = 3
    ciphertext1 = rsa.encrypt(m1)
    ciphertext2 = rsa.encrypt(m2)

    print(f"Ciphertext of {m1}: {ciphertext1}")
    print(f"Ciphertext of {m2}: {ciphertext2}")

    # Perform multiplication on encrypted integers
    encrypted_product = rsa.multiply_encrypted(ciphertext1, ciphertext2)
    print(f"Encrypted product: {encrypted_product}")

    # Decrypt the result of the multiplication
    decrypted_product = rsa.decrypt(encrypted_product)
    print(f"Decrypted product: {decrypted_product}")

    # Verify that it matches the product of the original integers
    original_product = m1 * m2
    print(f"Original product: {original_product}")
    assert decrypted_product == original_product, "Decrypted product does not match the original product!"

# buggy af code

'''
DigiRights Inc. is a leading provider of digital content, including e-books, movies, and music.
The company has implemented a secure digital rights management (DRM) system using the
ElGamal cryptosystem to protect its valuable digital assets. Implement a Python-based
centralized key management and access control service that can:
• Key Generation: Generate a master public-private key pair using the ElGamal
cryptosystem. The key size should be configurable (e.g., 2048 bits).
• Content Encryption: Provide an API for content creators to upload their digital content and
have it encrypted using the master public key.
• Key Distribution: Manage the distribution of the master private key to authorized
customers, allowing them to decrypt the content.
• Access Control: Implement flexible access control mechanisms, such as:
o Granting limited-time access to customers for specific content
o Revoking access to customers for specific content
o Allowing content creators to manage access to their own content
• Key Revocation: Implement a process to revoke the master private key in case of a security
breach or other emergency.
Database and Domain Name Servers (DNS)
• Key Renewal: Automatically renew the master public-private key pair at regular intervals
(e.g., every 24 months) to maintain the security of the DRM system.
• Secure Storage: Securely store the master private key, ensuring that it is not accessible to
unauthorized parties.
• Auditing and Logging: Maintain detailed logs of all key management and access control
operations to enable auditing and troubleshooting.
'''

from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Random.random import randrange
import os
import pickle
import base64
import json
from datetime import datetime, timedelta


class KeyManager:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.master_private_key = None
        self.master_public_key = None

    def generate_master_key_pair(self):
        key = ElGamal.generate(self.key_size, get_random_bytes)
        self.master_private_key = key
        self.master_public_key = key.publickey()

        # Save the keys to files
        with open("master_private_key.pem", "wb") as priv_file, open("master_public_key.pem", "wb") as pub_file:
            pickle.dump(self.master_private_key, priv_file)
            pickle.dump(self.master_public_key, pub_file)

        print("Master key pair generated and saved.")

    def load_keys(self):
        # Load keys from files
        if os.path.exists("master_private_key.pem") and os.path.exists("master_public_key.pem"):
            with open("master_private_key.pem", "rb") as priv_file, open("master_public_key.pem", "rb") as pub_file:
                self.master_private_key = pickle.load(priv_file)
                self.master_public_key = pickle.load(pub_file)
            print("Keys loaded successfully.")
        else:
            print("Key files not found. Generating new keys.")
            self.generate_master_key_pair()


class ContentManager:
    def encrypt_content(self, content):
        public_key = key_manager.master_public_key
        content_hash = SHA256.new(content).digest()

        # Encrypt the content hash
        encrypted_content = public_key.encrypt(content_hash, randrange(1, public_key.p - 1))

        # Save the encrypted content
        with open("encrypted_content.bin", "wb") as enc_file:
            enc_file.write(base64.b64encode(encrypted_content[0]))

        print("Content encrypted and saved to 'encrypted_content.bin'.")


class AccessControl:
    def __init__(self):
        self.access_file = "access_control.json"
        self.access_data = self.load_access_data()

    def load_access_data(self):
        if os.path.exists(self.access_file):
            with open(self.access_file, "r") as file:
                return json.load(file)
        return {}

    def save_access_data(self):
        with open(self.access_file, "w") as file:
            json.dump(self.access_data, file)

    def grant_access(self, user_id, duration_days=1):
        expiry_date = (datetime.now() + timedelta(days=duration_days)).isoformat()
        self.access_data[user_id] = {
            "access_granted": True,
            "expires_at": expiry_date
        }
        self.save_access_data()
        print(f"Access granted to {user_id} until {expiry_date}")
        log_action(f"Granted access", user_id)

    def revoke_access(self, user_id):
        if user_id in self.access_data:
            self.access_data[user_id]["access_granted"] = False
            self.save_access_data()
            print(f"Access revoked for {user_id}")
            log_action(f"Revoked access", user_id)
        else:
            print(f"No access found for user {user_id}")

    def check_access(self, user_id):
        if user_id in self.access_data:
            access_info = self.access_data[user_id]
            if access_info["access_granted"] and datetime.fromisoformat(access_info["expires_at"]) > datetime.now():
                print(f"{user_id} has access until {access_info['expires_at']}")
                return True
        print(f"{user_id} does not have access or access expired.")
        return False


def revoke_master_key():
    if os.path.exists("master_private_key.pem"):
        os.remove("master_private_key.pem")
        print("Master private key revoked.")
        log_action("Master private key revoked")
    else:
        print("No master private key found.")

    # Generate new key pair
    key_manager.generate_master_key_pair()
    log_action("Generated new master key pair")


def renew_master_key():
    key_manager.generate_master_key_pair()
    print("Master key renewed.")
    log_action("Master key renewed")


def log_action(action, user_id=None):
    with open("access_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}")
        if user_id:
            log_file.write(f" for user: {user_id}")
        log_file.write("\n")


def menu():
    while True:
        print("\n--- DigiRights DRM Menu ---")
        print("1. Generate Master Key Pair")
        print("2. Load Existing Keys")
        print("3. Encrypt Content")
        print("4. Grant Access to User")
        print("5. Revoke Access for User")
        print("6. Check User Access")
        print("7. Revoke Master Key")
        print("8. Renew Master Key")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key_manager.generate_master_key_pair()
        elif choice == '2':
            key_manager.load_keys()
        elif choice == '3':
            filename = input("Enter the content filename to encrypt: ")
            if os.path.exists(filename):
                with open(filename, "rb") as file:
                    content = file.read()
                content_manager.encrypt_content(content)
            else:
                print("File not found.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            duration_days = int(input("Enter duration in days: "))
            access_control.grant_access(user_id, duration_days)
        elif choice == '5':
            user_id = input("Enter user ID: ")
            access_control.revoke_access(user_id)
        elif choice == '6':
            user_id = input("Enter user ID: ")
            access_control.check_access(user_id)
        elif choice == '7':
            revoke_master_key()
        elif choice == '8':
            renew_master_key()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Initialize objects
key_manager = KeyManager()
content_manager = ContentManager()
access_control = AccessControl()

# Start the menu-driven program
menu()

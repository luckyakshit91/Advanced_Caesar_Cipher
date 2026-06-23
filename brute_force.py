from caesar_cipher import decrypt

def brute_force_attack(ciphertext):
    results = []

    for key in range(26):
        text = decrypt(ciphertext, key)
        results.append(f"Key {key}: {text}")

    return "\n".join(results)
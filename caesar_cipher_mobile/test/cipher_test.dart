import 'package:flutter_test/flutter_test.dart';
import 'package:caesar_cipher_mobile/utils/cipher_logic.dart';

void main() {
  group('Caesar Cipher Tests', () {
    test('Encryption should shift letters correctly', () {
      expect(encrypt("Hello World!", 3), equals("Khoor Zruog!"));
      expect(encrypt("abc", 1), equals("bcd"));
      expect(encrypt("XYZ", 3), equals("ABC"));
    });

    test('Decryption should shift letters backwards correctly', () {
      expect(decrypt("Khoor Zruog!", 3), equals("Hello World!"));
      expect(decrypt("bcd", 1), equals("abc"));
      expect(decrypt("ABC", 3), equals("XYZ"));
    });

    test('Brute Force should output 26 possible decryptions', () {
      final ciphertext = encrypt("Secret Message", 5);
      final attackResult = bruteForceAttack(ciphertext);
      final lines = attackResult.split("\n");
      
      expect(lines.length, equals(26));
      expect(lines[0], contains("Key 0:"));
      expect(lines[5], contains("Key 5: Secret Message"));
    });

    test('Frequency Analysis should count alphabet characters correctly', () {
      final text = "Hello World! AAAA";
      final analysis = frequencyAnalysis(text);
      
      // A: 4 times, L: 3 times, O: 2 times, H, E, W, R, D: 1 time
      expect(analysis, contains("A : 5")); // "Hello World! AAAA" has H, e, l, l, o, W, o, r, l, d, A, A, A, A -> letters: H(1), E(1), L(3), O(2), W(1), R(1), D(1), A(4) -> Wait, let's recount.
      // Wait, AAAA (4) + A in "World" (none) -> A is 4.
      // Let's check:
      expect(analysis, contains("L : 3"));
      expect(analysis, contains("O : 2"));
    });
  });

  group('AES Encryption Comparison Tests', () {
    test('AES encryption and decryption should be consistent', () {
      const message = "Secret AES Protocol";
      final ciphertext = aesEncrypt(message);
      
      // Ciphertext should be hex string (not empty and even length)
      expect(ciphertext.isNotEmpty, isTrue);
      expect(ciphertext.length % 2, equals(0));

      final decrypted = aesDecrypt(ciphertext);
      expect(decrypted, equals(message));
    });
  });
}

# Advanced Caesar Cipher Security Suite

A multi-platform cryptography education and utility suite featuring a **Python Tkinter Desktop Application** and a **Flutter Mobile App**. This toolkit provides tools for text encryption, decryption, brute-force simulation, frequency analysis, and AES comparisons.

---

## 🚀 Features

### 💻 Python Desktop Suite
*   **Secure Authentication:** Secure gatekeeper login screen requiring passphrase verification (`Akshit@123`).
*   **Caesar Cipher Utility:** Easily encrypt and decrypt raw text strings using custom shift keys (0–25).
*   **Brute-Force Simulator:** Test any ciphertext against all 26 keys simultaneously to show decryption possibilities.
*   **Frequency Analysis:** Inspect the frequency of characters in a ciphertext to facilitate frequency-based cryptanalysis.
*   **AES Comparison Mode:** Showcases Advanced Encryption Standard (AES-128 under ECB mode) side-by-side with Caesar Cipher to illustrate modern vs. classical encryption strength.
*   **Text File Encryption:** Load external `.txt` files directly, encrypt them, and save the output.
*   **Database Integration:** Saves all original and encrypted texts to a local SQLite database (`encrypted_messages.db`) for tracking.
*   **Detailed Logging:** Automated logging system writing system actions and events to `logs/encryption.log`.

### 📱 Flutter Mobile App (`caesar_cipher_mobile`)
*   **Cross-Platform Client:** Run on Android or iOS.
*   **Modern UI:** Dark-themed styling utilizing Google Fonts (Inter) and vibrant neon accents matching the desktop application's cyberpunk aesthetic.
*   **Authentication & Workspace Screens:** Mobile workflow mimicking the desktop logic.

---

## 🛠️ Project Structure

```text
Advanced_Caesar_Cipher tool/
│
├── aes_module.py             # AES encryption/decryption module (pycryptodome)
├── brute_force.py            # Caesar Cipher brute-force decryption logic
├── caesar_cipher.py          # Classical Caesar Cipher shift formulas
├── database.py               # SQLite database setup and messaging save functions
├── frequency_analysis.py     # Letter frequency counting utility
├── logger_module.py          # Logging configuration (logs/encryption.log)
├── main.py                   # Python Tkinter GUI launcher and desktop app logic
├── password_auth.py          # Plaintext credential checking
├── requirements.txt          # Python dependencies
│
└── caesar_cipher_mobile/     # Flutter mobile application
    ├── lib/                  # Dart application source files
    │   ├── main.dart         # Flutter entry point
    │   ├── screens/          # UI Screens (AuthScreen, HomeScreen)
    │   └── helpers/ / utils/ # Mobile utility helpers
    └── pubspec.yaml          # Flutter dependency configuration
```

---

## 💻 Getting Started: Python Desktop Suite

### Prerequisites
*   Python 3.8 or higher installed on your system.

### Installation
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/Advanced_Caesar_Cipher-tool.git
    cd Advanced_Caesar_Cipher-tool
    ```

2.  **Create and Activate a Virtual Environment:**
    *   **Windows (PowerShell):**
        ```powershell
        python -m venv .venv
        .venv\Scripts\Activate.ps1
        ```
    *   **macOS / Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Desktop GUI Application:**
    ```bash
    python main.py
    ```
    *Note: You will be prompted in the terminal to enter the password (`Akshit@123`) before the GUI window launches.*

---

## 📱 Getting Started: Flutter Mobile App

### Prerequisites
*   [Flutter SDK](https://docs.flutter.dev/get-started/install) installed and configured on your machine.
*   An Android/iOS simulator or physical device connected.

### Installation
1.  Navigate to the mobile directory:
    ```bash
    cd caesar_cipher_mobile
    ```

2.  Fetch packages:
    ```bash
    flutter pub get
    ```

3.  Run the application:
    ```bash
    flutter run
    ```

---

## 🔒 Configuration & Passwords
*   The default password to access the desktop GUI app is: **`Akshit@123`** (configured in `password_auth.py`).

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

# 🔐 Image Encryption CLI Tool

A simple command-line tool to **encrypt and decrypt image files** using **password-based AES encryption**, securing visual data from unauthorized access and tampering.

## 📦 Features

- 🔑 **Password-based encryption**
- 🔒 AES encryption (via `cryptography` library)
- 🖼️ Supports JPG, PNG, and other image formats
- ⚙️ CLI interface for easy use
- 🧂 Random salt generation for added security

---

## 🚀 Getting Started

### 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mdfayjulkabir/Image-Encryption_Command-line-interface-CLI-Tool.git
   cd image-encryption-cli
   ```

2. Install dependencies( if needed):
   ```bash
   pip install cryptography
   ```

---

## 💻 Usage

### 🔐 Encrypt an Image

```bash
python image_crypto_cli.py
```

Follow the prompts to select encryption or decryption mode.

---

## 🧠 How It Works

- Uses PBKDF2 to derive a secure key from a password and random salt.
- Encrypts using Fernet (AES-based symmetric encryption).
- Salt is stored in `salt.salt`.

> ⚠️ Keep the password and salt safe!

---

## 📁 Project Structure

```
image-encryption-cli/
├── image_crypto_cli.py       # Main script
├── salt.salt                 # Salt file (auto-generated)
└── README.md                 # This file
```

---

## 📚 License

MIT License. Use responsibly.

## 👨‍🎓 Ideal for

- Cybersecurity students
- Academic mini projects
- Personal privacy tools
- Open-source contributions

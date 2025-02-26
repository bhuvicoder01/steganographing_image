# Secure Data Hiding in Images Using Steganography

This project is a secure steganography tool developed as part of the IBM SkillBuild Cybersecurity Internship. It allows users to hide sensitive data within images using Least Significant Bit (LSB) substitution, combined with AES-256 encryption for added security. Featuring a graphical user interface (GUI) built with Tkinter, the tool offers an intuitive way to embed and extract messages, manage encryption keys, and ensure covert communication for cybersecurity applications.

---

## Table of Contents
- [Project Description](#project-description)
- [Technology Used](#technology-used)
- [Installation](#installation)
- [Usage](#usage)
- [Tips](#tips)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Description
This tool enables users to conceal confidential messages within images, making the hidden data undetectable to the naked eye and recoverable only with the correct encryption key. It combines LSB steganography for data hiding with AES-256 encryption for confidentiality, providing a dual-layer security approach. Developed for the IBM SkillBuild Cybersecurity Internship, it showcases practical applications in covert communication and data protection.

---

## Technology Used
- **Programming Language:** Python  
- **Libraries:**  
  - **Pillow:** For image processing and manipulation  
  - **Cryptography:** For AES-256 encryption  
  - **Tkinter:** For the graphical user interface (GUI)  
  - **Pyperclip:** For clipboard functionality (key copying)  
- **Steganography Technique:** Least Significant Bit (LSB) substitution  

---

## Installation
Follow these steps to set up the project on your local machine:

1. **Install Python:** Ensure Python 3.6 or higher is installed. Download from [python.org](https://www.python.org/downloads/) if needed.
2. **Install Required Libraries:** Open a terminal and run:
   ```bash
   pip install pillow cryptography pyperclip
   ```
   *Note:* Tkinter is included with Python, but on Linux, you may need to install `tk-dev` or `libtk-dev` (e.g., `sudo apt-get install python3-tk`).
3. **Clone the Repository:** Download the project files:
   ```bash
   git clone https://github.com/yourusername/steganography-project
   ```
   Replace `yourusername` with your actual GitHub username.
4. **Run the Application:** Navigate to the project directory and start the tool:
   ```bash
   cd steganography-project
   python app.py
   ```

---

## Usage
The GUI provides a simple interface for embedding and extracting messages:

1. **Select an Image:** Click "Browse" to choose an image (PNG or BMP recommended).
2. **Enter the Message:** Type the message you want to hide in the "Message" field.
3. **Manage the Encryption Key:**
   - **Generate Key:** Click "Generate Key" to create a random 32-byte key, shown as a 64-character hex string, and copied to the clipboard.
   - **Copy Key:** Click "Copy Key" to copy the current key from the key field to the clipboard.
   - **Manual Entry:** Optionally, enter a 32-byte key or a 64-character hex string manually.
4. **Embed Message:** Click "Embed Message" to hide the encrypted message in the image. The stego-image is saved with a "stego_" prefix (e.g., `stego_image.png`).
5. **Extract Message:** Click "Extract Message," select the stego-image, ensure the correct key is entered, and view the recovered message in a popup.

---

## Tips
- **Image Selection:** Use high-resolution images (e.g., 512x512 or larger) to maximize data hiding capacity.
- **Key Management:** Save your encryption key securely (e.g., paste it from the clipboard into a text file). The hex format makes it easier to handle.
- **Stego-Image Quality:** LSB substitution ensures minimal visual changes, while encryption keeps the data unreadable without the key.

---

## Contributing
This project was created for the IBM SkillBuild Cybersecurity Internship and is not currently accepting external contributions. For suggestions or feedback, please contact the maintainer (see [Contact](#contact)).

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions, issues, or feedback:
- **Email:** cebhuvneshsingh@gmail.com  
---
```

---

### **Instructions**
1. **Copy the Content:** Copy the entire text above.
2. **Create `README.md`:** In your project directory (`/workspaces/steganographing_image/` or your local repo), create a file named `README.md`.
3. **Paste and Edit:** Paste the content into `README.md`, then update the following placeholders:
   - Replace `yourusername` with your actual GitHub username in the clone URL and issues link.
   - Replace `[your.email@example.com]` with your actual email address.
4. **Save and Commit:** Add the file to your Git repository:
   ```bash
   git add README.md
   git commit -m "Add README file"
   git push origin main
   ```

---

### **Notes**
- **Markdown Format:** The content uses Markdown (`.md`) for GitHub compatibility, with headers, lists, and code blocks for readability.
- **Completeness:** It covers all required sections from your template and adds practical details for users.
- **Customization:** Feel free to adjust the email or add a personal touch (e.g., a thank-you note to IBM SkillBuild mentors).

This README should serve as a strong companion to your project submission, making it easy for evaluators or users to understand and use your steganography tool. Let me know if you need further tweaks!

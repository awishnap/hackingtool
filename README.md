# HackingTool 🔧

> A fork of [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) — All in One Hacking Tool for Linux

![GitHub stars](https://img.shields.io/github/stars/Z4nzu/hackingtool?style=social)
![GitHub forks](https://img.shields.io/github/forks/Z4nzu/hackingtool?style=social)
![GitHub issues](https://img.shields.io/github/issues/Z4nzu/hackingtool)
![License](https://img.shields.io/github/license/Z4nzu/hackingtool)

## ⚠️ Disclaimer

This tool is intended for **educational and ethical use only**. The authors are not responsible for any misuse or damage caused by this program. Use it only on systems you own or have explicit permission to test.

## 📋 Features

- Anonymous surfing tools
- Information gathering tools
- Wordlist generators
- Wireless attack tools
- SQL injection tools
- Phishing attack tools
- Web attack tools
- Post exploitation tools
- Forensic tools
- Payload creation tools
- Exploit framework tools
- Reverse engineering tools
- DDOS attack tools
- Remote administration tools (RAT)
- XSS attack tools
- Steganography tools
- SocialMedia brute-forcing tools
- Android hacking tools
- IDN homograph attack tools
- Email spoofing tools
- Hash cracking tools
- Wifi deauthentication tools
- Bluetooth hacking tools
- Bash obfuscation tools
- Telegram bots tools
- Twilio SMS tools
- Discord tools
- Termux hacking tools

## 🛠️ Requirements

- Python 3.6+
- Linux-based OS (Kali Linux, Parrot OS, Ubuntu, etc.)
- Git
- Root privileges (for some tools)

## 🚀 Installation

### Method 1: Clone and Run

```bash
git clone https://github.com/yourusername/hackingtool.git
cd hackingtool
pip3 install -r requirements.txt
sudo python3 hackingtool.py
```

### Method 2: Docker

```bash
docker build -t hackingtool .
docker run -it hackingtool
```

## 🐳 Docker Support

This project includes Docker support for running in an isolated environment.

```bash
# Build the image
docker build -t hackingtool .

# Run interactively
docker run -it --rm hackingtool
```

## 🤝 Contributing

Contributions are welcome! Please read our [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) before submitting.

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

### Requesting a New Tool

Want a new tool added? Use our [Tool Request Template](.github/ISSUE_TEMPLATE/tool_request.md).

### Reporting Bugs

Found a bug? Please use our [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md).

## 📝 Personal Notes

> **Note (personal fork):** I'm using this primarily to study information gathering and network scanning techniques in my home lab. The tools I use most frequently are in the *Information Gathering* and *Wireless Attack* categories. Tested on Kali Linux 2024.1.
>
> **Home lab setup:** Running on a dedicated Raspberry Pi 4 (8GB) with Kali Linux. For wireless testing I use an Alfa AWUS036ACH adapter. Note that on the Pi 4, some tools can be slow to load — running `sudo python3 hackingtool.py` with the `--no-check-update` flag (if available) helps speed up startup noticeably.
>
> **Tip for Raspberry Pi users:** If you hit permission errors with wireless tools, make sure your user is in the `netdev` group: `sudo usermod -aG netdev $USER`.

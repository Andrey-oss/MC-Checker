# MC-Checker v1.0-beta

A simple Minecraft server status checker built using Python and the [mcsrvstat.us](https://api.mcsrvstat.us/) API.

---

## Features

- Checks online status of **Minecraft Java** and **Bedrock** servers (WIP)
- Displays key server info (players, MOTD, version, etc.)
- Lightweight and fast
- CLI-based with ASCII logo
- Modular codebase (`core/` package)

---

## Requirements

- Python 3.7+
- Internet connection

## Install required packages with:

```bash
pip install requests
```

## How to Run

```bash
python3 mc-checker.py
```

Then enter the target Minecraft server address when prompted:

```
Target server: hypixel.net
```

## Project Structure

```
MC-Checker/
├── mc-checker.py            # Main entry point
├── core/
│   ├── logo.py              # ASCII logo printer
│   ├── main.py              # Server info parser and printer
│   ├── probe_request.py     # Initial API probe request
│   └── server_checker.py    # Service checker
├── LICENSE
├── README.md
└── CHANGELOG
```

## API Reference

* Java: https://api.mcsrvstat.us/2/<domain>
* Bedrock: https://api.mcsrvstat.us/bedrock/2/<domain>

## License

This project is licensed under the MIT License. See LICENSE for details.

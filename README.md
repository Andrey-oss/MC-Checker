# MC-Checker v1.1

A simple Minecraft server status checker built using Python and the [mcsrvstat.us](https://api.mcsrvstat.us/) API.

---

## Features

- Checks online status of **Minecraft Java** and **Bedrock** servers
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
pip3 install -r requirements.txt
```

## How to Run

```bash
python3 mc-checker.py
```

Then enter the target Minecraft server address when prompted:

```
Target server: hypixel.net
```

## Install via docker

1. Build docker container:

```bash
docker build -t mc_checker .
```

2. Run the tool:

```bash
docker run --rm -it mc_checker
```

## Future development

If you want to develop this project by yourself, you may use automated script which creates virtualenv with all dependencies:

```bash
bash init_venv.sh
```

## Project Structure

```
MC-Checker/
├── mc_checker.py            # Main entry point
├── core/
│   ├── logo.py              # ASCII logo printer
│   ├── main.py              # Server info parser and printer
│   ├── probe_request.py     # Initial probe request
├── LICENSE
├── README.md
├── requirements.txt
└── CHANGELOG
```

## API Reference

* Java: https://api.mcsrvstat.us/2/<domain>
* Bedrock: https://api.mcsrvstat.us/bedrock/2/<domain>

## License

This project is licensed under the MIT License. See LICENSE for details.

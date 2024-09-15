<p align="center"> <h3 align="center">Shogi Encryption</h3> <p align="center"> A file encoding/decoding project using Shogi moves to represent bits of data. It encodes file data into Shogi KIF format, and decodes it back into the original file. <br /> <br /> </p> </p>

---
<details open="open"> <summary>Table of Contents</summary> <ol> <li><a href="#about">About</a></li> <li><a href="#built-with">Built With</a></li> <li><a href="#usage">Usage</a></li> <li><a href="#contributing">Contributing</a></li> </ol> </details>

---

## About

Shogi Encryption encodes a file's binary data into a series of legal Shogi moves. The project utilizes Shogi's game rules to represent bits, converting binary data into Shogi's KIF format (a move notation for Shogi). Each move corresponds to a sequence of bits, and the legal move pool is dynamically updated based on the state of the game. The decoded KIF file can be converted back into the original file by reversing the process. Based on <text><a href="https://github.com/WintrCat/chessencryption/tree/master">Chess Encryption</a></text>

### Features

- File Encoding: Converts any file into a series of Shogi moves encoded in KIF format.
- File Decoding: Decodes the KIF file back to its original binary data.
- Handling Skipped Bits: If certain bits cannot be encoded into moves, they are stored separately and reinserted during decoding

---

## Built with

- <text> <a href="https://python.org/">Python</a></text>- Primary programming language.

- <text> <a href="https://github.com/gunyarakun/python-shogi">python-shog</a></text> - Python package to simulate Shogi moves and validate legal move states.

- <text> <a href="https://github.com/tqdm/tqdm">TQDM</a></text>- Progress bar for tracking encoding/decoding progress.

---

## Usage

### Setup the project locally:

1. Clone the repository:

```bash
git clone https://github.com/theg1239/shogiencryption
```
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Encoding a file into Shogi .KIF format:

1. Run the `encode.py` script:

```python
python encode.py <input_file> <output_kif_file>
```

2. The script will read the input file, encode the binary data into Shogi moves, and save the moves in KIF format to the output file. Any bits that cannot be encoded into moves will be saved as `SKIPPED_BITS` in the KIF file.

### Decoding a .KIF file back into the original file:

1. Run the `decode.py` script:

```python
python decode.py <input_kif_file> <output_file>
```

2. The script will read the KIF file, decode the Shogi moves back into binary data, and reconstruct the original file. Any skipped bits from the encoding process will be reinserted at the correct positions.

---

## Contributing

Contributions to improve this project are welcome. If you have any suggestions or bug fixes, feel free to open a pull request. Your contributions will be reviewed and integrated into the project if they improve the functionality or structure.


import argparse
from math import log2
import shogi
from tqdm import tqdm

def to_binary_string(value: int, length: int) -> str:
    return bin(value)[2:].zfill(length)

def moves_to_kif_string(moves_made):
    kif_content = []
    for i, move in enumerate(moves_made):
        kif_content.append(f"{i+1}. {move}")
    return '\n'.join(kif_content)

def encode(input_file: str, output_file: str):
    with open(input_file, 'rb') as f:
        file_bytes = f.read()
    file_bits = ''.join(f'{byte:08b}' for byte in file_bytes)
    total_bits = len(file_bits)
    bit_index = 0

    board = shogi.Board()
    moves_made = []
    skipped_bits = []  # list to store skipped bits

    with tqdm(total=total_bits, desc="Encoding Progress", unit="bit") as pbar:
        while bit_index < total_bits:
            legal_moves = list(board.legal_moves)
            num_moves = len(legal_moves)
            max_bits = int(log2(num_moves))

            if max_bits == 0:
                max_bits = 1

            bits_to_encode = file_bits[bit_index:bit_index + max_bits]

            if len(bits_to_encode) < max_bits:
                skipped_bits.append((bit_index, bits_to_encode))
                break

            move_index = int(bits_to_encode, 2)

            if move_index >= num_moves:
                skipped_bits.append((bit_index, bits_to_encode))
                bit_index += max_bits
                continue

            move = legal_moves[move_index]
            board.push(move)
            moves_made.append(move.usi())
            bit_index += max_bits

            pbar.update(max_bits)

            if board.is_game_over():
                board.reset()

    kif_content = moves_to_kif_string(moves_made)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(kif_content)
        if skipped_bits:
            f.write("\nSKIPPED_BITS: " + str(skipped_bits) + "\n")

    print(f"Encoding complete. Output written to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encode a file into Shogi KIF format.')
    parser.add_argument('input_file', help='The file to encode.')
    parser.add_argument('output_file', help='The output KIF file.')
    args = parser.parse_args()
    encode(args.input_file, args.output_file)

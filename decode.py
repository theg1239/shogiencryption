import argparse
from math import log2
import shogi
from tqdm import tqdm

def parse_kif_moves(kif_content: str) -> (list, list):
    """parse KIF content and extract the list of moves and skipped bits"""
    moves = []
    skipped_bits = []
    lines = kif_content.splitlines()
    for line in lines:
        if ". " in line:
            move_str = line.split(". ")[1].strip()
            moves.append(move_str)
        elif "SKIPPED_BITS" in line:
            skipped_bits_str = line.split(": ")[1].strip()
            skipped_bits = eval(skipped_bits_str)
    return moves, skipped_bits

def decode(input_file: str, output_file: str):
    with open(input_file, 'r', encoding='utf-8') as f:
        kif_content = f.read()

    moves, skipped_bits = parse_kif_moves(kif_content)

    board = shogi.Board()
    decoded_bits = ''

    with tqdm(total=len(moves), desc="Decoding Progress", unit="move") as pbar:
        for move in moves:
            legal_moves = list(board.legal_moves)
            num_moves = len(legal_moves)
            max_bits = int(log2(num_moves)) if num_moves > 1 else 1

            move_indices = {move_.usi(): idx for idx, move_ in enumerate(legal_moves)}
            move_index = move_indices.get(move)

            if move_index is None:
                print(f"Invalid move: {move}")
                continue

            bits = f'{move_index:0{max_bits}b}'
            decoded_bits += bits
            board.push(legal_moves[move_index])

            pbar.update(1)

            if board.is_game_over():
                board.reset()

    for index, bits in skipped_bits:
        decoded_bits = decoded_bits[:index] + bits + decoded_bits[index:]

    byte_array = bytearray()
    for i in range(0, len(decoded_bits), 8):
        byte_chunk = decoded_bits[i:i+8]
        byte_value = int(byte_chunk, 2)
        byte_array.append(byte_value)

    with open(output_file, 'wb') as f:
        f.write(byte_array)

    print(f"Decoding complete. Output written to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decode a Shogi KIF file back into the original file.')
    parser.add_argument('input_file', help='The KIF file to decode.')
    parser.add_argument('output_file', help='The output file.')
    args = parser.parse_args()
    decode(args.input_file, args.output_file)

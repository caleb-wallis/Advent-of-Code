
filename : str = "input.txt"
false_id_count : int = 0

def all_chunks_equal(s: str, chunk_size: int) -> bool:
    """Return True if s can be split into equal-size chunks and all chunks are identical."""
    # Number of chunks
    n = len(s) // chunk_size
    chunk = s[:chunk_size]
    # Compare each chunk directly
    for i in range(1, n):
        if s[i*chunk_size:(i+1)*chunk_size] != chunk:
            return False
    return True

with open(filename) as input_file:
    ranges = input_file.read().split(",")

    for ids in ranges:
        start, end = map(int, ids.split("-"))

        for id_value in range(start, end):
            s = str(id_value)
            L = len(s)

            # Try all even chunk sizes (must divide evenly)
            for chunk_size in range(L // 2, 0, -1):
                if L % chunk_size != 0:
                    continue  # split must be even

                if all_chunks_equal(s, chunk_size):
                    false_id_count += id_value
                    break  # Stop after the first valid split

print(false_id_count)

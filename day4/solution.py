from hasher import Hasher

input = 'iwrupvqb'

hasher = Hasher()
index = 0
part_one_found = False
part_two_found = False

while True:
    test_string = f"{input}{index}"
    hash_result = hasher.md5_hash(test_string)
    
    if not part_one_found and hasher.is_valid_hash(hash_result, leading_zeros=5):
        print(f"Part 1: {index}")
        part_one_found = True

    if not part_two_found and hasher.is_valid_hash(hash_result, leading_zeros=6):
        print(f"Part 2: {index}")
        part_two_found = True

    if part_one_found and part_two_found:
        break

    index += 1
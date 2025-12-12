
filename : str = "input.txt"
false_id_count : int = 0

with open (filename) as input:
    ranges = input.read().split(",")
    for ids in ranges:
        ids = ids.split("-")
        start = int(ids[0])
        end = int(ids[1])

        for id in range(start, end):
            str_id = str(id)
            mid_index = len(str_id) // 2  # Use integer division for the midpoint index
            first_half_id = str_id[:mid_index]
            second_half_id = str_id[mid_index:]
            if(first_half_id == second_half_id):
                false_id_count += id

print(false_id_count)
           
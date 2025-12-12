import textwrap

filename : str = "input.txt"
false_id_count : int = 0

# get input string
with open (filename) as input:
    # split into id ranges
    ranges = input.read().split(",")

    for ids in ranges:
        # get start and end of the range
        ids = ids.split("-")
        start = int(ids[0])
        end = int(ids[1])

        # loop through ids
        for id in range(start, end):
            str_id = str(id)
            split_size = len(str_id) // 2  # Use integer division for the midpoint index

            while(split_size >= 1):
                result = textwrap.wrap(str_id, split_size)
                # Convert the list to a set to remove duplicates
                unique_parts = set(result)
                    
                # If all parts are the same, the set will only have 1 element
                if(len(unique_parts) == 1):
                    false_id_count += id
                    break
                else:
                    # increase number of splits
                    split_size = split_size - 1

print(false_id_count)

# init variables
min : int = 0
max : int = 100
position : int = 50
count : int = 0

# input file
file : str = "input.txt"

# read the file
with open(file) as input:
  # loop over the file
  for instruction in input:
    # direction and val to turn the dial
    direction : str = instruction[0] 
    turn : int = int(instruction[1:])

    # calc full rotations and the remainer
    rotations, remainder = divmod(turn, max)
    count += rotations

    # make the remainder negative if turning left
    remainder = -remainder if direction == "L" else remainder

    # where the position will be (before transforming to fit the min and max)
    next_position = position + remainder

    # if position is on 0 (it has already been counted for)
    if position != 0:
        # if direction is left and is below min add 1 to count
        if direction == "L" and next_position <= min:
            count += 1
        # if direction is right and is above max add 1 to count
        elif direction == "R" and next_position >= max:
            count += 1

    # if next pos is negative it will make it positive with the correct amount of rotation
    position = next_position % 100

# print out count
print(count)


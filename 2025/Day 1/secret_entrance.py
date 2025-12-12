
# init variables
min : int = 0
max : int = 99
position : int = 50
count : int = 0
num_turns: int = 0

#file : str = "sample_input.txt"
file : str = "input.txt"

# read file
with open(file) as input:
  for instruction in input:
    direction : str = instruction[0] 
    turn : int = int(instruction[1:])

    # Turn in direction
    if(direction == "L"):
      position -= turn
    
    elif(direction == "R"):
      position += turn
    
    # Calibrate if past boundaries
    while(position > 99):
      position -= 100
    while(position < 0):
      position += 100

    # Count num times we hit pos 0
    if(position == 0):
        count += 1

    num_turns += 1
    #print(position)

print(count)
print(num_turns)
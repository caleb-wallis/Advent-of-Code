
total : int = 0
filename : str = "input.txt"

# get max voltage (2 batteries)
def find_max_joltage(bank: str) -> int:
    tens : int = int(bank[0])
    ones : int = int(bank[1])

    for i, ch in enumerate(bank[2:], start=2):
        num = int(ch)

        if num > tens and i != len(bank) - 1:   # not last char
            tens = num
            ones = int(bank[i + 1])
        elif num > ones:
            ones = num

    return tens * 10 + ones


with open(filename) as f:
     for battery in f:
         battery = battery.strip()

         # part 1
         total += find_max_joltage(battery)

print("Total:", total)

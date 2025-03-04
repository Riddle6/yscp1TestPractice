'''
This python file will input heights in inches and average sets of heights in inches, and print out the data.
'''
print("\nExample 1: Simple Heights in Inches\n")
heights = {}

# Collecting data points for our dictionary
heights[1] = 65.78331
heights[2] = 71.51521
heights[3] = 69.39874
heights[4] = 68.2166
heights[5] = 67.78781

#print("\n", heights, "\n")

for height, inches in heights.items():
    print(f"Item {height} is {inches} tall.")


print("\nExample 2: Average Heights in Inches for Sets of Data\n")

avgInches = {}

avgInches['Set 1'] = [65.78331, 71.51521, 69.39874]
avgInches['Set 2'] = [63.56331, 82.13597, 67.89543, 60.54321]
avgInches['Set 3'] = [55.87767, 69.35221, 84.86533, 72.88988]
avgInches['Set 4'] = [63.56331, 82.13597, 67.89543, 57.4646]
avgInches['Set 5'] = [65.78331, 71.51521, 69.39874]

#print(f"\n{avgInches}\n")

print("\nAverage Height Per Set in Inches:\n")

for set, inches in avgInches.items():
    # Sum() function adds a set of data together.
    # Len() function gives you the length of whatever is inside of the arguments.
    avg = sum(inches) / len(set)
    print(f"{set}'s average height is: {avg:.5f}")
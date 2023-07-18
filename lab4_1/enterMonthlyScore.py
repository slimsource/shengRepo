# Initialize a list with 12 elements set to 0
monthlyScore = [0] * 12

# Display the initial list
print("Initial monthly scores:", monthlyScore)

# Update scores for each month
for month in range(12):
    score = int(input(f"Enter score for month {month + 1}: "))
    monthlyScore[month] = score

# Display the updated list
print("Updated monthly scores:", monthlyScore)

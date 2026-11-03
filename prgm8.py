scores = [80, 90, 85, 75, 95]

total = sum(scores)

if len(scores) > 0:
    average = total / len(scores)
    print("Total:", total)
    print("Average:", average)
else:
    print("No scores available")

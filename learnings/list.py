score = []
for i in range(3):
    score.append(int(input("Enter your score: ")))
print(score)
updatedScore = [item + 5 if item < 40 else item for item in score]
print(updatedScore)
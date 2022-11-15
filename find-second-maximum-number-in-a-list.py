# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Constraints

#2 <= n <= 10

# Output Format

# -100 <= A[i] <= 100

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
# Explanation 0

# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

# sco = input("ent: ")
# print(sco)
# print(type(sco))

# num_of_scores = int(input("Enter the count of the scores: "))
# scores = [2, 3, 6, 6, 5,7,8,10,9]
# for i in range(num_of_scores):
#     score = input("Enter the score: ")
#     scores.append(int(score))




def second_max_value():
    num_of_scores = int(input())
    scores = list(map(int, input().split(' ')))
    max_value = -100
    second_max_value = -100
    for i in scores:
        if i > max_value:
            max_value = i
        
        for j in range(len(scores)):
            if second_max_value < scores[j] < max_value:
                second_max_value = scores[j]

    
    return second_max_value

print(second_max_value())

    

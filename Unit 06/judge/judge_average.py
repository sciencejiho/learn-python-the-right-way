# Given four scores (Korean, English, Mathematics, and Science) 
# as an input, return its average.
# There should be no prompt, and the average score must be integer
#
# Example 1:
# Input: 83 92 87 90
# Output: 88
#
# Example 2:
# Input: 32 53 22 95
# Output: 50

score_kor, score_en, score_math, score_sci = map(int, input().split())
print(int((score_kor + score_en + score_math + score_sci) / 4))

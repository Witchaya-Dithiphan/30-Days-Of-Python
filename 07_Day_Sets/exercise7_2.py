it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 2

# 1. Join A and B
C = A.union(B)
print(C)
# 2. Find A intersection B
C = A.intersection(B)
print(C)
# 3. Is A subset of B
print(A.issubset(B))
# 4. Are A and B disjoint sets
print(A.isdisjoint(B))
# 5. Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)
print(A_with_B)
print(B_with_A)
# 6. What is the symmetric difference between A and B
C = A.symmetric_difference(B)
print(C)
# 7. Delete the sets completely
del A
del B
del it_companies
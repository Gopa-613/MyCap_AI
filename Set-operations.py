#Python Program to Illustrate Different Set Operations.

s1={1,2,3,4,5,6}
s2={2,3,6,8,9,10}

union =s1.union(s2)
intersection = s1.intersection(s2)
s1_minus_s2 = s1.difference(s2)
s2_minus_s1 = s2.difference(s1)
symm_diff = s1.symmetric_difference(s2)

print("Set 1:", s1)
print("Set 2:", s2)
print("Union:", union)
print("Intersection:", intersection)
print("Set 1 - Set 2 :", s1_minus_s2)
print("Set 2 - Set 1 :", s2_minus_s1)
print("Symmetric Difference:", symm_diff)

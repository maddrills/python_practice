from prescription_data import *

trail_patients = ["Denise", "Eddie", "Frank", "Georgia",]

for patient in trail_patients:
    person_under_inspection = patients[patient]
    for infection in adverse_interactions:
        if infection.issubset(person_under_inspection):
            print(f"{patient} is in Danger")
            break
s1 = {1,2,3,4,5};
s2 = 5
print(s1)
print(s2)
# print(s2.issubset( s1))
print(s2 in s1)
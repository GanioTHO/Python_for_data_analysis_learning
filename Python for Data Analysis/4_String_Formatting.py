role = 'Data Analyst'
skill = "Pyhton"

# Write out 'Role: Data Analyst'

print('Role: ' + role)
# Role: Data Analyst

print("Role: {} Skill Required: {}".format(role, skill))
# Role: Data Analyst Skill Required: Pyhton

print(f"Role: {role} Skill required: {skill}")
# Role: Data Analyst Skill Required: Pyhton

print("Role: %s Skill Required: %s" % (role, skill))
# Role: Data Analyst Skill required: Pyhton

years_experience = '0123456789'
print(', '.join(years_experience))
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

skills = ['Python', 'SQL', 'Excel']
print(", ".join(skills))
# Python, SQL, Excel

price = 59
print(f"The price is exactly: {price:.2f}")
# The price is exactly: 59.00

price2 = 20000
print(f"The price is: {price2:,}")
# The price is: 20,000

price3 = 100
txt = f"It is {'perfect' if price3 == 100 else 'ok'}"
print(txt)
# It is perfect
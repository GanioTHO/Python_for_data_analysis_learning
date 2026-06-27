a = 'This is a string in single quote'
b = "This is a string in double quote"

c = '''
Multi
Line
String
'''

d = """
Also
Same
"""

skill = "Python"
print(skill.upper())
# PYTHON
print(skill.lower())
# python
# print(help(str))

print(skill.replace("P", "J"))
# Jython

job_title = "Data Analyst"
print(job_title.replace("a", "o", 2))
# Doto Analyst

print(job_title.split(sep=" ", maxsplit=1))
# ['Data', 'Analyst']      
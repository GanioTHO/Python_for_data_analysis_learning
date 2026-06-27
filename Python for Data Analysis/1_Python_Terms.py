salary = 100000

print(salary)
# 100000
print(type(salary))
# <class 'int'>
print(type("Hello!"))
# <class 'str'>

print(id(salary))
# 2913962270896
# 2486295175344
# 1976880505008

def greet():
    return "Hi"

print(greet())

# print(help(int))
'''
Help on class int in module builtins:        

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
-- More  -- 
'''
job_title = "Data Analyst"
job_location = "Poland"
job_salary = 250000

class JobPost:
    def __init__(self, title, location, salary):
        self.title = title
        self.location = location
        self.salary = salary

print(JobPost(job_title, job_location, job_salary))
# <__main__.JobPost object at 0x000002C676DAC530>

job_1 = JobPost(job_title, job_location, job_salary)

print(job_1.title)
# Data Analyst

print(job_salary.__add__(1))
# 250001
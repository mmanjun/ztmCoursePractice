import random
import sys

first_arg = int(sys.argv[1])
second_arg = int(sys.argv[2])
print(f"The numbers you entered are : {first_arg}, {second_arg}")
print(f"The random number I generated is: {random.randint(first_arg, second_arg)}")
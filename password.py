import random


a = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQURSTUVWXYZ!@#$%^&*()_+"


code_with_trick = 16 

p = "".join(random.sample(a, code_with_trick))

print(p)
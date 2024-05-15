import random
import string

letters = string.ascii_letters
x = "".join(random.sample(letters,6))
print(x + "@abhi.com")
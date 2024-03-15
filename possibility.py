import random


class Foo:
    x = [["a", 0.1], ["b", 0.2], ["c", 0.7]]
    my_dict = {}
    for key, value in x:
        value *= 10
        my_dict[key] = int(value)

    def sample(self):
        result = []
        for key, value in self.my_dict.items():
            result.extend([key] * value)
        rand = random.choice(result)
        return rand

obj = Foo()
print(obj.sample())

#_________________________________________________

import sys
import time
#import random

class Possibility:
    def __init__(self, text):
        # Unzipping text to separate values and keys (probabilities)
        self.value, self.key = zip(*text)

    def sample(self):
        # Returns a single sample based on the weights
        return random.choices(self.value, weights=self.key, k=1)


x = [["a", 0.1], ["b", 0.2], ["c", 0.7]]
obj = Possibility(x)
print(*obj.sample())

start_time = time.time()

# Measure the memory of the instance 'obj', not the 'Possibility' class itself
my_memory = sys.getsizeof(obj)
elapsed_time = time.time() - start_time  # Measuring the time taken for the memory size check

print("_" * 30, f'\nTime : {elapsed_time:.2f}s | Memory : {my_memory} bytes')


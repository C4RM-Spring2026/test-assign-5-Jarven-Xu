import numpy as np

def FizzBuzz(start, finish):

    nums = np.arange(start, finish + 1)

    out = nums.astype(object)

    fizz = nums % 3 == 0
    buzz = nums % 5 == 0

    out[fizz] = "fizz"
    out[buzz] = "buzz"
    out[fizz & buzz] = "fizzbuzz"

    return list(out)

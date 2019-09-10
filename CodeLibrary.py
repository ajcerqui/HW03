# Library to generate random codes and accompany lock check

import random
import string

SEED = random.randint(0,1000)

def generate_code(digits: int = 3, seed:int = None) -> str :
    ''' Generates a random sequence of lowercase letters of length
    equal to digits.
    '''
    letters = string.ascii_lowercase
    for i in range(digits):
        random.seed(seed)
        code = ''.join(random.choices(letters, k=3))
    return code


def attempt_unlock(guess:str) -> str:
    if guess == generate_code(seed=SEED):
        return 'ACCESS GRANTED'
    else:
        return 'ACCESS DENIED'

import numpy as np
import random

def seed_everything(seed, random_seed):
    if random_seed == True:
        np.random.seed(seed)
        random.seed(seed)
        print(f'シード値（seed={seed}）は固定しました。')
    else:
        print('シード値は固定しませんでした。')
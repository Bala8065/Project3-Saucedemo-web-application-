import random
from typing import List, Tuple

def choose_random_products(all_products: List[Tuple[str, float]], n: int = 4):
    if len(all_products) < n:
        raise ValueError("Not enough products to choose from")
    return random.sample(all_products, n)

from game_data import difficulty, tiers

class Combination:
    def __init__(self, item1, product, item2=None):
        self.item1 = item1
        self.item2 = item2
        self.product = product

    def as_tuple(self):
        return (self.item1, self.item2, self.product)

    def __repr__(self):
        if self.item2:
            return f"{self.item1} + {self.item2} → {self.product}"
        return f"{self.item1} → {self.product}"

    def score(self, inventory):
        def get_diff(item):
            if not item:
                return 0
            if item in difficulty:
                return difficulty[item]
            if item in tiers:
                return tiers[item] * 2
            print(f"[WARNING] No difficulty or tier found for: {item}")
            return 0

        diff1 = get_diff(self.item1)
        diff2 = get_diff(self.item2)

        score1 = -diff1 / 2 if self.item1 in inventory else -diff1
        score2 = -diff2 / 2 if (self.item2 and self.item2 in inventory) else -diff2

        return score1 + score2

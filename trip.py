class Trip:
    def __init__(self):
        self.combinations = []

    def add(self, combo):
        if len(self.combinations) < 10:
            self.combinations.append(combo)

    def __len__(self):
        return len(self.combinations)

    def __repr__(self):
        return "\n".join(str(c) for c in self.combinations)

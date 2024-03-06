class Queens_Evoluion:
    def create_first_gen(self):
        for i in range(self.num_of_chromosomes):
            self.chromosomes.append()

    def __init__(self, num_of_chromosomes):
        self.chromosomes = []
        self.num_of_chromosomes = num_of_chromosomes
        self.create_first_gen()

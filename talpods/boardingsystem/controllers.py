from .models import BoardingPass


class BoardingPassesSorter:
    boarding_passes = []
    sorted_boarding_passes = []
    first_pass = BoardingPass()
    last_pass = BoardingPass()

    # Initialize with list of boarding passes
    def __init__(self, boarding_passes=None):
        self.boarding_passes = boarding_passes
        self.sorted_boarding_passes = []

    def get_sorted_cards(self):
        return self.sorted_boarding_passes

    def sort(self):
        self.set_first_and_last()
        self.remove_first__and_last()  # remove first and last from list
        self.add_to_sorted_passes(self.first_pass)  # now add first to sorted list
        while True:
            for index, b_pass in enumerate(self.boarding_passes):
                if self.sorted_boarding_passes[-1].destination == b_pass.source:
                    self.add_to_sorted_passes(b_pass)
                if self.sorted_boarding_passes[-1].destination == self.last_pass.source:
                    self.add_to_sorted_passes(self.last_pass)
                    return self.sorted_boarding_passes

    def add_to_sorted_passes(self, b_pass=None):
        self.sorted_boarding_passes.append(b_pass)

    def remove_first__and_last(self):
        for index, b_pass in enumerate(self.boarding_passes):
            if self.first_pass == b_pass or self.last_pass == b_pass:
                del self.boarding_passes[index]

    def set_first_and_last(self):
        destinations = [p.destination for p in self.boarding_passes]
        sources = [p.source for p in self.boarding_passes]
        for b_pass in self.boarding_passes:
            if b_pass.source not in destinations:
                self.first_pass = b_pass
            if b_pass.destination not in sources:
                self.last_pass = b_pass





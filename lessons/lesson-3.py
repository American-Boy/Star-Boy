class Flying:
    def fly(self, amphibian):
        amphibian.state = "in the air "
        print(f" Amphibia now  {amphibian.state}.")

class Swimming:
    def swim(self, amphibian):
        amphibian.state = "in the water "
        print(f"Amphhibia now {amphibian.state}.")

class Amphibian(Flying, Swimming):
    def init(self):
        self.state = "on land"
        print(f"Amphibia in the beginning {self.state}.")

    def land(self):
        self.state = "On land"
        print(f"Amphibia now {self.state}.")

    def current_state(self):
        print(f"Ongoing amphibias's state: {self.state}.")


amphibian = Amphibian()


amphibian.fly(amphibian)
amphibian.current_state()
amphibian.swim(amphibian)
amphibian.current_state()
amphibian.land()
amphibian.current_state()



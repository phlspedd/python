class Bike(object):
    """docstring for Bike."""
    def __init__(self, color, frame_material):
        super(Bike, self).__init__()
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Braking")

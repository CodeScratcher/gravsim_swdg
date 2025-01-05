import numpy as np

class MyClass:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.acceleration = np.array([0, 0])
    
    def update(delta):
        self.velocity += acceleration * delta * 0.5
        self.position += velocity * delta
        
        # update gravity and acceleration here

        self.velocity += acceleration * delta * 0.5

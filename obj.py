import numpy as np

G = 6.67430e-11

class GravityObject:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.acceleration = np.array([0, 0])
    
    def update(objs, delta):
        velocity += acceleration * delta * 0.5
        position += velocity * delta
        
        # update gravity and acceleration here
        acceleration = applyGravity(objs) / mass

        velocity += acceleration * delta * 0.5

    def applyGravity(objs):
        forces = np.array([0, 0])
        
        for obj in objs:
            if not (obj.position == this).all():
                pull = G * mass * obj.mass / np.linalg.norm(obj.position - position) ** 2
                force = ((obj.position - position) / np.linalg.norm(obj.position - position)) * pull
                forces += force
        
        return forces
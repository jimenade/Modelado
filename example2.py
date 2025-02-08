import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, 0)

planeId = p.loadURDF("plane.urdf")

euler_angles = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0, 0, 3]

robotId = p.loadURDF("example2.urdf", startPosition, startOrientation)

# position, orientation = p.getBasePositionAndOrientation(robotId)
# print("Posición:", position)
# print("Orientación (cuaternión):", orientation)

y0 = 3.0
v0 = 0.0
a = -9.81
t = 0

dt = 1./240.

# Ecuaciones de posicion y velocidad:
# y = y0 + v*t + 1/2*a*exp(t)
# v = v0 + a*t

y = y0
v = v0


while y > 0:
    v = v + a*t
    y = y + v*t + 1/2*a*pow(t, 2)

    t = t + dt
   

    print(f"Posición: {y:.2f} m | Velocidad: {v:.2f} m/s")
    
    p.resetBasePositionAndOrientation(robotId, [0, 0, y], [0, 0, 0, 1])

    p.stepSimulation()
    time.sleep(dt)

p.disconnect()
import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

planeId = p.loadURDF("plane.urdf")

euler_angles = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0, 0, 1]

robotId = p.loadURDF("r2d2.urdf", startPosition, startOrientation)

numJoints = p.getNumJoints(robotId)
print("NumJoint: " + str(numJoints))

for j in range(numJoints):
    print("%d - %s" %(p.getJointInfo(robotId, j)[0], p.getJointInfo(robotId, j)[1].decode("utf-8")))


frictionId = p.addUserDebugParameter("jointFriction", 0, 10, 5)
torqueId = p.addUserDebugParameter("joint torque", -10, 10, 5)  

while(1):

    frictionForce = p.readUserDebugParameter(frictionId)
    jointTorque = p.readUserDebugParameter(torqueId)

    # Movemos las ruedas de dealnte y detras y dch e izq
    # Rueda delantera dch = 2
    # Rueda trasera dch   = 3
    # Rueda delantera izq = 6
    # Rueda trasera izq   = 7
    p.setJointMotorControlArray(robotId, [2, 3, 6, 7], p.VELOCITY_CONTROL, targetVelocities=[-10, -10, -10, -10])
    
    # Movemos el gripper
    # gripper telescopico = 8
    # gripper dch         = 9
    # gripper izq         = 11
    p.setJointMotorControlArray(robotId, [8, 9, 11], p.POSITION_CONTROL, targetPositions=[5, 5, 5])

    p.stepSimulation()
    time.sleep(1./240.)


# for i in range(10000):
#     p.stepSimulation()
#     time.sleep(1./240.)

# p.disconect()
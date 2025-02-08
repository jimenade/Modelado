import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

planeId = p.loadURDF("plane.urdf")

euler_angles = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0, 0, 0]

robotId = p.loadURDF("example.urdf", startPosition, startOrientation)

numJoints = p.getNumJoints(robotId)
print("NumJoint: " + str(numJoints))

for j in range(numJoints):
    print("%d - %s" %(p.getJointInfo(robotId, j)[0], p.getJointInfo(robotId, j)[1].decode("utf-8")))


frictionId = p.addUserDebugParameter("Joint Friction", 0, 10, 5)
torqueId = p.addUserDebugParameter("Joint torque", -10, 10, 5)  

while(1):

    frictionForce = p.readUserDebugParameter(frictionId)
    jointTorque = p.readUserDebugParameter(torqueId)
    
    # Establecemos la velocidad de la articulacion
    p.setJointMotorControl2(robotId, 2, p.VELOCITY_CONTROL, targetVelocity=0,  force=frictionForce)

    # Establecemos el torque de la articulacion
    p.setJointMotorControl2(robotId, 2, p.TORQUE_CONTROL, force=jointTorque)

    
    p.stepSimulation()
    time.sleep(1./240.)


# for i in range(10000):
#     p.stepSimulation()
#     time.sleep(1./240.)

# p.disconect()
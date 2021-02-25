def deposit():
    """Deposits the current load of the robot in order to score points. Deposit can only be done at the robot home base. If it is done anywhere else, the robot will lose its load and cannot recover it
    :returns: None

    """
    pass

def getAngleTo(x: float, z: float) -> float:
    """Calculate and return the angle in degrees about the up axis/y axis between the provided float (x, z) coordinate and the current direction that the robot is facing

    :x: x value of the other coordinate
    :z: z value of the other coordinate
    :returns: angle in degrees

    """
    return 0.0

def getBasePosition() -> list[float]:
    """Returns a python array which contains the x,y,z position of the robot spawn point on the base.
    :returns: [x, y, z]

    """
    return []

def getBattery() -> float:
    """Returns float of robot's current battery charge as a percentage of its max battery capacity
    :returns: battery percentage as float

    """
    return 0.0

def getCurrentlyCarrying() -> int:
    """Returns the amount of objects that the drone is currently carrying.
      :returns: number of objects

    """
    return 0

def getDistanceTo(x: float, z: float) -> float:
    """Calculate and return the distance along the ground plane between the provided float (x, z) coordinate and the current position of the robot.
      :returns: distance as float

    """
    return 0

def getGPS() -> list[float]:
    """Returns a python array which contains the robot’s current (x,y,z) coordinate position.
      :returns: [x, y, z]

    """
    return []

def getHeading() -> float:
    """Calculate and return the global compass heading that the robot is currently facing. The compass will return 0 if the robot is facing the blue base and 180 if the robot is facing the red base.
      :returns: angle in degrees [0, 180]

    """
    return 0

def getIRData() -> dict:
    """Returns the data recorded from the onboard IR sensors as a python dictionary. If there is no object detected, the dictionary will be empty.If there is an object detected, the following data will be returned in the dictionary:
      - Triggered sensor
          'forward'
          'backward'
          'left'
          'right'
          'up'
          'down'
      - Type of object
          'charger'
          'mine'

      NOTES
          sensors will not be live until calling robot.toggleSensors(True)
          robot2 and robot3 must be remanaged to use sensors

      >>> robot1.getIRData()
      {
        "forward": {
            distance: 10.543,
            type: "charger"
        }
      }

      :returns: dictionary

    """
    return {}

def land():
    """A blocking or async command which will land the robot on the ground.
      :returns: None

    """
    pass

def linearAngular(linV: float, angV: float):
    """A non-blocking command which sets the robot’s velocity directly. Linear velocity, linV, is velocity forwards  and backwards. Angular velocity, angV, is the rotational velocity. Both can be applied at once to make the robot turn in an arc. A positive linear velocity results in forward movement, a negative linear velocity results in backwards movement. Positive angular velocity results in clockwise rotation, negative angular velocity results in counterclockwise rotation.
      :returns: None

    """
    pass

def mine():
    """A blocking or async command which can only be done when landed on a mine. This will mine as many objects as the robot can hold from the mine. The robot can then travel back to the base and deposit these objects to score points.
      :returns: None

    """
    pass

def moveBackward(dis: float):
    """A blocking or async command which will fly the robot backwards by the specified distance dis.
      :returns: None

    """
    pass

def moveDown(dis: float):
    """A blocking or async command which will fly the robot down (towards the ground) by a specified distance dis.
      :returns: None

    """
    pass

def moveForward(dis: float):
    """A blocking or async command which will fly the robot forwards by the specified distance dis.
      :returns: None

    """
    pass

def moveLeft(dis: float):
    """A blocking or async command which will fly the robot to the left by the specified distance dis.
      :returns: None

    """
    pass

def moveRight(dis: float):
    """A blocking or async command which will fly the robot to the right by the specified distance dis.
      :returns: None

    """
    pass

def moveUp(dis: float):
    """A blocking or async command which will fly the robot up (away from the ground) by the specified distance dis.
      :returns: None

    """
    pass


def setAltitude(altitude: float):
    """A blocking or async command which will fly the robot up or down to the specified altitude alt.
      :returns: None

    """
    pass

def stop():
    """Stops the robot and cancels any current movement commands.
      :returns: None

    """
    pass

def takeControl():
    """Switches camera view to the specified robot.
    :returns: None

    """
    pass

def takeOff(altitude: float):
    """A blocking or async command which will takeoff the robot from a landed state to a specified altitude

    :altitude: target altitude
    :returns: None

    """
    pass

def toggleSensors(new_state: bool):
    """Enables robot sensors if the boolean "new_state" argument is true and disables sensors if it is false

    :new_state: new sensor state
    :returns: None

    """
    pass

def turnLeft(angle: float):
    """A blocking or async command which will rotate the robot counterclockwise by the number of degrees specified by the float angle.

    :angle: angle in degrees to turn
    :returns: None

    """
    pass

def turnRight(angle: float):
    """A blocking or async command which will rotate the robot clockwise by the number of degrees specified by the float angle.

    :angle: angle in degrees to turn
    :returns: None

    """
    pass

def remanage(new_attributes: dict):
    """This function assigns the Attribute Points of the robot. The robot must be at home base in order to run this function. There is a max of 21 points to use across robot2 and robot3 with a max of 15 points applied to any one drone.The remanage function takes a python dictionary as an argument. You can modify hullPoints, speedAP, accelerationAP, batteryAP, sensorRangeAP, and holdingCapacityAP.

    :new_attributes: dictionary with pairs { attribute_name: num_points }
    :returns: None

    >>> <robot>.remanage(
        {
            'hullPoints':5,
            'speedAP':3,
            'accelerationAP':3,
            'batteryAP':3,
            'sensorRangeAP':3,
            'holdingCapacityAP':3
        });

    """

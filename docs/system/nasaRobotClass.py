class nasaRobot:

    orientationOperation = {
    "N" : ("y", int.__add__),
    "S" : ("y", int.__sub__),
    "W" : ("x", int.__sub__),
    "E" : ("x", int.__add__)
    }

    changeOrientationDegrees = {
        "L" : +90,
        "R" : -90
    }

    correspondentDegreeOrientation = {
        "90" : "N",
        "270" : "S",
        "180": "W",
        "0" : "E",
        "360" : "E" # Alias para East
    }


    def __init__(self):
        self.position = {
            "x" : 0,
            "y" : 0
        }
        self.orientation = 90

        self.terrainMars = TerrainMars({
            "x" : 5,
            "y" : 5
        })

        self.unitsMoviment = 1
    
    def moveToFront(self):
        actualOrientation = self.convertDegreesToOrientation()
        positionToChange, operator = self.orientationOperation[actualOrientation]
        self.position[positionToChange] = operator(self.position[positionToChange], self.unitsMoviment)
        if self.terrainMars.inTerrain(self.position):
            return True
        else:
            return False

    def changeOrientation(self, direction):
        self.orientation += self.changeOrientationDegrees[direction]
        return True

    def convertDegreesToOrientation(self):
        if self.orientation < 0:
            self.orientation = 360 + self.orientation
        return self.correspondentDegreeOrientation[str(self.orientation)]

    def getRobotPosition(self):
        return str(tuple([self.position["x"], self.position["y"], self.convertDegreesToOrientation()]))
    
class TerrainMars:
    def __init__(self, limits):
        self.limits = limits

    def inTerrain(self, coordinates):
        for axis, value in coordinates.items():
            if self.limits[axis] < value:
                return False
        return True
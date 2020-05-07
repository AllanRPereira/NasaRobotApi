from flask import Flask
from docs.system import *

nasaRobot = Flask(__name__)
nasaRobot.config["SECRET_KEY"] = "549162e939b7697544c079993f49d403688da60a2bdee77e60cd867579fb632a"

@nasaRobot.route("/rest/mars/<path:robotMoveCommands>", methods=["POST"])
def moveRobotNasa(robotMoveCommands):
    robotPosition = {
        "x" : 0,
        "y" : 0,
        "o" : 90 # North is equal a 0°
    }
    robotMoveCommands = robotMoveCommands.upper()
    print(robotMoveCommands)
    if not checkComands(robotMoveCommands):
        return "Error"

    for move in robotMoveCommands:
        if move != "M":
            degreesChange = howToChangeOrientation[move]
            robotPosition["o"] += degreesChange
            if robotPosition["o"] == 360: robotPosition["o"] = 0
        else:
            actualOrientation = correspondentDegreeOrientation[str(robotPosition["o"])]
            position, operation = whereToMakeInOrientation[actualOrientation]
            robotPosition[position] = operation(robotPosition[position], unitsMoviment)
            print(robotPosition)
            if robotPosition[position] >= limitRobotsPositions[position]:
                return "Error"
    for key, value in robotPosition.items():
        robotPosition[key] = str(value)
    positionToSimbol = correspondentDegreeOrientation[robotPosition["o"]]
    response = (robotPosition["x"], robotPosition["y"], positionToSimbol)
    return str(response)


def checkComands(robotMoveList):
    acceptsCommandsToRobot = ["M", "L", "R"]
    for move in robotMoveList:
        if move not in acceptsCommandsToRobot:
            return False
    return True

if __name__ == "__main__":
    nasaRobot.run(host="127.0.0.1", port=5000, debug=True)
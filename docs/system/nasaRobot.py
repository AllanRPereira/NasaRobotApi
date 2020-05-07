from flask import Flask, abort
from docs.system.nasaRobotClass import nasaRobot

nasaRobotApp = Flask(__name__)
nasaRobotApp.config["SECRET_KEY"] = "549162e939b7697544c079993f49d403688da60a2bdee77e60cd867579fb632a"

@nasaRobotApp.route("/rest/mars/<path:robotMoveCommands>", methods=["POST"])
def moveRobotNasa(robotMoveCommands):
    robot = nasaRobot()
    robotMoveCommands = robotMoveCommands.upper()
    if not checkComands(robotMoveCommands):
        return ("400 Bad Request", 400)

    for move in robotMoveCommands:
        if move != "M":
            robot.changeOrientation(move)
        else:
            if not robot.moveToFront():
                return ("400 Bad Request", 400)
    return robot.getRobotPosition()

def checkComands(robotMoveList):
    acceptsCommandsToRobot = ["M", "L", "R"]
    for move in robotMoveList:
        if move not in acceptsCommandsToRobot:
            return False
    return True

if __name__ == "__main__":
    nasaRobotApp.run(host="127.0.0.1", port=5000, debug=True)
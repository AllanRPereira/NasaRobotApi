whereToMakeInOrientation = {
    "N" : ("y", int.__add__),
    "S" : ("y", int.__sub__),
    "W" : ("x", int.__add__),
    "E" : ("x", int.__sub__)
}

howToChangeOrientation = {
    "L" : +90,
    "R" : -90
}

correspondentDegreeOrientation = {
    "90" : "N",
    "270" : "S",
    "180": "W",
    "0" : "E"
}


limitRobotsPositions = {
    "x" : 5,
    "y" : 5
}

unitsMoviment = 1
import requests

PORT = 5000

def test_moveToFront():
    positionRobot = requests.post(f"http://localhost:{PORT}/rest/mars/MMM").content.decode()
    assert positionRobot == "(0, 3, 'N')", "Movimento incorreto para frente"

def test_moveToRight():
    positionRobot = requests.post(f"http://localhost:{PORT}/rest/mars/MMRMMRMM").content.decode()
    assert positionRobot == "(2, 0, 'S')", "Movimento incorreto para a direita"

def test_moveToLeft():
    positionRobot = requests.post(f"http://localhost:{PORT}/rest/mars/MML").content.decode()
    assert positionRobot == "(0, 2, 'W')", "Movimento incorreto para a esquerda"

def test_invalidMove():
    positionRobot = requests.post(f"http://localhost:{PORT}/rest/mars/AAA")
    assert positionRobot.status_code == 400, "Código de erro incorreto no caso do comando inválido"

def test_moveToOutside():
    positionRobot = requests.post(f"http://localhost:{PORT}/rest/mars/MMMMMM")
    assert positionRobot.status_code == 400, "Código de erro incorreto no caso fora dos limites"

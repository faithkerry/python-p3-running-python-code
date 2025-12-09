from os import path

def test_app_py_exists():
    assert path.exists("lib/app.py")

def test_app_py_prints():
    with open("lib/app.py") as f:
        content = f.read()
    assert "Hello World! Pass this test, please." in content


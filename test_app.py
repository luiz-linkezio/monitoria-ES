import subprocess

def test_app_output():
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, CI/CD!" 
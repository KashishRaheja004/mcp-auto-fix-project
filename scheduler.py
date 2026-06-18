import subprocess

with open("error.log", "w") as log:
    subprocess.run(
        ["python", "calculator.py"],
        stderr=log,
        text=True
    )

print("Execution completed. Check error.log")
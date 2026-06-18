import subprocess

print("MCP Server Triggered: AI Fix Simulation")

# Step 1: Fix calculator automatically
fix_code = """
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(10, 0))
"""

with open("calculator.py", "w") as f:
    f.write(fix_code)

print("Code fixed by MCP Server")

# Step 2: Git automation simulation
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Auto fix via MCP server"])
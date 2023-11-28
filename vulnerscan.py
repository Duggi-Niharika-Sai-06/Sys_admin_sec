import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

# Commands to execute
commands = [
    "sudo iptables -L",
    # Add any other commands you want to execute, e.g.,
    # "sudo iptables -S",
    # "sudo ufw status",
    # etc.
]

# Executing and printing the output of each command
for cmd in commands:
    print(f"Executing: {cmd}")
    output = run_command(cmd)
    print(output)

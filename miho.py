import subprocess

print ("cecking midi connections")

subprocess.Popen(["aconnect", "OP-Z", "OP-1 Midi Device"])
subprocess.Popen(["aconnect", "-l"])

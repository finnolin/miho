import subprocess


#OP-Z Out
subprocess.Popen(["aconnect", "OP-Z", "OP-1 Midi Device"])

#OP-1 Out


#Keystep Out
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-1 Midi Device"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-Z"])
import subprocess

#-------DEVICES-------
#OP-Z
#OP-1 Midi Device
#Arturia KeyStep 32
#reface CS
#Circuit



#CONNECTIONS:

#OP-Z Out
subprocess.Popen(["aconnect", "OP-Z", "OP-1 Midi Device"])
subprocess.Popen(["aconnect", "OP-Z", "reface CS"])
subprocess.Popen(["aconnect", "OP-Z", "Circuit"])

#Keystep Out
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-1 Midi Device"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-Z"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "reface CS"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "Circuit"])
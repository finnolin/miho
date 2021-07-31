import subprocess

#-------DEVICES-------
#OP-Z
#OP-1 Midi Device
#Arturia KeyStep 32
#reface CS
#Circuit
#VoiceLive Touch 2
#Deluge


#CONNECTIONS:

#Deluge Out
subprocess.Popen(["aconnect", "Deluge", "OP-1 Midi Device"])
subprocess.Popen(["aconnect", "Deluge", "reface CS"])
subprocess.Popen(["aconnect", "Deluge", "VoiceLive Touch 2"])
subprocess.Popen(["aconnect", "Deluge", "OP-Z"])


#Keystep Out
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-1 Midi Device"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-Z"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "reface CS"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "Deluge"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "VoiceLive Touch 2"])
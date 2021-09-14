import subprocess

#-------DEVICES-------
#OP-Z
#OP-1
#Arturia KeyStep 32
#reface CS
#Circuit
#VoiceLive Touch 2
#Deluge
#Midi USB-USB


#CONNECTIONS:

#Deluge Out
subprocess.Popen(["aconnect", "Deluge", "OP-1"])
subprocess.Popen(["aconnect", "Deluge", "reface CS"])
subprocess.Popen(["aconnect", "Deluge", "VoiceLive Touch 2"])
subprocess.Popen(["aconnect", "Deluge", "OP-Z"])
subprocess.Popen(["aconnect", "Deluge", "MIDI USB-USB MIDI 1"])

#Keystep Out
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-1"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "OP-Z"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "reface CS"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "Deluge"])
subprocess.Popen(["aconnect", "Arturia KeyStep 32", "VoiceLive Touch 2"])

#Norns Out
subprocess.Popen(["aconnect", "MIDI USB-USB MIDI 1", "OP-1"])
subprocess.Popen(["aconnect", "MIDI USB-USB MIDI 1", "reface CS"])

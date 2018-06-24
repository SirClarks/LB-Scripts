def print_menu():
	print("\nRunScript Picker")
	print("1. SublimeText")
	print("2. Spotify")
	print("3. Gimp")
	print("4. Substance Player")
	print("5. Mplay")
	print("6. Exit")

#import os
import subprocess

loop=True
while loop:
	print_menu()
	print("Enter your choice [1-6]: ")
	choice = raw_input()

	if choice=='1':
		#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/sublime_text.sh')
		subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/sublime_text.sh"])

	elif choice=='2':
		#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/spotify.sh')
		subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/spotify.sh"])

	elif choice=='3':
		#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/gimp.sh')
		subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/gimp.sh"])

	elif choice=='4':
		#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/substance_player.sh')
		subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/substance_player.sh"])

	elif choice=='5':
		#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/houdini_mplay.sh')
		subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/houdini_mplay.sh"])

	elif choice=='6':
		print "\n-----exiting------\n"
		loop=False
	else:
		raw_input("Wrong option selection, enter any key to try again..")

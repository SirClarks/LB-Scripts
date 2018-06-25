

#package imports
import subprocess
import signal
import sys
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--test", required=False,
	help="testing help and argument passing")
args = vars(ap.parse_args())

if args["test"]=='plus':
	print("yes you entered plus.")
else:
	print("failed")

#print("Testing this {}".format(args["test"]))

def print_menu():
	print("\nRunScript Picker")
	print("1. SublimeText")
	print("2. Spotify")
	print("3. Gimp")
	print("4. Substance Player")
	print("5. Mplay")
	print("6 ")
	print("6. Exit")

#main menu
def menu_select():
	try:
		loop=True
		while loop:
			print_menu()
			print("Select runscript [1-6]: ")
			choice = raw_input()

			if choice=='1':
				#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/sublime_text.sh')
				subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/sublime_text.sh"])
				sys.exit(0)

			elif choice=='2':
				#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/spotify.sh')
				subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/spotify.sh"])
				sys.exit(0)

			elif choice=='3':
				#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/gimp.sh')
				subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/gimp.sh"])
				sys.exit(0)

			elif choice=='4':
				#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/substance_player.sh')
				subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/substance_player.sh"])
				sys.exit(0)

			elif choice=='5':
				#os.system('/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/houdini_mplay.sh')
				subprocess.Popen(["bash", "/LOSTBOYS/LIBRARY/TECH_CONFIG/run_scripts/houdini_mplay.sh"])
				sys.exit(0)

			elif choice=='6':
				print "\n-----exiting------\n"
				loop=False
				sys.exit(0)

			else:
				raw_input("Wrong option selection, enter any key to try again..")
	except KeyboardInterrupt:
		print("\n")
		sys.exit(0)


menu_select()

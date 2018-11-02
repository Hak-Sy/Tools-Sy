import os
import sys

#----------------------------------------
#| Code => Hak-Sy                       |
#| Fb => hosam.ahmad2017                |
#| Gmail => hosamalshami019@gmail.com   |
#| From = > Syria                       |
#----------------------------------------
sys.stdout.write ("\033[1;91m") #color red

print ("\t\t                     ,        , ")
print ("\t\t                    /(        )` ")
print ("\t\t                    \ \___   / |  ")
print ("\t\t                    /- _  `-/  '  ")
print ("\t\t                   (/\/ \ \   /\    ")
print ("\t\t                   / /   | `    \ ")
print ("\t\t                   O O   ) /    | ")
print ("\t\t                   `-^--'`<     ' ")
print ("\t\t                   (_.)  _  )   / ")
print ("\t\t                   `.___/`    /  ")
print ("\t\t                     `-----' /    ")
print ("\t\t        <----.     __ / __   \    ")
print ("\t\t        <---<|====O)))==) \) /==== ")
print ("\t\t        <----'    `--' `.__,' \   ")
print ("\t\t                     |        |     ") 
print ("\t\t                      \       /      ")
print ("\t\t              ______  ( (_  / \______ ")
print ("\t\t             ,  '  ,-----'  |        \ ")
print ("\t\t              ` --{__________)       \/ ")
sys.stdout.write ("\033[94m") #color white

print ('\n\t\t\t    [~] Welcome To Tools Sy [~]')

input ("Please enter for conect ...")

print (''' 
~ Tools Information 	   	    ~ Tools Doos Attack ~
1- Vega                       		 5- Slowloris
2- Nikto                        	 6- Xerxes
3- Maltego                    		 7- Hammer
4- Nmap                       		 8- Botnet   
 												''')
 

me = input ("Enter Number to download :")

if me == "1":
 cmd1 = os.system ("apt-get install vega")
if me == "2":
 cmd1 = os.system ("apt-get install nikto git && git clone https://github.com/sullo/nikto")
if me == "3":
 cmd1 = os.system ("apt-get install maltego git && git clone https://github.com/Lookingglass/Maltego")
if me == "4":
 cmd1 = os.system ("apt-get install nmap git && git clone https://github.com/nmap/nmap")
if me == "5":
 cmd1 = os.system ("git clone https://github.com/llaera/slowloris.pl")
if me == "6":
 cmd1 = os.system ("git clone https://github.com/dswalker/xerxes")
if me == "7":
 cmd1 = os.system ("git clone https://github.com/Code52/HAMMER")
if me == "8":
 cmd1 = os.system ("sudo git clone https://github.com/malwares/Botnet")
 
sys.stdout.write ("\033[91m") #color red  

input ("\nPress Enter to continue")

sys.stdout.write("\033[94m") #color white
print('''
     -=-------------------------------------=-     ''')
sys.stdout.write("\033[1;32m") #color green
print ('''                     
~ Hacking Sites ~ 	   	    ~ Tools Targeting ~
 1- Wpscan             		       5- Metasploit
 2- Sqlmap             		       6- Armitage
 3- Xsser               	       7- Beef xss
 4- Joomscan           		       8- Websploit        
                   ''')

namo = input("Enter Number Tools :")
if namo == "1":
 cmd1 = os.system ("apt-get install wpscan")
if namo == "2":
 cmd1 = os.system ("apt-get install sqlmap") 
if namo == "3":
 cmd1 = os.system ("apt-get install xsser git && git clone https://github.com/epsylon/xsser")
if namo == "4":
 cmd1 = os.system ("apt-get install joomscan git && git clone https://github.com/rezasp/joomscan")
if namo == "5": 
 cmd1 = os.system ("apt-get install metasploit-framework")
if namo == "6":
 cmd1 = os.system ("apt-get install armitage")
if namo == "7":
 cmd1 = os.system ("git clone https://github.com/beefproject/beef")
if namo == "8":
 cmd1 = os.system ("apt-get install websploit")

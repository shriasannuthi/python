#PYTHON 3 CODE FOR TIC-TAC-TOE
from os import system

print("\n=~=~=~=~=~=~=~= TIC-TAC-TOE =~=~=~=~=~=~=~=\n")
print("> HOW TO PLAY :")
print("--> Enter a digt from the check below.")
print("--> Each player is given a unique character.")
print("--> The first player to fill the checks either")
print("    horizontally, vertically, or diagonally WINS.")
print("\nPlayer 1 - ' X '")
print("Player 2 - ' O '\n\n")

r1='         |     |     '
r2='      1  |  2  |  3  '	
r3='    _____|_____|_____'	
r4='         |     |     '
r5='      4  |  5  |  6  '
r6='    _____|_____|_____'
r7='         |     |     '
r8='      7  |  8  |  9  '	  
r9='         |     |     '

def Win(r2,r5,r8):
	if r2[6]==r2[12]==r2[18] or r5[6]==r5[12]==r5[18] or r8[6]==r8[12]==r8[18]:return 1
	elif r2[6]==r5[6]==r8[6] or r2[12]==r5[12]==r8[12] or r2[18]==r5[18]==r8[18]:return 1
	elif r2[6]==r5[12]==r8[18] or r2[18]==r5[12]==r8[6]:return 1				
def Check(p):
	digits=['1','2','3','4','5','6','7','8','9']
	return 1 if p in digits else 0
		
print(r1,r2,r3,r4,r5,r6,r7,r8,r9,'',sep="\n");l=[]

while (1):		
	p1=input("Player 1's turn:\nSelect a check: ")
	while Check(p1)!=1 or p1 in l:
		if Check(p1)!=1:
			print("Invalid Input :(\nPlease Try Again.\n")
			p1=input("Player 1's turn:\nSelect a check: ")
		elif p1 in l:
			print("The selected check is already filled :(\nPlease Try Again.\n")
			p1=input("Player 1's turn:\nSelect a check: ")		
	l.append(p1)		
			
	if   p1=='1':r2=r2.replace('1','X')
	elif p1=='2':r2=r2.replace('2','X')
	elif p1=='3':r2=r2.replace('3','X')
	elif p1=='4':r5=r5.replace('4','X')
	elif p1=='5':r5=r5.replace('5','X')
	elif p1=='6':r5=r5.replace('6','X')
	elif p1=='7':r8=r8.replace('7','X')
	elif p1=='8':r8=r8.replace('8','X')
	elif p1=='9':r8=r8.replace('9','X')
	system("cls")
	print('\n\n       TIC-TAC-TOE \n')
	print('',r1,r2,r3,r4,r5,r6,r7,r8,r9,'',sep="\n")
	
	if Win(r2,r5,r8)==1:
		print("=========== Player1 WON ===========")
		print("=~=~=~=~= CONGRATUlATIONS =~=~=~=~=")
		input("\n\n Hit Enter To Continue ... ")
		break
	elif len(l)==9:
		print("=========== IT'S A DRAW ===========")
		print("=~=~=~=~=~=~ TRY AGAIN =~=~=~=~=~=~")
		input("\n\n Hit Enter To Continue ... ")
		break
		
	p2=input("Player 2's turn:\nSelect a check: ")
	while Check(p2)!=1 or p2 in l:
		if Check(p2)!=1:
			print("Invalid Input :(\nPlease Try Again.\n")
			p2=input("Player 2's turn:\nSelect a check: ")
		elif p2 in l:
			print("The selected check is already filled :(\nPlease Try Again.\n")
			p2=input("Player 2's turn:\nSelect a check: ")
	l.append(p2)			
	
	if   p2=='1':r2=r2.replace('1','O')
	elif p2=='2':r2=r2.replace('2','O')
	elif p2=='3':r2=r2.replace('3','O')
	elif p2=='4':r5=r5.replace('4','O')
	elif p2=='5':r5=r5.replace('5','O')
	elif p2=='6':r5=r5.replace('6','O')
	elif p2=='7':r8=r8.replace('7','O')
	elif p2=='8':r8=r8.replace('8','O')
	elif p2=='9':r8=r8.replace('9','O')
	system("cls")
	print('\n\n       TIC-TAC-TOE \n')
	print('',r1,r2,r3,r4,r5,r6,r7,r8,r9,'',sep="\n")
	
	if Win(r2,r5,r8)==1:
		print("=========== Player2 WON ===========")
		print("=~=~=~=~= CONGRATUlATIONS =~=~=~=~=")
		input("\n\n Hit Enter To Continue ... ")
		break
	elif len(l)==9:
		print("=========== IT'S A DRAW ===========")
		print("=~=~=~=~=~=~ TRY AGAIN =~=~=~=~=~=~")
		input("\n\n Hit Enter To Continue ... ")
		break
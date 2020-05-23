import string
import time

class Caesar():
    
  def __init__(self):
    self.AtoM = ("ABCDEFGHIJKLM")
    self.NtoZ = ("NOPQRSTUVWXYZ")
     
  def decode(self,strings):
    #password = passlow.upper()
    rot13 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    print("\n",str.translate(strings, rot13),"\n")
    
  def encode(self,password):
    rot13 = str.maketrans("NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm","ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")
    print("\n",str.translate(password, rot13),"\n")
    
  def change(self):
    
    print("""
 ___        _     _ ____
|  _ \ ___ | |_  / |___ / 
| |_) / _ \| __| | | |_ \ 
|  _ < (_) | |_  | |___) |
|_| \_\___/ \__| |_|____/  Caesar Algorithm

(1) Decode
(2) Encode
(99) Exit
          """)
    
    while (True):
        
        try:
            
            choice = int(input("Your Choice: "))
                
            if choice == 99:
                print("Bye!")
                time.sleep(2)
                break
    
            elif choice == 1:
                self.entryDecode = str(input('Enter the Text: '))
                self.decode(self.entryDecode)
            
            elif choice == 2:
                self.entryEncode = str(input("Enter the Password: "))
                self.encode(self.entryEncode)
        
            else:
                print("\nThere is no such option\n")
                
        except ValueError:
            print("\nThe value you enter is not a number, please just enter a number!\n")
if __name__ == '__main__':
  caesarRot = Caesar()
  caesarRot.change()
import sys
import os



    
    
def main():
    print('(1) Developer Stuff')
    print('(2) Search ')
    print('(3) Download Github Repo')
    
    var = (int(input('What would you like to do? ')))
    
    if var == 1:
        dev()
        
    if var == 2:
        search()
    
    if var == 3:
        github()
        

####################################################################################################################################################################################
    
    
def dev():
    print('(1) Open Vscode')
    print('(2) Open Github this repo')    
    print('(3) Open StackOverflow')
    
    var2 = (int(input('What would you like to do? ')))
    
    if var2 == 1:
        os.system('code')
        
    if var2 == 2:
        os.system('start chrome github.com/tysudo/Help-Script-3.0.0')
        
    if var2 == 3:
        os.system('start chrome https://stackoverflow.com/')
    
    
    
    
    
    
    
    
main()
import sys
import os



    
    
def main():
    print('(1) Developer Stuff')
    print('(2) Search ')
    
    
    var = (int(input('What would you like to do? ')))
    os.system('cls')
    
    if var == 1:
        dev()
        
    if var == 2:
        search()
    


####################################################################################################################################################################################
    
    
def dev():
    print('(1) Open Vscode')
    print('(2) Open Github this repo')    
    print('(3) Open StackOverflow')
    
    
    var2 = (int(input('What would you like to do? ')))
    os.system('cls')
    
    if var2 == 1:
        os.system('code')
        
    if var2 == 2:
        os.system('start chrome github.com/tysudo/Help-Script-3.0.0')
        
    if var2 == 3:
        os.system('start chrome https://stackoverflow.com/')
        
        
def search():
    print('(1) Search StackOverflow')
    print('(2) Search Dev stuff on Amazon.ca')
    print('(3) Search Github')
    
    
    
    var4 = (int(input('What would you like to do? ')))
    os.system('cls')
    
    
    if var4 == 1:
        var5 = (str(input('What would you like to search? Spaces must be + ')))
        os.system('start chrome https://stackoverflow.com/search?q='+var5+' ')
        

    if var4 == 2:
        os.system('start chrome https://www.amazon.ca/s?k=tech+gadgets&sprefix=tech+gad%2Caps%2C294&ref=nb_sb_ss_ts-doa-p_1_8')
        
        
    if var4 == 3:
        var6 = (str(input('What would you like to search for? Spaces must be +')))
        os.system('start chrome https://github.com/search?q='+var5+'')
    
    
    
    
    
main()
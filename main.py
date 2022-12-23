from encodings import utf_8
from unittest import result
import zipfile #this libeary is user for password encripted ziped file or folder
import time #this is for time

folderPath = input('Enter path to your file / folder :')
zipf = zipfile.ZipFile(folderPath)

#check it file is password ency
if not zipf:
    print('file is not password procted')

else:
    starttime = time.time()
    result = 0
    count = 0
    #make an array
    charaters = ['0','1','2','3','4','5','6','7','8','9',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '!','@','#','$','%','^','&','*','(',')','-','+','='
    ]
    print('brute force')

    #password not found therefore result is zero
    if (result == 0):
        print('checking statemant')
        for i in charaters:
            for j in charaters:
                for k in charaters:    
                    for l in charaters:
                        guess = str(i)+str(j)+str(k)+str(l)
                        password = guess.encode('utf8').strip()
                        count = count+1
                        try:
                            with zipfile.ZipFile(folderPath,'w')as zf:
                                zf.extractall(pwd=password)
                                print('the password is '+guess)
                                endtime = time.time()
                                result  = 1
                                break
                        except:
                            pass
                    if result == 1:
                        break           
                if result == 1:
                        break        
            if result == 1:
                        break            
    if result == 0:
        print('there is nothing more we can do for more purchase our preimum plan')
    else:
        duration  = endtime-starttime
        print('password found successfully')


import time
import os
from PersonalInformation import local

print('Chen lizhu')
while True:
    try:
        file=open('%s\\Log.txt'%local,'a')
    except:
        file=open('%s\\Log.txt'%local,'r')
    file.write(time.strftime('%y-%m-%d,%H:%M:%S',time.localtime())+'\n')
    file.close()

    os.system('%s\\NewCareerDream.py'%local)
    os.system('%s\\NewJournaEconomicPerspectives.py'%local)
    os.system('%s\\NewTianchi.py'%local)
    os.system('%s\\NewYuqing.py'%local)

    file=open('%s\\Log.txt'%local,'a')
    file.write('sleeping...\n\n')
    file.close()

    time.sleep(1800)
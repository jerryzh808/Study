import time
import os
time_2019=[2019,1,1,11,30,0];
while 1:
    curtime=time.strftime('%Y-%m-%d %H:%M:%S');
    list_time=list(curtime.split( ));
    time_1=list_time[0].split("-");
    time_2=list_time[1].split(":");
    time_3=time_1+time_2;
    n=0;
    while n<len(time_3):
        time_3[n]=int(time_3[n]);
        n+=1;
    if time_2019[5]-time_3[5]<0:
        a=time_2019[5]+60-time_3[5];
    else:
        a=time_2019[5]-time_3[5];

    if time_2019[5]-time_3[5]==0:
        b=time_2019[4]+60-time_3[4];
    else:
        b=time_2019[4]+59-time_3[4];

    print('%d : %d' %(b,a));
    time.sleep(1);









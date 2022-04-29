with open('/Users/Sohad/Desktop/time_check.csv','w') as s:
    s.write('First Name,Last Name,  Time, Date\n')
    date = input("Date of Today:  ")
    for _ in range(100):
        name = input("First Name:  ")
        if name == 'end':
            break
        last = input("Last Name:  ")
        time = input("Time:  ")
        s.write("{},{},{},{}\n".format(name,last,time,date))
        print('----------Next Line----------')
with open('/Users/Sohad/Desktop/time_check.csv','r') as ss:
    sss = ss.read()
    print(sss)

T = int(input())

for case in range(1,T+1):
    X = raw_input()
    strX = str(X).split()
    p = int(strX[0])
    q = int(strX[1])
    pos_pts=[]
    occ_time=[]
    for sub_p in range (0,p):
        L = raw_input()
        strL = str(L).split()
        x = int(strL[0])
        y = int(strL[1])
        face = strL[2]
        if face =="N":
            for m in range (0,x+1):
                for n in range (y+1,q):
                    if [m,n] in pos_pts:
                        occ_time[pos_pts.index([m,n])]+=1
                    else:
                        pos_pts.append([m,n])
                        occ_time.append(1)
                        
        elif face =="S":
            for m in range (0,x+1):
                for n in range (0,y):
                    if [m,n] in pos_pts:
                        occ_time[pos_pts.index([m,n])]+=1
                    else:
                        pos_pts.append([m,n])
                        occ_time.append(1)
        elif face == "W":
            for m in range (0,x):
                for n in range (0,y+1):
                    if [m,n] in pos_pts:
                        occ_time[pos_pts.index([m,n])]+=1
                    else:
                        pos_pts.append([m,n])
                        occ_time.append(1)
        elif face =="E":
            for m in range (x+1,q):
                for n in range (0,y+1):
                    if [m,n] in pos_pts:
                        occ_time[pos_pts.index([m,n])]+=1
                    else:
                        pos_pts.append([m,n])
                        occ_time.append(1)
    #find max:
    max_time=max(occ_time)
    
    newl=[]
    for i in range(0,len(occ_time)):
        if occ_time[i]==max_time:
            newl.append(pos_pts[i])
    
    sortl=sorted(newl)
    
    result = sortl[0]
    s1 = result[0]
    s2 = result[1]
    
    print("Case #{}: {} {} ".format(case, s1,s2))

#!/usr/bin/env python3

def intoGeo(borderA, borderB, borderC, borderD):
    with open('out.txt', 'r') as f:
        line = f.readline()
        li_all = []
        while line:
            li = line.split()
            li_all.append(li)
            line = f.readline()
    
    # prev each el in li_all represents all agent regarding the same time 
    # below each el in trans represents all time of one agent
    trans = []
    for i in range(1, len(li_all[0])):
        agent = []
        for el in li_all:
            thistime = []
            thistime.append(el[i])
            thistime.append(el[0])
            agent.append(thistime)
        trans.append(agent)

    # trans structure is by now okay, below removes the "()" and turn into float
    for agt in trans:
        for i in range(len(agt)):
            agt[i].append(float(agt[i][1]))
            temp = agt[i][0][1:-1].split(',')
            agt[i][0] = float(temp[0])
            agt[i][1] = float(temp[1])

    # turn into geo-coordinates
    # 35x17.4m is the real dimension of the simulated rectangle with geo calibration
    xRate = [(borderC[0] - borderB[0])/35, (borderC[1] - borderB[1])/35]
    yRate = [(borderB[0] - borderA[0])/17.4, (borderB[1] - borderA[1])/17.4]
    geoCenter = [(borderA[0] + borderC[0])/2, (borderA[1] + borderC[1])/2]
    for agt in trans:
        for i in range(len(agt)):
            xGeo = agt[i][0] * xRate[0] + agt[i][1] * yRate[0]
            yGeo = agt[i][0] * xRate[1] + agt[i][1] * yRate[1]
            agt[i][0] = xGeo + geoCenter[0] - 0.082*(18.064249995157855-18.063598779214896)
            agt[i][1] = yGeo + geoCenter[1] - 0.082*(59.33535531252224-59.3351910473156)
    res = []
    for agt in trans:
        res.append({'trajectory': agt})
    res = str(res).replace("'", "\"")
    
    print(res)

if __name__=="__main__":
    # border of the simulated area
    intoGeo(
            [18.06409196251192, 59.33551828048482],
            [18.064249995157855, 59.33535531252224],
            [18.063598779214896, 59.3351910473156],
            [18.06344074656896, 59.33535401527818])
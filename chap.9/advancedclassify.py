from pylab import *
from geopy import geocoders
from geopy import distance

API_KEY = "As-upZFGArNVGs6pDLy5Uw-m5mZ-w7ZRKDLJ-M4G7zHZpKYs8cls2aDwa_CtnHzt"


class matchrow:
    def __init__(self, row, allnum=False):
        if allnum:
            self.data = [float(row[i]) for i in range(len(row) - 1)]
        else:
            self.data = row[0: len(row) - 1]
        self.match = int(row[len(row) - 1])


def loadmatch(f, allnum=False):
    rows = []
    for line in file(f):
        rows.append(matchrow(line.split(','), allnum))
    return rows


def loadnumerical(f):
    oldrows = loadmatch(f)
    newrows = []
    for row in oldrows:
        d = row.data
        data = [float(d[0]),
                float(d[5]),
                yesno(d[1]),
                yesno(d[2]),
                yesno(d[6]),
                yesno(d[7]),
                matchcount(d[3], d[8]),
                milesdistance(d[4], d[9]),
                row.match]
        newrows.append(matchrow(data))
    return newrows


def plotagematches(rows):
    xdm, ydm = [r.data[0] for r in rows if r.match == 1],\
               [r.data[1] for r in rows if r.match == 1]
    xdn, ydn = [r.data[0] for r in rows if r.match == 0],\
               [r.data[1] for r in rows if r.match == 0]
    avgs = lineartrain(rows)
    xavg0 = avgs[0][0]
    yavg0 = avgs[0][1]
    xavg1 = avgs[1][0]
    yavg1 = avgs[1][1]
    plot(xdm, ydm, 'go')
    plot(xdn, ydn, 'r+')
    plot(xavg0, yavg0, 'r*')
    plot(xavg1, yavg1, 'g*')
    show()


def lineartrain(rows):
    averages = {}
    counts = {}

    for row in rows:
        cl = row.match

        averages.setdefault(cl, [0, 0] * (len(row.data)))
        counts.setdefault(cl, 0)

        for i in range(len(row.data)):
            averages[cl][i] += float(row.data[i])

        counts[cl] += 1

    for cl, avg in averages.items():
        for i in range(len(avg)):
            avg[i] /= counts[cl]

    return averages


def dotproduct(v1, v2):
    return sum([v1[i] * v2[i] for i in range(len(v1))])


def dpclassify(point, avgs):
    b = (dotproduct(avgs[1], avgs[1]) - dotproduct(avgs[0], avgs[0])) / 2
    y = dotproduct(point, avgs[0]) - dotproduct(point, avgs[1]) + b
    if y > 0:
        return 0
    return 1


def yesno(v):
    if v == 'yes':
        return 1
    elif v == 'no':
        return -1
    return 0


def matchcount(interest1, interest2):
    l1 = interest1.split(':')
    l2 = interest2.split(':')
    x = 0
    for v in l1:
        if v in l2:
            x += 1
    return x


def milesdistance(a1, a2):
    g = geocoders.Bing(API_KEY)
    try:
        loc1 = g.geocode(a1, exactly_one=False)
        loc2 = g.geocode(a2, exactly_one=False)
        loc1 = loc1[0][1]
        loc2 = loc2[0][1]
    except:
        print a1
        print a2
        raise
    return distance.distance(loc1, loc2).miles


def scaledata(rows):
    length = len(rows[0].data)
    low = [999999999.0] * length
    high = [-999999999.0] * length

    # [BUG] wor -> row
    for row in rows:
        d = row.data
        for i in range(length):
            if d[i] < low[i]:
                low[i] = d[i]
            if d[i] > high[i]:
                high[i] = d[i]

    def scaleinput(d):
        return [(d.data[i] - low[i]) / (high[i] - low[i])
                for i in range(len(low))]

    # [BUG] row.data -> row
    newrows = [matchrow(scaleinput(row) + [row.match]) for row in rows]

    return newrows, scaleinput

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as num
from decimal import Decimal, getcontext

#only allow decimals with 2 decimal places
getcontext().prec = 3

def main():
    global x, y, z

    x = []
    y = []
    z = []

    setupInterval()
    graphSets()
    setUpGraph()

    plot.show()

def setupInterval():
    global loopIndexs

    #[beginning, last, loop increment]
    indexRange = [-10, 10, 0.2]
    loopIndexs = []
    index = indexRange[0]

    while True:
        if (index >= indexRange[1]):
            break

        loopIndexs.append(index)
        index = Decimal(index) + Decimal(indexRange[2])
        print("Added interval:", index)

def graph2VarFunction():
    #Graphing f(x, y) = xy / (x^2 + y^2)

    for xo in loopIndexs:
        for yo in loopIndexs:
            try:
                zo = xo / (xo**2 + yo**2)
            except:
                #Point DNE
                continue

            x.append(float(xo))
            y.append(float(yo))
            z.append(float(zo))

            print("Point graphed:", xo, yo, zo)

def graph3VarFunction():
    #Graphing f(x, y, z) = xyz / (x^2 + y^2 + z^2 + 1)

    for xo in loopIndexs:
        for yo in loopIndexs:
            for zo in loopIndexs:
                try:
                    wo = xo*yo*zo / (xo**2 + yo**2 + zo**2)
                except:
                    #Point DNE
                    continue

                x.append(float(xo))
                y.append(float(yo))
                z.append(float(zo))

                print("Point graphed: (Except for the 4th var)", xo, yo, zo, wo)

def graphSets():
    #xo = x sub 0 or x not
    for xo in loopIndexs:
        for yo in loopIndexs:
            for zo in loopIndexs:
                #equation
                if (Decimal(xo**2) + Decimal(yo**2) / 10 + Decimal(zo**2) == 9):
                    x.append(float(xo))
                    y.append(float(yo))
                    z.append(float(zo))

                    print("Point graphed:", xo, yo, zo)

def graphParametrically():
    #For graphing parametric eqations
    for t in loopIndexs:
        xParametric = t ** 2
        yParametric = t ** 3
        zParametric = t ** 4

        x.append(float(xParametric))
        y.append(float(yParametric))
        z.append(float(zParametric))

    #For graphing the prime line
        xParametric = 2 * t
        yParametric = 3 * t ** 2
        zParametric = 3 * t ** 3

        x.append(float(xParametric))
        y.append(float(yParametric))
        z.append(float(zParametric))

def setUpGraph():
    global x, y, z

    axis = plot.figure().add_subplot(projection = "3d")

    #For plotting a surface
    # z = [[0, 2], [3, 4]]
    # x = [[0, 2], [3, 6]]
    # y = [[0, 2], [3, 4]]
    # axis.plot_surface(num.array(x), num.array(y), num.array(z), linewidth = 2.0)

    axis.scatter(x, y, z)

    #make axis lines
    axis.set_xlabel("X")
    axis.set_ylabel("Y")
    axis.set_zlabel("Z")

    #make quiver
    x, y, z = num.array([[-10, 0, 0], [0, -10, 0], [0, 0, 10]])
    u, v, w = num.array([[10, 0, 0], [0, 10, 0], [0, 0, -10]])
    axis.quiver(x, y, z, u, v, w, color="red")

if (__name__ == "__main__"):
    main()
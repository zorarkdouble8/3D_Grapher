# 3D_Grapher
This is a basic 3D grapher that uses matplotlib, numpy, and decimal to achieve accurate looking graphs

## How to use
Run grapher.py and it will show a window of the graph

What it does:
    -Generates a list of intervals in which other functions will use
    -Adds the points to be plotted to the x, y, and z list
    -Sets up the graph and graphs the points in the x, y, z list ((x[0], y[0], z[0]) would be a point)

### Functions:
**setupInterval:** This is where the application will make the intervals. To edit the interval, edit the indexRange vals in the form: [beginning, last, loop increment]

**setupGraph:** This is where the graph gets setup and where the points gets inserted into the graph. Note: *axis.scatter* inserts the 
x, y, z, lists into the graph

**graphSets:** This is where you can graph the equations of planes and such. The way this works is as follows:
    1. Goes through the interval using 3 for statements (each for xo, yo, and zo)
    2. Tests if the point xo, yo, zo is equal *This is where you would put your equation*
    3. If it is equal, add the point to the x, y, and z, list

**graphParametrically:** This is where you can graph paramectricized equations. This is how it works:
    1. Goes through the interval (t)
    2. Each value of t is then plugged into xParametric, yParametric, and zParametric *This is where you put your equation*
    3. xParametric, yParametric, and zParametric is then appended to the x, y, z list

**graph2VarFunction:** This is where you can graph multi-variable graphs. This is how it works:
    1. Loops though the interval and assigns the values to xo, yo
    2. Gets zo from the equation involving xo and yo *this is where you put your equation*
    3. If an error occurs in the try, except statement (Like if the formula tried to divide by 0) then it will skip that iteration (step 4)
    4. xo, yo, zo is added to the x, y, z list

# Copyright
Anyone may copy, edit, and contribute to this project. However, you cannot monitize nor distribute this software
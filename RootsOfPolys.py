# Polynomial object, constructor assumes polynomial is a tuple ordered from constant to leading.

class Polynomial(object):
    def __init__(self,polynomial):
        self.polynomial = polynomial

    def getCoefficientAtDegree(self,number):
        # Gets the coefficient at the specific degree
        return self.polynomial[number]

    def getPoly(self):
        # Returns the polynomial as a tuple
        return self.polynomial

    def getPolyDegree(self):
        # Returns the polynomials degree
        return len(self.polynomial)-1

    def getLeading(self):

        # Returns the leading coefficient
        return self.getCoefficientAtDegree(-1)

    def getConstant(self):

        # Returns the constant coefficient
        return self.getCoefficientAtDegree(0)

    def setPoly(self,polynomial):

        # Sets the polynomial to the specified tuple
        self.polynomial = polynomial



class Calculator(object):
    # Calculator parent object, contains all methods child classes will share

    def __init__(self,polynomial):
        # Assumes polynomial is an object of type Polynomial
        self.polynomial = polynomial

    def getPoly(self):
        return self.polynomial.getPoly()

    def getCoefficientAtDegree(self,degree):

        # Returns the coefficient at the specified degree
        return self.polynomial.getCoefficientAtDegree(degree)

    def getConstant(self):
        return self.polynomial.getConstant()

    def getLeading(self):
        return self.polynomial.getLeading()

    def getPolyDegree(self):

        # Returns a tuple containing the polynomials degree in ascending order
        degree = self.polynomial.getPolyDegree() + 1
        ans = []
        for x in range(degree):
            ans.append(x)

        return tuple(ans)

    def solvePoly(self,number):

        # Solves the polynomial as a function of x, where x is equal to number
        ans = 0.0
        degree = self.getPolyDegree()

        for exponent in degree:
            ans += self.getCoefficientAtDegree(exponent)*(number**exponent)

        return ans

    def setPoly(self, polynomial):

        # Sets polynomial value to a new polynomial
        self.polynomial.setPoly(polynomial)

    def orderPoly(self):

        # Returns the polynomial in standard form as a tuple
        ans = list(self.polynomial.getPoly())
        ans.reverse()
        return tuple(ans)

    def formatPoly(self,polynomial):

        # Formats the polynomial in standard form and returns it as a string
        x = list(polynomial)
        x.reverse()
        ans = "("
        for y in range(len(x)):
            if y == 0:
                ans += self.formatCoefficient(x[y]) + self.formatX(len(x)-1)
                continue
            elif y == len(x)-1:
                if x[y] >= 0:
                    ans += " + " + str(x[y])
                else:
                    ans += " - " + str(abs(x[y]))
                ans += self.formatX(len(x) - y - 1)
                continue
            if x[y] >= 0:
                ans += " + " + self.formatCoefficient(x[y])
            else:
                ans += " - " + self.formatCoefficient(abs(x[y]))
            ans += self.formatX(len(x)-y-1)
        ans += ")"
        return ans

    def formatCoefficient(self,coefficient):

        # Formats the coefficient of the polynomial and returns a string
        if coefficient == 1:
            ans = ""
        else:
            ans = str(coefficient)
        return ans

    def formatX(self,degree):

        # Formats the independent variable and returns a string
        if degree == 0:
            ans = ""
        elif degree == 1:
            ans = "x"
        else:
            ans = "x^"+str(degree)
        return ans

class FactorPolyCalc(Calculator):

    # Factors the given polynomial object
    def __init__(self,polynomial):
        Calculator.__init__(self, polynomial)
        self.zero = 0
        self.zeros = []
        self.polyList = []
        self.pqrList = []
        self.initPoly = self.getPoly()
        self.P = self.calcP()
        self.Q = self.calcQ()
        self.R = self.calcR()
        self.yIntercept = self.solvePoly(0)
        self.factorPoly()

    def calcP(self):

        # Calculates all possible values of P and returns them in a list
        p =[]
        x = self.getConstant()
        if x != 0:
            for y in range(abs(x)):
                if x%(y+1)==0:
                    p.append(y+1)
        else:
            p.append(x)
        return p

    def calcQ(self):

        # Calculates all possible values of Q ans returns them in a list
        q =[]
        x = self.getLeading()
        for y in range(abs(x)):
            if x%(y+1)==0:
                q.append(y+1)
        return q

    def calcR(self):

        # Calculates all possible values of R using P and Q returning it as a string
        p = self.P
        q = self.Q
        r = []
        for x in p:
            for y in q:
                w = x/y
                if w in r:
                    continue
                r.append(w)
        r.sort()
        r.reverse()
        self.pqrList.append((p,q,r))
        return r

    def findRealZero(self):

        # Goes through values in R until it finds one that makes f(x) <= epsilon
        epsilon = .0000000001
        flag = 0
        ans = 0
        for x in self.R:
            w = self.solvePoly(x)
            y = self.solvePoly(-x)
            if abs(w)<=epsilon:
                ans = x
                break
            if abs(y)<=epsilon:
                ans = -x
                break
        try:
            self.zeros.append(ans)
            self.zero = ans
        except:
            flag = 1
        return flag

    def factor(self):

        # Factors the polynomial using synthetic division
        ans =[]
        poly = self.orderPoly()
        ans.append(poly[0])
        for x in poly[1:]:
            ans.append(int(x+self.zero*ans[-1]))
        ans.reverse()
        self.setPoly(tuple(ans[1:]))
        self.polyList.append(self.getPoly())
        self.P = self.calcP()
        self.Q = self.calcQ()
        self.R = self.calcR()

    def factorPoly(self):

        # Factors the polynomial
        while len(self.getPolyDegree()) - 2 > 0:
            flag = self.findRealZero()
            if flag == 1:
                
                break
            self.factor()

    def formatZeros(self,zeros):

        # Formats the zeros and returns them as Strings
        ans = ""
        for x in zeros:
            if zeros[-1] == x:
                ans += str(round(x,2))
            else:
                ans += str(round(x,2)) + ", "
        return ans

    def __str__(self):

        # Formats the output of printing the object
        ans = "Object that factors the polynomial " + self.formatPoly(self.initPoly)
        return ans

    # ///////////////////////////////////////////////////////////////////////

    # User accessible functions

    # ///////////////////////////////////////////////////////////////////////

    def display(self):

        # Displays the data in a user friendly way
        zeros = []
        for y in self.getZeros():
            if y > 0:
                zero = "(x - " + str(round(y,2))+")"
            else:
                zero = "(x + " + str(abs(round(y,2)))+")"
            zeros.append(zero)
        polys = self.polyList
        print("\n**********************************************************")
        print(self.formatPoly(self.initPoly))
        for x in range(len(zeros)):
            cont = 0
            for v in self.pqrList[x]:
                if cont == 0:
                    print(" P =", v)
                elif cont == 1:
                    print(" Q =", v)
                else:
                    print(" R =", v)
                cont += 1
            str_zeros = ""
            for w in zeros[:x+1]:
                str_zeros += w
            print("\n**********************************************************")
            print(str_zeros + self.formatPoly(polys[x]))
        print(" Y-intercept = " + str(self.yIntercept))
        print(" X-intercepts = " + self.formatZeros(self.getZeros()))
        print("**********************************************************")

    def getZeros(self):

        # Returns the polynomials factors
        return self.zeros

    def getYInt(self):

        # Returns the polynomials factors
        return self.yIntercept


# class RationalCalc(object):
#     def __init__(self, polyOne, polyTwo):
#         # polyOne and polyTwo are polynomial objects
#
#         self.polyOne = FactorPolyCalc(polyOne)
#         self.polyTwo = FactorPolyCalc(polyTwo)
#         self.zeros = []
#         self.asymptotes = []
#         self.holes = []






def factorPolyInterface():
    polyInput = input("Enter polynomial separated by blank spaces: ")
    copyPoly = polyInput[:]
    poly = []
    while True:
        y = 0
        for x in range(len(copyPoly)):
            if copyPoly[x] == " ":
                poly.append(int(copyPoly[:x]))
                copyPoly = copyPoly[x+1:]
                y = 1
                break
        if y == 1:
            continue
        else:
            poly.append(int(copyPoly))
            break

    poly.reverse()
    polynomial = Polynomial(tuple(poly))
    calc = FactorPolyCalc(polynomial)
    calc.display()


def runInterface():
    while True:
        indicator = input("1 to run program, any other number to exit: ")
        try:
            indicator = int(indicator)
            if indicator == 1:
                factorPolyInterface()
            else:
                break
        except ValueError:
            print("Your input is invalid")


runInterface()

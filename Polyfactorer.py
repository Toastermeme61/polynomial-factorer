class Term(object):
    #Term object, is the parent object for all other terms
    
    def __init__(self, coefficient):
        #Constructs the term object using the corresponding coefficient
        
        self.coefficient = coefficient   
    def getCoefficient(self):
        #Returns the terms coefficient
        
        return self.coefficient  
    def setCoefficient(self,coefficient):
        #Sets the terms coefficient
        
        self.coefficient = coefficient
        
class PolynomialTerm(Term):
    #Polynomial term, represents 1 polynomial term
    
    def __init__(self, coefficient, exponent):
        #Constructs the polynomial term object using the corresponding coefficient and exponent
        
        Term.__init__(self,coefficient)
        self.exponent = exponent
    def getExponent(self):
        #Returns the terms exponent or degree
        
        return self.exponent
    def setExponent(self,exponent):
        #Sets the terms exponent or degree
        
        self.exponent = exponent
    def solve(self,independentVariable):
        #Solves the polynomial term with the inputed independet variable (x), returning the corresponding value
        
        return self.getCoefficient()*independentVariable**self.getExponent()

class Polynomial(object):
    #Object of type Polynomial, made up of multiple PolynomialTerm objects
    
    def __init__(self, polynomial):
        #Constructs the Polynomial object using a list of tuples, each tuple containing two values
        #The first containing the terms coefficient and the second value containing its degree
        
        self.polynomial = self.createPolynomial(polynomial)
    def createPolynomial(self, listPoly):
        #Takes a list containing the tuples representing the polynomial terms and creates a new list where
        #each index contains an object of type PolynomialTerm corresponding witht he original tuples and returns the list
        
        polynomial = []
        for x in listPoly:
            polynomial.append(PolynomialTerm(x[0],x[1]))
        return polynomial
    def setPolynomial(self, polynomial):
        #Uses a list of tuples to create a new list of PolynomialTerm objects and sets it to self.polynomial
        
        self.polynomial = self.createPolynomial(polynomial)
    def getPolynomialDegree(self):
        #Returns the polynomials degree, assuming the PolynomialTerm object at index 0 is the leading term
        
        return self.polynomial[0].getExponent()
    def getTermAtDegree(self,degree):
        #Returns the PolynomialTerm object corresponding to the specific degree
        
        return self.polynomial[self.getPolynomialDegree() - degree]
    def getCoefficientAtDegree(self,degree):
        #Returns the coefficient at the corresponding degree
        
        return self.getTermAtDegree(degree).getCoefficient();
    def getLeadingTerm(self):
        #Returns the leading PolynomialTerm object of the polynomial function
        
        return self.getTermAtDegree(self.getPolynomialDegree())
    def getLeadingCoefficient(self):
        #Returns the leading coefficient of the Polynomial function
        
        return self.getLeadingTerm().getCoefficient();
    def getConstantTerm(self):
        #Returns the constant PolynomialTerm object of the polynomial function
        
        return self.getTermAtDegree(0)
    def getConstantCoefficient(self):
        #Returns the constant coefficient of the Polynomial function
        
        return self.getConstantTerm().getCoefficient();
    
    def solve(self,independentVariable):
        #Solves the polynomial for the given independent variable and returns the corresponding value
        
        ans = 0
        for x in range(self.getPolynomialDegree()+1):
            ans += self.getTermAtDegree(x).solve(independentVariable)
        return ans
    
class PolynomialFactorer(object):
    #PolynomialFactorer object, finds all the real rational zeros for the given polynomial and factors it
    
    def __init__(self, polynomial):
        #Constructs the PolynomialFactorer object by setting the given Polynomial object to the instance variable self.polynomial
        
        self.polynomial = polynomial
    def calcP(self):
        #Calculates all possible divisors for the constant coefficient and returns them in a list
        
        p =[]
        coefficient = self.polynomial.getConstantCoefficient()
        if coefficient != 0:
            for x in range(abs(coefficient)):
                if coefficient%(x+1) == 0:
                    p.append(x+1)
        else:
            p.append(coefficient)
        return p
    
    def calcQ(self):
        #Calculates all possible divisors for the leading coefficient and returns them as a list
        
        q =[]
        coefficient = self.polynomial.getLeadingCoefficient()
        if coefficient != 0:
            for x in range(abs(coefficient)):
                if coefficient%(x+1) == 0:
                    q.append(x+1)
        else:
            q.append(coefficient)
        return q
    
    def calcR(self):
        #Calculates all the possible values for dividing P/Q and returns it as a list without repeating values
        
        p = self.calcP()
        q = self.calcQ()
        r =[]
        for x in p:
            for y in q:
                w = x/y
                if w in r:
                    continue
                r.append(w)
        r.sort()
        r.reverse()
        return r
    
    def solvePoly(self, indVariable):
        #Solves the polynomial for the corresponding independent variable and returns the corresponding value
        
        return self.polynomial.solve(indVariable)
    
    def findRealZero(self):
        #Solves polynomial for values of R until the corresponding value is equal to 0 and returns the corresponding value
        
        epsilon = .0000000001
        ans = 0
        for x in self.calcR():
            positive = self.solvePoly(x)
            negative = self.solvePoly(-x)
            if abs(positive)<=epsilon:
                ans = x
                break
            if abs(negative)<=epsilon:
                ans = -x
                break
        if type(ans) == int:
            print("No real zero")
        return ans

##    def synthethicDivision(self):
##        zero = self.findRealZero()
##        orderedPoly  =[]
##        for x in 
            
poly = Polynomial([(6,4),(1,3),(-56,2),(-9,1),(18,0)])
factorer = PolynomialFactorer(poly)
print(factorer.findRealZero())
print(factorer.solvePoly(factorer.findRealZero()))

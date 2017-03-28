class Term(object):
    def __init__(self, coefficient):
        self.coefficient = coefficient   
    def getCoefficient(self):
        return self.coefficient  
    def setCoefficient(self,coefficient):
        self.coefficient = coefficient
        
class PolynomialTerm(Term):
    def __init__(self, coefficient, exponent):
        Term.__init__(self,coefficient)
        self.exponent = exponent
    def getExponent(self):
        return self.exponent
    def setExponent(self,exponent):
        self.exponent = exponent
    def solve(self,independentVariable):
        return self.getCoefficient()*independentVariable**self.getExponent()

class Polynomial(object):
    def __init__(self, polynomial):
        self.polynomial = self.createPolynomial(polynomial)
    def createPolynomial(self, listPoly):
        polynomial ={}
        for x in listPoly:
            polynomial[x[1]] = PolynomialTerm(x[0],x[1])
        return polynomial
    def setPolynomial(self, polynomial):
        self.polynomial = self.createPolynomial(polynomial)
    def getTermAtDegree(self,degree):
        return self.polynomial[degree]
    def getCoefficientAtDegree(self,degree):
        return self.getTermAtDegree(degree).getCoefficient();
    def getLeadingTerm(self):
        return self.getTermAtDegree(max(self.polynomial))
    def getLeadingCoefficient(self):
        return self.getLeadingTerm().getCoefficient();
    def getConstantTerm(self):
        return self.getTermAtDegree(min(self.polynomial))
    def getConstantCoefficient(self):
        return self.getConstantTerm().getCoefficient();
    def solve(self,independentVariable):
        ans = 0
        for x in self.polynomial:
            ans += self.getTermAtDegree(x).solve(independentVariable)
        return ans
class PolynomialFactorer(object):
    def __init__(self, polynomial):
        self.polynomial = polynomial
    def calcP(self):
        p =[]
        coefficient = self.polynomial.getConstantCoefficient()
        if coefficient != 0:
            for x in range(abs(coefficient)):
                if coefficient%(x+1) == 0:
                    p.append(x+1)
        else:
            p.append(coefficient)
        return p
poly = Polynomial([(1,2),(1,1),(1,0)])
print(poly.solve(2))

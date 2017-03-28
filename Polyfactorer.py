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
        polynomial =[]
        for x in listPoly:
            polynomial.append(PolynomialTerm(x[0],x[1]))
        return polynomial
    def solve(self,independentVariable):
        ans = 0
        for x in self.polynomial:
            ans += x.solve(independentVariable)
        return ans
poly = Polynomial([(1,2),(1,1),(1,0)])
print(poly.solve(2))

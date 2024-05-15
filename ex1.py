def load_data():
    matrixD = []
    matrixY = []
    f = open('smartphone.txt', 'r')
    while True:
        line = f.readline()
        line = line.rstrip('\n')
        if len(line) == 0:
            break
        (a,n,d) = line.partition('  ')
        (b, n, c) = d.partition('  ')
        matrixD.append([float(a), float(b)])
        matrixY.append([float(c)])
    return [matrixD,matrixY]
def gradientDescent(filename, alpha=0.1, max_iter=1000, threshold=0.001):
    cost_J = float('inf')
    max_iter = 1000
    iter = 1
    Costs = []
    matrixs = load_data()
    Y = matrixs[1]
    Data= select_single(matrixs[0],0)
    Hypothesis = [0,0]
    while(True):
        error = computeErrors(Data, Y, [0, 0])
        cost = computeCost(Data,Y,Hypothesis)
        grandiant= computeGradient(Data,error)
        Costs.append(cost)
        Hypothesis = updateHypothsis(Hypothesis, alpha, grandiant)
        if(cost_J<cost or iter>max_iter):
            break
        cost_J=cost

    print(computeCost(Data,Y, Hypothesis))
    return Hypothesis

def predict_value(Example: list, Hypothesis: list):
    prediction = 0
    for i in range(Example.__len__()):
        prediction += Example[i] * Hypothesis[i]
    return prediction


def select_single(D,n):
    D1 = []
    for i in range (D.__len__()):
        D1.append(D[i][n])
    return addOnesColum(D1)
def addOnesColum(D1: list):
    for i in range(D1.__len__()):
        D1[i] = [1, D1[i]]
    return D1

def computeErrors (Data: list, Y:list, Hypothesis:list):
    v = []
    if(Data.__len__()!= Y.__len__()):
        return []
    for i in range(0, Data.__len__()):
        v.append(predict_value(Data[i], Hypothesis) - Y[i][0])
    return v
def computeCost(Data:list , Y:list , Hypothesis:list):
    errors = 0
    v:list = computeErrors(Data,Y,Hypothesis)
    for i in range(0, (v.__len__())):
        errors += v[i]*v[i]
    return errors/(2*Data.__len__())
def computeGradient(Data:list, Errors:list):
    gradiants = []
    g =0
    print(Data.__len__() == Errors.__len__())
    for i in range(0,Data[0].__len__()):
        for j in range(0,Data.__len__()):
            g += Data[j][i]*Errors[j]
        g /= Data.__len__()
        gradiants.append(g)
    return gradiants
def updateHypothsis(Hypothesis, alpha, Gradient):
    new = [Hypothesis[i] - alpha*Gradient[i] for i in range(0,Hypothesis.__len__())]
    return new


if __name__ == '__main__':
    print(gradientDescent("smartphone.txt"))






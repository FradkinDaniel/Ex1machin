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
        matrixD.append([a,b])
        matrixY.append([c])
    return [matrixD,matrixY]
def gradiant_decent(matrix):
    hy = [0 for i in range(5)]
    alpha = 0.1
    cost_j = 100000000000000000
    max_iter = 1000
    iter = 1
def predict_value(Example: list, Hypothesis: list):
    prediction = 0
    for i in range(Example.__len__()):
        prediction += Example[i] * Hypothesis[i]
        print("prediction:%d",prediction)
    return prediction


def select_single(D,n):
    D1 = []
    for i in range (D.__len__()):
        D1.append(D[i][n])
        print(D1[i])
    return addOnesColum(D1)
def addOnesColum(D1: list):
    for i in range(D1.__len__()):
        D1[i] = [1, D1[i]]
    return D1

def computeErrors (Data: list, Y:list, Hypothesis:list):
    v = list
    if(Data.__len__!= Y.__len__()):
        return []
    for i in range (0,Data.__len__()):
        v.append(predict_value(Data[i], Hypothesis)-Y[i])
    return v
def computeCost(Data, Y, Hypothesis):
    print("in")
    errors = 0
    v:list = computeErrors(Data,Y,Hypothesis)
    for i in v:
        errors += i*i
        print(errors)
    print(errors/(2*Data.__len__()))
    return errors/(2*Data.__len__())



if __name__ == '__main__':
    matrixs = load_data()
    Y = matrixs[1]
    Data:list = select_single(matrixs[0],0)
    print(computeCost(Data, Y,[0,0]))






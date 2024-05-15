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
def computeErrors (Data, Y, Hypothesis):





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
if __name__ == '__main__':
    matrixs = load_data()
    select_single(matrixs[0],1)






import sys
from knn_classifier import knn_classifier


def main():
    try:
        number_of_neighbours = sys.argv[1]
    except:
        print("Usage: python3 main.py <num_neighbours>",file=sys.stderr)
        sys.exit(1)
    test = knn_classifier.read_file('iris_test.csv')
    #print(*test, sep='\n')
    training = knn_classifier.read_file('iris_treino.csv')
    #print(*training,sep='\n')
    k = knn_classifier(test)
    k.analyse(test, training, number_of_neighbours)
    k.show_matrix()

if __name__ == '__main__':
    main()
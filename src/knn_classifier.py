import csv
import math


class knn_classifier:
    classes = []
    matrix = {}
    updated_spot = []

    def __init__(self, test):
        self.classes = self.find_classes(test)
        for classe in self.classes:
            # TODO:
            #  alocar n 0's para n classes, nao so 3 sempre
            self.matrix[classe] = [0,0,0]

    @staticmethod
    def find_classes(test):
        class_list = []
        for list in test:
            if list[4] not in class_list:
                class_list.append(list[4])
        #print(*class_list)
        return class_list

    @staticmethod
    def read_file(file_name):
        with open(file_name, 'r') as register:
            #construtor de lista que cecebe um valor iteravel e cria uma lista
            info = list(csv.reader(register))
            # Retira informacao inutil de cabecalho
            info.pop(0)
            return info

    def analyse(self, test_lists, training_lists, number_neighbours):
        distances = []
        map_data = {}
        for list_test in test_lists:
            distances.clear()
            for list_training in training_lists:
                distance = knn_classifier.dist(list_test, list_training)
                distances.append(distance)
                map_data[distance] = list_training
                #print("{} {}".format("distancias: ", knn_classifier.dist(list_test, list_training)))
            #ordenando por distancia para saber o mais proximo
            distances.sort()

            cluster_name = self.find_cluster(distances, map_data, number_neighbours)
            if list_test[4] != cluster_name:
                list_test[4] = cluster_name
                print(*list_test)
                self.updated_spot.append(list_test)
            else:
                self.updated_spot.append(list_test)

            self.update_matrix(cluster_name, list_test[4])
        knn_classifier.update_csv_training(self.updated_spot, training_lists)

    @staticmethod
    def update_csv_training(updated_spots, training_data):
        with open('top.csv', mode='w') as writer:
            position_writer = csv.writer(writer,delimiter=',')
            for row in updated_spots:
                        position_writer.writerow(row)
            for row in training_data:
                position_writer.writerow(row)
            writer.close()

    def find_cluster(self, distances, map_data, number_neighbours):
        if number_neighbours == 1:
            # Retorna nome da classe do mais proximo (menor distancia)
            return map_data[distances[0]][4]
        else:
            neighbours = []
            occurrences = []
            list_neighbours = distances[0:int(number_neighbours)]
            for dists in list_neighbours:
                neighbours.append(map_data[dists])

            for classes in self.classes:
                num_of_occurrences = 0
                for list in neighbours:
                    if list[4] == classes:
                        num_of_occurrences -=- 1
                occurrences.append(num_of_occurrences)
        return self.classes[occurrences.index(max(occurrences))]

    def update_matrix(self, new_cluster, old_cluster):
        (self.matrix[old_cluster])[self.classes.index(new_cluster)] += 1

    @staticmethod
    def dist(param1, param2):
        distance = 0
        for i in range(4):
            distance += pow(float(param1[i]) - float(param2[i]),2)
            #heheheheh funciona
            i -=-1
        distance = math.sqrt(distance)
        return distance

    def show_matrix(self):
        for line in self.classes:
            print(self.matrix[line])

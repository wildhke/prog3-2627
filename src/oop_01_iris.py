import pandas as pd

class Vehicle:
    def __init__(self, power, color, wheel_base):
        self.power = power
        self.color = color
        self.wheel_base = wheel_base


class IrisData:
    def __init__(self):
        self.data = None
        self.name = "Iris"
        self.unique_class_names = None

    def read_csv(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def get_distinct_classes(self):
        self.unique_class_names = self.data["Species"].tolist()


    @classmethod
    def from_csv(cls, csv_file):
        iris = cls()
        iris.read_csv(csv_file)
        return iris



if __name__ == "__main__":
    path = "./data/Iris.csv"

    iris_data = IrisData()
    iris_data.read_csv(path)
    #print(iris_data.data.head())
    #print( iris_data.get_distinct_classes())
    #print(iris_data.unique_class_names)
    #print("---"*10)
    iris2 = IrisData.from_csv(path)
    #print(iris2.data.head(n=10))
    #print(iris2.get_distinct_classes())

    porsche = Vehicle(350, "black", 3.95)
    print(porsche.power)
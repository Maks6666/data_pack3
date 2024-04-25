# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).
import pickle
import gzip

class CapitalsPickle:
    def __init__(self, dct):
        self.dct = dct

    def save_data_pck(self, data):
        self.data = data
        with open("capitals.pickle", "wb") as file:
            pickle.dump(data, file)
        return "Data saved."

    def read_data_pck(self):
        with open("capitals.pickle", "rb") as file:
            read_data = pickle.load(file)
        return read_data

    def add_data_pck(self):
        with open("capitals.pickle", "wb") as file:
            num_of_values = int(input("How many keys/values do you want to append?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1}: ")
                value = input(f"Input value for key '{key}': ")
                self.dct[key] = value
            pickle.dump(self.dct, file)
            return "Data saved."

    def del_data(self):
        with open("capitals.pickle", "wb") as file:
            num_of_values = int(input("How many values fo you want to delete?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1} to delete: ")
                del self.dct[key]
            pickle.dump(self.dct, file)
            return "Data saved."


dct = {"UK": "London", "France": "Paris", "USA": "Washington"}
dict_1 = CapitalsPickle(dct)
dict_1.save_data_pck(dct)
dict_1.add_data_pck()
dict_1.del_data()
print(dict_1.read_data_pck())


class CapitalsGzip:
    def __init__(self, dct):
        self.dct = dct

    def save_data_gz(self, data):
        with gzip.open("g_capitals.gz", "wb") as file:
            serialized_data = pickle.dumps(data)
            file.write(serialized_data)

    def read_data_gz(self):
        with gzip.open("g_capitals.gz", "rb") as file:
            serialized_data = file.read()
            read_data = pickle.loads(serialized_data)
        return read_data

    def add_data_gz(self):
        with gzip.open("g_capitals.gz", "wb") as file:
            num_of_values = int(input("How many keys/values do you want to append?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1}: ")
                value = input(f"Input value for key '{key}': ")
                self.dct[key] = value
            serialized_data = pickle.dumps(self.dct)
            file.write(serialized_data)


    def del_data_gz(self):
        with gzip.open("g_capitals.gz", "wb") as file:
            num_of_values = int(input("How many values fo you want to delete?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1} to delete: ")
                del self.dct[key]
            serialized_data = pickle.dumps(self.dct)
            file.write(serialized_data)


dct = {"UK": "London", "France": "Paris", "USA": "Washington"}
dict_1 = CapitalsGzip(dct)
dict_1.save_data_gz(dct)
dict_1.add_data_gz()
dict_1.del_data_gz()
print(dict_1.read_data_gz())


# Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування).
import pickle
import gzip

class BandsPickle:
    def __init__(self, dct):
        self.dct = dct

    def save_data_pck(self, data):
        self.data = data
        with open("bands_1.pickle", "wb") as file:
            pickle.dump(data, file)
        return "Data saved."

    def read_data_pck(self):
        with open("bands_1.pickle", "rb") as file:
            read_data = pickle.load(file)
        return read_data

    def add_data_pck(self):
        with open("bands_1.pickle", "wb") as file:
            num_of_values = int(input("How many keys/values do you want to append?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1}: ")
                value = input(f"Input value for key '{key}': ")
                self.dct[key] = value
            pickle.dump(self.dct, file)
            return "Data saved."

    def del_data(self):
        with open("bands_1.pickle", "wb") as file:
            num_of_values = int(input("How many values fo you want to delete?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1} to delete: ")
                del self.dct[key]
            pickle.dump(self.dct, file)
            return "Data saved."


# dct = {"band_1": "album_1", "band_2": "album_2", "band_3": "album_3"}
# dict_1 = BandsPickle(dct)
# dict_1.save_data_pck(dct)
# dict_1.add_data_pck()
# dict_1.del_data()
# print(dict_1.read_data_pck())


class BandsGzip:
    def __init__(self, dct):
        self.dct = dct

    def save_data_gz(self, data):
        with gzip.open("g_bands.gz", "wb") as file:
            serialized_data = pickle.dumps(data)
            file.write(serialized_data)

    def read_data_gz(self):
        with gzip.open("g_bands.gz", "rb") as file:
            serialized_data = file.read()
            read_data = pickle.loads(serialized_data)
        return read_data

    def add_data_gz(self):
        with gzip.open("g_bands.gz", "wb") as file:
            num_of_values = int(input("How many keys/values do you want to append?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1}: ")
                value = input(f"Input value for key '{key}': ")
                self.dct[key] = value
            serialized_data = pickle.dumps(self.dct)
            file.write(serialized_data)


    def del_data_gz(self):
        with gzip.open("g_bands.gz", "wb") as file:
            num_of_values = int(input("How many values fo you want to delete?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1} to delete: ")
                del self.dct[key]
            serialized_data = pickle.dumps(self.dct)
            file.write(serialized_data)


dct = {"band_1": "album_1", "band_2": "album_2", "band_3": "album_3"}
dict_1 = BandsGzip(dct)
dict_1.save_data_gz(dct)
dict_1.add_data_gz()
dict_1.del_data_gz()
print(dict_1.read_data_gz())


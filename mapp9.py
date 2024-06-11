class Fruit:
    def add_fruit(self, fruit):
        return fruit + " buah"

# Daftar nama buah
fruits = ["apel", "pisang", "jeruk", "mangga"]

# Membuat instance dari kelas Fruit
processor = Fruit()

# Menggunakan map() dengan metode add_fruit() dari kelas Fruit
fruits_with_buah = map(processor.add_fruit, fruits)

# Mengonversi objek map ke dalam list untuk melihat hasilnya
fruits_with_buah_list = list(fruits_with_buah)
print(fruits_with_buah_list) 

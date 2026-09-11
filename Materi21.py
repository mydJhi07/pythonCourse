# Membuat 3 list biasa (1D)
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# Menggabungkannya menjadi 2D List
groceries = [fruits, vegetables, meats]

# ATAU bisa juga ditulis langsung seperti ini:
# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]

# --- Cara Mengakses ---
# Mengakses baris pertama (Mengembalikan seluruh list fruits)
print(groceries[0]) 

# Mengakses baris pertama, kolom pertama (Mengembalikan "apple")
print(groceries[0][0]) 

# Mengakses baris kedua, kolom kedua (Mengembalikan "carrots")
print(groceries[1][1])


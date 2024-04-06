def Mahasiswa(name, age, address):
    return {'name': name, 'age': age, 'address': address}

mhs = Mahasiswa(
    name= "John Lennon",
    age= 20,
    address="Kabupaten Tangerang"
)

print("Name : ", mhs['name'])
print("Age :", mhs['age'])
print("Address : ", mhs['address'])
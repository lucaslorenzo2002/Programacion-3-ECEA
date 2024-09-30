class Export:
    def __init__(self, data):
        self.data = data

    def exportFile(self):
        with open('Cuil.txt', "w") as file: 
            file.write(f'Genre: {self.data.get("genero")}, Dni: {self.data.get("dni")}, Cuil: {self.data.get("cuil")}')
    
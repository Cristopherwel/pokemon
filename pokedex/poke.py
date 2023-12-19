import tkinter as tk
import requests

class Pokemon:      #creacion de la clase, metodos y widgets
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Pokemon")
        self.ventana.geometry("300x200")
        self.nombre_label = tk.Label(self.ventana, text="Ingresar nombre del Pokemon:")
        self.nombre_label.pack()  
        self.nombre_entrada = tk.Entry(self.ventana)
        self.nombre_entrada.pack()
        self.pokemon_label = tk.Label(self.ventana, text="")
        self.pokemon_label.pack()
        self.boton = tk.Button(self.ventana, text="Buscar Pokemon", command=self.obtener_info_poke)
        self.boton.pack()
        
        # almacenar los atributos de cada pokemon segun la API
        self.id_pokemon = ""
        self.nombre_pokemon = ""
        self.tipos = ""
        self.vida = ""
        self.daño = ""
        
    def obtener_info_poke(self):
        nombre_pokemon = self.nombre_entrada.get() # se obtiene informacion del Pokemon ingresado por el usuario
        
        # URL de la API para obtener informacion de cada pokemon  
        urlApi = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
        pokemon = requests.get(urlApi)  # se realiza la solicitud a la API
        
        # Verificacion de la respuesta de la solicitud
        if pokemon.status_code == 200: # Si la respuesta booleana es True la solicitud es correcta
            # datos de cada pokemon en respuesta JSON
            datos_pokemon = pokemon.json()
            self.id_pokemon = datos_pokemon["id"]
            self.nombre_pokemon = datos_pokemon["name"]
            
            tipos = ", ".join([tipo['type']['name'] for tipo in datos_pokemon['types']])
            self.tipos = tipos
            
            for i in datos_pokemon['stats']:
                if i['stat']['name'] == 'hp':
                    self.vida = i['base_stat']
                elif i['stat']['name'] == 'attack':
                    self.daño = i['base_stat']
                    
            # texto que se mostrara en la etiqueta de la interfaz gráfica
            info_pokemon = f"Pokémon encontrado:\n"
            info_pokemon += f"Nombre: {self.nombre_pokemon}\n"
            info_pokemon += f"ID: {self.id_pokemon}\n"
            info_pokemon += f"Tipos: {self.tipos}\n"
            info_pokemon += f"Puntos de Vida: {self.vida}\n"
            info_pokemon += f"Daño: {self.daño}"
            
            # una vez buscado un pokemon se mostraran los datos del mismo en la interfaz grafica
            self.pokemon_label.config(text=info_pokemon)
        else:
            #Si el pokemon no existe aparecera este mensaje
            self.pokemon_label.config(text="Pokémon no encontrado")

#inicia o ejcuta la ventana
if __name__ == "__main__":
    ventana = tk.Tk()
    a = Pokemon(ventana)
    ventana.mainloop()
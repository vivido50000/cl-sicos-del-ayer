import tkinter as tk
import qrcode
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

# <----------------------------------Colores---------------------------------->
gris_oscuro = "#333"      # Color gris oscuro
gris_claro = "#555"       # Color gris claro
amarillo = "#ffcc00"      # Color amarillo
naranja = "#ff8c00"       # color naranja
negro_palido = "#1c1c1c"  # Color negro pálido
blanco = "#FEFBF6"        # Color blanco
rojo_fuerte = "#750E21"   # Color rojo fuerte
amarillo_cine = "#FFEB3B"  

# <----------------------------------Crear Grupos de Películas---------------------------------->
def agregar_pelicula(contenedor, titulo, imagen_path, command):
    pelicula = tk.Frame(contenedor, borderwidth=2,
                        relief="flat", bg=blanco)
    pelicula.pack(side=tk.LEFT, padx=10, pady=10)

    # Cargar y redimensionar la imagen de la película
    imagen_original = Image.open(imagen_path)
    nuevo_tamaño = (400, 300)  # Ajusta el tamaño según tus necesidades
    imagen_redimensionada = imagen_original.resize(nuevo_tamaño)
    imagen = ImageTk.PhotoImage(imagen_redimensionada)

    imagen_label = tk.Label(pelicula, image=imagen, bg=rojo_fuerte)
    # Necesario para evitar que la imagen se recolecte como basura
    imagen_label.image = imagen
    imagen_label.pack()

    info_pelicula = tk.Frame(pelicula, bg=blanco)
    info_pelicula.pack()

    titulo_pelicula = tk.Label(info_pelicula, text=titulo, font=("Arial", 29), bg=blanco, fg=gris_oscuro)
    titulo_pelicula.pack()

    boton_info = tk.Button(info_pelicula,text="Más información",font=("Arial",15,"bold"),bg=gris_oscuro,fg=blanco,command=command,highlightbackground=rojo_fuerte,highlightthickness=10)
    boton_info.pack(pady=10)


def contenedor_de_horarios(container, movie_title, showtimes, col, row):
    """Crea un grupo de horarios de películas en el contenedor especificado con un estilo moderno y esquinas redondeadas."""
    # Crear un frame con un estilo moderno y esquinas redondeadas
    movie_frame = tk.Frame(container, bg="#424242", bd=0, relief="flat")
    movie_frame.grid(column=col, row=row, padx=10, pady=10)  # Reducimos padx y pady para que los elementos estén más cerca

    # Añadir un borde externo con esquinas redondeadas (efecto tarjeta)
    card_frame = tk.Frame(movie_frame, bg="#2E2E2E", bd=2, relief="flat", 
                          highlightbackground="#3B3B3B", highlightthickness=2)
    card_frame.pack(fill="both", expand=True, padx=5, pady=5, ipadx=5, ipady=5)

    # Añadir esquinas redondeadas al frame (efecto visual)
    card_frame.config(highlightbackground="#6D6D6D", highlightcolor="#6D6D6D", highlightthickness=2)
    
    # Crear una etiqueta para el título de la película con estilo moderno
    title_label = tk.Label(card_frame, text=movie_title, bg="#3C3C3C", fg="white", 
                           font=("Arial", 16, "bold"), anchor="center", padx=10, pady=10)
    title_label.pack(fill="x", pady=(5, 5))  # Espacio superior e inferior del título

    # Etiqueta para los horarios con un diseño más estilizado
    showtimes_label = tk.Label(card_frame, text=showtimes, bg="#3C3C3C", fg="#A8DADC",  # Color de acento suave
                               font=("Arial", 12, "italic"), padx=10, pady=5)
    showtimes_label.pack(fill="x", pady=(0, 10))  # Espacio inferior de los horarios

    # Añadir un sombreado suave para mejorar el diseño
    card_frame.config(highlightbackground="#A8DADC", highlightthickness=2)  # Borde de acento sutil


# <-------------------------------seccion terminada funciones---------------------------------------------------->


def open_peli1(root):
    root.withdraw()
    peli1_window = tk.Toplevel(root)
    peli1_window.title("Cine Retro - El padrino")
    peli1_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    peli1_window.configure(bg="#d3d3d3")

    class CinemaApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Cine Retro - Película 1")

            # Sección de encabezado
            self.header_frame = tk.Frame(self.root, bg="#333333")
            self.header_frame.pack(fill=tk.X)

            # Logo y botón de "Volver"
            self.logo_image = tk.PhotoImage(file="imagenes/logo2.png")
            self.logo = tk.Label(self.header_frame, image=self.logo_image, bg="#333333")
            self.logo.pack(side=tk.LEFT, padx=20)

            self.btn_volver = tk.Button(
                self.header_frame, text="Volver", command=self.volver,
                bg="#ff5733", fg="white", font=("Arial", 12, "bold"), borderwidth=4, relief="raised"
            )
            self.btn_volver.pack(side=tk.RIGHT, padx=20)

            # Cuadro de la película con borde
            self.pelicula_frame = tk.Frame(self.root, bg="#ffffff", padx=15, pady=15, borderwidth=15, relief="ridge")
            self.pelicula_frame.pack(padx=20, pady=20)

            # Título de la película
            self.pelicula_titulo = tk.Label(self.pelicula_frame, text="El Padrino", font=("Arial", 22, "bold"), fg="#ff5733", bg="#ffffff")
            self.pelicula_titulo.pack(pady=(10, 5))

            # Imagen de la película
            imagen_peli = Image.open("peliculas/Elpadrino.png")
            imagen_peli = imagen_peli.resize((400, 400))
            self.imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)
            self.imagen_label = tk.Label(self.pelicula_frame, image=self.imagen_peli_tk, bg="#ffffff")
            self.imagen_label.pack(side=tk.LEFT, padx=10, pady=10)

            # Información de la película y calificación
            self.info_frame = tk.Frame(self.pelicula_frame, bg="#ffffff")
            self.info_frame.pack(side=tk.LEFT, padx=20, pady=10)

            self.genero_label = tk.Label(self.info_frame, text="Género: Acción/Suspenso", font=("Arial", 14), bg="#ffffff")
            self.genero_label.pack(anchor="w", pady=5)

            self.director_label = tk.Label(self.info_frame, text="Idiomas:Español, Ingles, latin, italiano y Subtitulada", font=("Arial", 14), bg="#ffffff")
            self.director_label.pack(anchor="w", pady=5)

            self.protagonistas_label = tk.Label(self.info_frame, text="Clasificacion:", font=("Arial", 14), bg="#ffffff")
            self.protagonistas_label.pack(anchor="w", pady=5)

            # Calificación con estrellas
            self.calificacion_label = tk.Label(self.info_frame, text="Calificación: ⭐⭐⭐⭐", font=("Arial", 14), bg="#ffffff")
            self.calificacion_label.pack(anchor="w", pady=5)

            # Botón para comprar entradas
            self.btn_comprar = tk.Button(self.info_frame, text="Comprar Entradas", command=self.open_modal, bg="#ff5733", fg="white", font=("Arial", 16))
            self.btn_comprar.pack(pady=(20, 0))

            # Modal (ventana emergente)
            self.modal_frame = None
            self.setup_modal()

        def volver(self):
            self.root.destroy()  # Cierra la ventana de Película 1
            root.deiconify()  # Reabre la ventana principal

        def setup_modal(self):
            # Configuración del modal (ventana emergente)
            self.modal_frame = tk.Toplevel(self.root)
            self.modal_frame.title("Reserva de Entradas")
            self.modal_frame.geometry("500x600")
            self.modal_frame.config(bg="#f5f5f5")  # Fondo claro
            self.modal_frame.withdraw()  # Ocultar el modal inicialmente

            # Paso 1: Selección de horario y día
            self.paso1_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.paso1_frame.pack(pady=15)

            tk.Label(self.paso1_frame, text="Seleccione el horario y el día", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Opciones para horarios
            tk.Label(self.paso1_frame, text="Horario:", bg="#ffffff").pack()
            horarios = ["15:00", "18:00", "21:00"]
            self.horario_var = tk.StringVar(value=horarios[0])
            tk.OptionMenu(self.paso1_frame, self.horario_var, *horarios).pack(pady=5)

            # Opciones para días
            tk.Label(self.paso1_frame, text="Día:", bg="#ffffff").pack()
            dias = ["10/10/2024", "11/10/2024", "12/10/2024"]
            self.dia_var = tk.StringVar(value=dias[0])
            tk.OptionMenu(self.paso1_frame, self.dia_var, *dias).pack(pady=5)

            self.siguiente_btn = tk.Button(self.paso1_frame, text="Siguiente", command=self.show_asientos, 
                                           bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                           relief="flat", padx=5, pady=5)
            self.siguiente_btn.pack(pady=10)

            # Paso 2: Selección de asientos
            self.paso2_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso2_frame, text="Elija sus asientos", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Label para mostrar la cantidad de asientos ocupados y disponibles
            self.asientos_info_label = tk.Label(self.paso2_frame, text="Asientos ocupados: 0\nAsientos disponibles: 56", 
                                                font=("Arial", 12), bg="#ffffff")
            self.asientos_info_label.pack(pady=10)

            self.seating_grid = tk.Frame(self.paso2_frame, bg="#ffffff")
            self.seating_grid.pack(pady=10)

            self.asientos_seleccionados = []
            filas, columnas = 7, 8
            letras = 'ABCDEFG'

            self.seats = {}
            for i in range(filas):
                for j in range(columnas):
                    seat_id = f"{letras[i]}{j+1}"  # A1, A2, etc.
                    btn = tk.Button(self.seating_grid, text=seat_id, width=4, height=2, 
                                    bg="#555", fg="#fff", relief="flat", font=("Arial", 10))
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    btn.config(command=lambda b=btn: self.toggle_seat(b))
                    self.seats[seat_id] = btn

            self.confirmar_asientos_btn = tk.Button(self.paso2_frame, text="Confirmar Asientos", 
                                                    command=self.show_comida, bg="#ff8c42", fg="white", 
                                                    font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.confirmar_asientos_btn.pack(pady=10)

            # Paso 3: Selección de comida
            self.paso3_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso3_frame, text="Elija su comida", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            self.comida_var = tk.StringVar(value="Combo 1")
            self.combos = {
                "Combo 1": "Palomitas + Bebida",
                "Combo 2": "Nachos + Refresco",
                "Combo 3": "Hot Dog + Bebida",
                "Sanchez": "Palomitas 2x1",
                "No gracias": "Ninguna"
            }

            for combo, descripcion in self.combos.items():
                tk.Radiobutton(self.paso3_frame, text=f"{combo}: {descripcion}", variable=self.comida_var, 
                               value=combo, bg="#ffffff", font=("Arial", 12)).pack(anchor="w")

            self.siguiente_comida_btn = tk.Button(self.paso3_frame, text="Siguiente", command=self.show_resumen, 
                                                  bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                                  relief="flat", padx=5, pady=5)
            self.siguiente_comida_btn.pack(pady=10)

            # Paso 4: Resumen del pedido
            self.paso4_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.resumen_label = tk.Label(self.paso4_frame, text="Resumen de la compra", font=("Arial", 16, "bold"), 
                                          bg="#ffffff")
            self.resumen_label.pack(pady=10)

            self.confirmar_compra_btn = tk.Button(self.paso4_frame, text="Confirmar Compra", command=self.confirmar_compra, 
                                                  bg="#ff5733", fg="white", font=("Arial", 12, "bold"), relief="flat", 
                                                  padx=5, pady=5)
            self.confirmar_compra_btn.pack(pady=10)

            self.detalles_pedido = tk.Label(self.paso4_frame, font=("Arial", 12), bg="#ffffff")
            self.detalles_pedido.pack(pady=10)

        def open_modal(self):
            self.modal_frame.deiconify()

        def toggle_seat(self, btn):
            seat_id = btn.cget("text")
            if seat_id in self.asientos_seleccionados:
                self.asientos_seleccionados.remove(seat_id)
                btn.config(bg="#555")
            else:
                self.asientos_seleccionados.append(seat_id)
                btn.config(bg="red")

            # Actualiza la información de asientos ocupados y disponibles
            ocupados = len(self.asientos_seleccionados)
            disponibles = 56 - ocupados  # Total de asientos: 56
            self.asientos_info_label.config(text=f"Asientos ocupados: {ocupados}\nAsientos disponibles: {disponibles}")

        def show_asientos(self):
            self.paso1_frame.pack_forget()  # Oculta paso 1
            self.paso2_frame.pack(pady=15)  # Muestra paso 2

        def show_comida(self):
            self.paso2_frame.pack_forget()  # Oculta paso 2
            self.paso3_frame.pack(pady=15)  # Muestra paso 3

        def show_resumen(self):
            self.paso3_frame.pack_forget()  # Oculta paso 3
            self.paso4_frame.pack(pady=15)  # Muestra paso 
            
            # Mostrar los detalles del resumen
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"
            self.detalles_pedido.config(text=resumen)

        def descargar_comprobante(self):
            # Crear el contenido del comprobante
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"

            # Asegúrate de asignar las variables necesarias
            dia_var = self.dia_var.get()
            horario = self.horario_var.get()
            asientos_seleccionados = asientos_texto
            email = "Losclasicosdelayer"    # Suponiendo que tienes un campo 'email_var' en la clase

            contenidoHTML = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: 'Helvetica Neue', Arial, sans-serif;
                        background-color: #f0f2f5;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        width: 70%;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ff6b6b;
                        font-size: 28px;
                        margin-bottom: 10px;
                    }}
                    h2 {{
                        color: #333;
                        font-size: 22px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        line-height: 1.6;
                        font-size: 16px;
                        color: #555;
                    }}
                    .details, .contact-info {{
                        margin-bottom: 30px;
                    }}
                    .details p, .contact-info p {{
                        margin: 8px 0;
                    }}
                    .details label, .contact-info label {{
                        font-weight: bold;
                        color: #333;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 12px 20px;
                        font-size: 16px;
                        color: #fff;
                        background-color: #ff6b6b;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        text-decoration: none;
                        transition: background-color 0.3s ease;
                    }}
                    .btn:hover {{
                        background-color: #ff4a4a;
                    }}
                    .note {{
                        font-style: italic;
                        color: #888;
                        margin-top: 20px;
                        font-size: 14px;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 40px;
                        color: #999;
                        font-size: 14px;
                    }}
                </style>
                <title>Confirmación de Compra - Cine</title>
            </head>
            <body>
                <div class="container">
                    <h1>¡Compra Confirmada!</h1>
                    <p>Gracias por tu compra en nuestro cine! A continuación, te mostramos los detalles de tu reserva.</p>

                    <div class="details">
                        <h2>Detalles de la Película</h2>
                        <p><strong>Película:</strong> El padrino</p>
                        <p><strong>Fecha:</strong> {dia_var}</p>
                        <p><strong>Hora:</strong> {horario}</p>
                        <p><strong>Asientos seleccionados:</strong> {asientos_seleccionados}</p>
                    </div>

                    <div class="contact-info">
                        <h2>Información de Contacto</h2>
                        <p><strong>Telefono:</strong>11 4870 7273</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p class="note">*Si tiene alguna consulta no dude en contactarnos</p>
                    </div>

                    <p class="note">*Por favor, presenta este comprobante en la entrada del cine. ¡Disfruta la película!</p>
                </div>

                <div class="footer">
                    <p>&copy; 2024 CinePlus. Todos los derechos reservados.</p>
                </div>
            </body>
            </html>
            """

            # Crear un archivo HTML con el contenido
            
            file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads',f"entrada.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(contenidoHTML)

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Comprobante generado", f"Comprobante guardado en: {file_path}")

        def confirmar_compra(self):
            
            # Botón para descargar el comprobante
            self.btn_descargar_comprobante = tk.Button(self.paso4_frame, text="Descargar Comprobante", 
                                                       command=self.descargar_comprobante, bg="#42a5f5", fg="white", 
                                                       font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.btn_descargar_comprobante.pack(pady=10)

    
    app = CinemaApp(peli1_window)  # Asegúrate de pasar peli1_window, no root
    peli1_window.mainloop()  # Asegúrate de que mainloop esté en la ventana emergente


def open_peli2(root):
    root.withdraw()
    peli2_window = tk.Toplevel(root)
    peli2_window.title("Cine Retro - El padrino")
    peli2_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    peli2_window.configure(bg="#d3d3d3")

    class CinemaApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Cine Retro - Película 1")

            # Sección de encabezado
            self.header_frame = tk.Frame(self.root, bg="#333333")
            self.header_frame.pack(fill=tk.X)

            # Logo y botón de "Volver"
            self.logo_image = tk.PhotoImage(file="imagenes/logo2.png")
            self.logo = tk.Label(self.header_frame, image=self.logo_image, bg="#333333")
            self.logo.pack(side=tk.LEFT, padx=20)

            self.btn_volver = tk.Button(
                self.header_frame, text="Volver", command=self.volver,
                bg="#ff5733", fg="white", font=("Arial", 12, "bold"), borderwidth=4, relief="raised"
            )
            self.btn_volver.pack(side=tk.RIGHT, padx=20)

            # Cuadro de la película con borde
            self.pelicula_frame = tk.Frame(self.root, bg="#ffffff", padx=15, pady=15, borderwidth=15, relief="ridge")
            self.pelicula_frame.pack(padx=20, pady=20)

            # Título de la película
            self.pelicula_titulo = tk.Label(self.pelicula_frame, text="Robot Salvaje", font=("Arial", 22, "bold"), fg="#ff5733", bg="#ffffff")
            self.pelicula_titulo.pack(pady=(10, 5))

            # Imagen de la película
            imagen_peli = Image.open("peliculas/Robot Salvaje.png")
            imagen_peli = imagen_peli.resize((400, 400))
            self.imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)
            self.imagen_label = tk.Label(self.pelicula_frame, image=self.imagen_peli_tk, bg="#ffffff")
            self.imagen_label.pack(side=tk.LEFT, padx=10, pady=10)

            # Información de la película y calificación
            self.info_frame = tk.Frame(self.pelicula_frame, bg="#ffffff")
            self.info_frame.pack(side=tk.LEFT, padx=20, pady=10)

            self.genero_label = tk.Label(self.info_frame, text="Género: Acción", font=("Arial", 14), bg="#ffffff")
            self.genero_label.pack(anchor="w", pady=5)

            self.director_label = tk.Label(self.info_frame, text="Idiomas:Español, Ingles Subtitulada", font=("Arial", 14), bg="#ffffff")
            self.director_label.pack(anchor="w", pady=5)

            self.protagonistas_label = tk.Label(self.info_frame, text="Clasificación:ATP", font=("Arial", 14), bg="#ffffff")
            self.protagonistas_label.pack(anchor="w", pady=5)

            # Calificación con estrellas
            self.calificacion_label = tk.Label(self.info_frame, text="Calificación: ⭐⭐⭐⭐⭐", font=("Arial", 14), bg="#ffffff")
            self.calificacion_label.pack(anchor="w", pady=5)

            # Botón para comprar entradas
            self.btn_comprar = tk.Button(self.info_frame, text="Comprar Entradas", command=self.open_modal, bg="#ff5733", fg="white", font=("Arial", 16))
            self.btn_comprar.pack(pady=(20, 0))

            # Modal (ventana emergente)
            self.modal_frame = None
            self.setup_modal()

        def volver(self):
            self.root.destroy()  # Cierra la ventana de Película 1
            root.deiconify()  # Reabre la ventana principal

        def setup_modal(self):
            # Configuración del modal (ventana emergente)
            self.modal_frame = tk.Toplevel(self.root)
            self.modal_frame.title("Reserva de Entradas")
            self.modal_frame.geometry("500x600")
            self.modal_frame.config(bg="#f5f5f5")  # Fondo claro
            self.modal_frame.withdraw()  # Ocultar el modal inicialmente

            # Paso 1: Selección de horario y día
            self.paso1_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.paso1_frame.pack(pady=15)

            tk.Label(self.paso1_frame, text="Seleccione el horario y el día", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Opciones para horarios
            tk.Label(self.paso1_frame, text="Horario:", bg="#ffffff").pack()
            horarios = ["15:00", "18:00", "21:00"]
            self.horario_var = tk.StringVar(value=horarios[0])
            tk.OptionMenu(self.paso1_frame, self.horario_var, *horarios).pack(pady=5)

            # Opciones para días
            tk.Label(self.paso1_frame, text="Día:", bg="#ffffff").pack()
            dias = ["10/10/2024", "11/10/2024", "12/10/2024"]
            self.dia_var = tk.StringVar(value=dias[0])
            tk.OptionMenu(self.paso1_frame, self.dia_var, *dias).pack(pady=5)

            self.siguiente_btn = tk.Button(self.paso1_frame, text="Siguiente", command=self.show_asientos, 
                                           bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                           relief="flat", padx=5, pady=5)
            self.siguiente_btn.pack(pady=10)

            # Paso 2: Selección de asientos
            self.paso2_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso2_frame, text="Elija sus asientos", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Label para mostrar la cantidad de asientos ocupados y disponibles
            self.asientos_info_label = tk.Label(self.paso2_frame, text="Asientos ocupados: 0\nAsientos disponibles: 56", 
                                                font=("Arial", 12), bg="#ffffff")
            self.asientos_info_label.pack(pady=10)

            self.seating_grid = tk.Frame(self.paso2_frame, bg="#ffffff")
            self.seating_grid.pack(pady=10)

            self.asientos_seleccionados = []
            filas, columnas = 7, 8
            letras = 'ABCDEFG'

            self.seats = {}
            for i in range(filas):
                for j in range(columnas):
                    seat_id = f"{letras[i]}{j+1}"  # A1, A2, etc.
                    btn = tk.Button(self.seating_grid, text=seat_id, width=4, height=2, 
                                    bg="#555", fg="#fff", relief="flat", font=("Arial", 10))
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    btn.config(command=lambda b=btn: self.toggle_seat(b))
                    self.seats[seat_id] = btn

            self.confirmar_asientos_btn = tk.Button(self.paso2_frame, text="Confirmar Asientos", 
                                                    command=self.show_comida, bg="#ff8c42", fg="white", 
                                                    font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.confirmar_asientos_btn.pack(pady=10)

            # Paso 3: Selección de comida
            self.paso3_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso3_frame, text="Elija su comida", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            self.comida_var = tk.StringVar(value="Combo 1")
            self.combos = {
                "Combo 1": "Palomitas + Bebida",
                "Combo 2": "Nachos + Refresco",
                "Combo 3": "Hot Dog + Bebida",
                "Sanchez": "Palomitas 2x1",
                "No gracias": "Ninguna"
            }

            for combo, descripcion in self.combos.items():
                tk.Radiobutton(self.paso3_frame, text=f"{combo}: {descripcion}", variable=self.comida_var, 
                               value=combo, bg="#ffffff", font=("Arial", 12)).pack(anchor="w")

            self.siguiente_comida_btn = tk.Button(self.paso3_frame, text="Siguiente", command=self.show_resumen, 
                                                  bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                                  relief="flat", padx=5, pady=5)
            self.siguiente_comida_btn.pack(pady=10)

            # Paso 4: Resumen del pedido
            self.paso4_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.resumen_label = tk.Label(self.paso4_frame, text="Resumen de la compra", font=("Arial", 16, "bold"), 
                                          bg="#ffffff")
            self.resumen_label.pack(pady=10)

            self.confirmar_compra_btn = tk.Button(self.paso4_frame, text="Confirmar Compra", command=self.confirmar_compra, 
                                                  bg="#ff5733", fg="white", font=("Arial", 12, "bold"), relief="flat", 
                                                  padx=5, pady=5)
            self.confirmar_compra_btn.pack(pady=10)

            self.detalles_pedido = tk.Label(self.paso4_frame, font=("Arial", 12), bg="#ffffff")
            self.detalles_pedido.pack(pady=10)

        def open_modal(self):
            self.modal_frame.deiconify()

        def toggle_seat(self, btn):
            seat_id = btn.cget("text")
            if seat_id in self.asientos_seleccionados:
                self.asientos_seleccionados.remove(seat_id)
                btn.config(bg="#555")
            else:
                self.asientos_seleccionados.append(seat_id)
                btn.config(bg="red")

            # Actualiza la información de asientos ocupados y disponibles
            ocupados = len(self.asientos_seleccionados)
            disponibles = 56 - ocupados  # Total de asientos: 56
            self.asientos_info_label.config(text=f"Asientos ocupados: {ocupados}\nAsientos disponibles: {disponibles}")

        def show_asientos(self):
            self.paso1_frame.pack_forget()  # Oculta paso 1
            self.paso2_frame.pack(pady=15)  # Muestra paso 2

        def show_comida(self):
            self.paso2_frame.pack_forget()  # Oculta paso 2
            self.paso3_frame.pack(pady=15)  # Muestra paso 3

        def show_resumen(self):
            self.paso3_frame.pack_forget()  # Oculta paso 3
            self.paso4_frame.pack(pady=15)  # Muestra paso 
            
            # Mostrar los detalles del resumen
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"
            self.detalles_pedido.config(text=resumen)

        def descargar_comprobante(self):
            # Crear el contenido del comprobante
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"

            # Asegúrate de asignar las variables necesarias
            dia_var = self.dia_var.get()
            horario = self.horario_var.get()
            asientos_seleccionados = asientos_texto
            email = "Losclasicosdelayer"    # Suponiendo que tienes un campo 'email_var' en la clase

            contenidoHTML = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: 'Helvetica Neue', Arial, sans-serif;
                        background-color: #f0f2f5;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        width: 70%;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ff6b6b;
                        font-size: 28px;
                        margin-bottom: 10px;
                    }}
                    h2 {{
                        color: #333;
                        font-size: 22px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        line-height: 1.6;
                        font-size: 16px;
                        color: #555;
                    }}
                    .details, .contact-info {{
                        margin-bottom: 30px;
                    }}
                    .details p, .contact-info p {{
                        margin: 8px 0;
                    }}
                    .details label, .contact-info label {{
                        font-weight: bold;
                        color: #333;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 12px 20px;
                        font-size: 16px;
                        color: #fff;
                        background-color: #ff6b6b;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        text-decoration: none;
                        transition: background-color 0.3s ease;
                    }}
                    .btn:hover {{
                        background-color: #ff4a4a;
                    }}
                    .note {{
                        font-style: italic;
                        color: #888;
                        margin-top: 20px;
                        font-size: 14px;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 40px;
                        color: #999;
                        font-size: 14px;
                    }}
                </style>
                <title>Confirmación de Compra - Cine</title>
            </head>
            <body>
                <div class="container">
                    <h1>¡Compra Confirmada!</h1>
                    <p>Gracias por tu compra en nuestro cine! A continuación, te mostramos los detalles de tu reserva.</p>

                    <div class="details">
                        <h2>Detalles de la Película</h2>
                        <p><strong>Película:</strong>Robot Salvaje</p>
                        <p><strong>Fecha:</strong> {dia_var}</p>
                        <p><strong>Hora:</strong> {horario}</p>
                        <p><strong>Asientos seleccionados:</strong> {asientos_seleccionados}</p>
                    </div>

                    <div class="contact-info">
                        <h2>Información de Contacto</h2>
                        <p><strong>Telefono:</strong>11 4870 7273</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p class="note">*Si tiene alguna consulta no dude en contactarnos</p>
                    </div>

                    <p class="note">*Por favor, presenta este comprobante en la entrada del cine. ¡Disfruta la película!</p>
                </div>

                <div class="footer">
                    <p>&copy; 2024 CinePlus. Todos los derechos reservados.</p>
                </div>
            </body>
            </html>
            """

            # Crear un archivo HTML con el contenido
            file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads',f"entrada.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(contenidoHTML)

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Comprobante generado", f"Comprobante guardado en: {file_path}")

        def confirmar_compra(self):
            # Botón para descargar el comprobante
            self.btn_descargar_comprobante = tk.Button(self.paso4_frame, text="Descargar Comprobante", 
                                                       command=self.descargar_comprobante, bg="#42a5f5", fg="white", 
                                                       font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.btn_descargar_comprobante.pack(pady=10)

    
    app = CinemaApp(peli2_window)  # Asegúrate de pasar peli1_window, no root
    peli2_window.mainloop()  # Asegúrate de que mainloop esté en la ventana emergente


def open_peli3(root):
    root.withdraw()
    peli3_window = tk.Toplevel(root)
    peli3_window.title("Cine Retro - El padrino")
    peli3_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    peli3_window.configure(bg="#d3d3d3")

    class CinemaApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Cine Retro - Película 1")

            # Sección de encabezado
            self.header_frame = tk.Frame(self.root, bg="#333333")
            self.header_frame.pack(fill=tk.X)

            # Logo y botón de "Volver"
            self.logo_image = tk.PhotoImage(file="imagenes/logo2.png")
            self.logo = tk.Label(self.header_frame, image=self.logo_image, bg="#333333")
            self.logo.pack(side=tk.LEFT, padx=20)

            self.btn_volver = tk.Button(
                self.header_frame, text="Volver", command=self.volver,
                bg="#ff5733", fg="white", font=("Arial", 12, "bold"), borderwidth=4, relief="raised"
            )
            self.btn_volver.pack(side=tk.RIGHT, padx=20)

            # Cuadro de la película con borde
            self.pelicula_frame = tk.Frame(self.root, bg="#ffffff", padx=15, pady=15, borderwidth=15, relief="ridge")
            self.pelicula_frame.pack(padx=20, pady=20)

            # Título de la película
            self.pelicula_titulo = tk.Label(self.pelicula_frame, text="Venom el ultimo baile", font=("Arial", 22, "bold"), fg="#ff5733", bg="#ffffff")
            self.pelicula_titulo.pack(pady=(10, 5))

            # Imagen de la película
            imagen_peli = Image.open("peliculas/venom el ultimo baile.png")
            imagen_peli = imagen_peli.resize((400, 400))
            self.imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)
            self.imagen_label = tk.Label(self.pelicula_frame, image=self.imagen_peli_tk, bg="#ffffff")
            self.imagen_label.pack(side=tk.LEFT, padx=10, pady=10)

            # Información de la película y calificación
            self.info_frame = tk.Frame(self.pelicula_frame, bg="#ffffff")
            self.info_frame.pack(side=tk.LEFT, padx=20, pady=10)

            self.genero_label = tk.Label(self.info_frame, text="Género: Acción", font=("Arial", 14), bg="#ffffff")
            self.genero_label.pack(anchor="w", pady=5)

            self.director_label = tk.Label(self.info_frame, text="Idiomas:Español, Ingles Subtitulada", font=("Arial", 14), bg="#ffffff")
            self.director_label.pack(anchor="w", pady=5)

            self.protagonistas_label = tk.Label(self.info_frame, text="clasificacion: Mayores de +13 ", font=("Arial", 14), bg="#ffffff")
            self.protagonistas_label.pack(anchor="w", pady=5)

            # Calificación con estrellas
            self.calificacion_label = tk.Label(self.info_frame, text="Calificación: ⭐⭐⭐⭐", font=("Arial", 14), bg="#ffffff")
            self.calificacion_label.pack(anchor="w", pady=5)

            # Botón para comprar entradas
            self.btn_comprar = tk.Button(self.info_frame, text="Comprar Entradas", command=self.open_modal, bg="#ff5733", fg="white", font=("Arial", 16))
            self.btn_comprar.pack(pady=(20, 0))

            # Modal (ventana emergente)
            self.modal_frame = None
            self.setup_modal()

        def volver(self):
            self.root.destroy()  # Cierra la ventana de Película 1
            root.deiconify()  # Reabre la ventana principal

        def setup_modal(self):
            # Configuración del modal (ventana emergente)
            self.modal_frame = tk.Toplevel(self.root)
            self.modal_frame.title("Reserva de Entradas")
            self.modal_frame.geometry("500x600")
            self.modal_frame.config(bg="#f5f5f5")  # Fondo claro
            self.modal_frame.withdraw()  # Ocultar el modal inicialmente

            # Paso 1: Selección de horario y día
            self.paso1_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.paso1_frame.pack(pady=15)

            tk.Label(self.paso1_frame, text="Seleccione el horario y el día", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Opciones para horarios
            tk.Label(self.paso1_frame, text="Horario:", bg="#ffffff").pack()
            horarios = ["15:00", "18:00", "21:00"]
            self.horario_var = tk.StringVar(value=horarios[0])
            tk.OptionMenu(self.paso1_frame, self.horario_var, *horarios).pack(pady=5)

            # Opciones para días
            tk.Label(self.paso1_frame, text="Día:", bg="#ffffff").pack()
            dias = ["10/10/2024", "11/10/2024", "12/10/2024"]
            self.dia_var = tk.StringVar(value=dias[0])
            tk.OptionMenu(self.paso1_frame, self.dia_var, *dias).pack(pady=5)

            self.siguiente_btn = tk.Button(self.paso1_frame, text="Siguiente", command=self.show_asientos, 
                                           bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                           relief="flat", padx=5, pady=5)
            self.siguiente_btn.pack(pady=10)

            # Paso 2: Selección de asientos
            self.paso2_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso2_frame, text="Elija sus asientos", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Label para mostrar la cantidad de asientos ocupados y disponibles
            self.asientos_info_label = tk.Label(self.paso2_frame, text="Asientos ocupados: 0\nAsientos disponibles: 56", 
                                                font=("Arial", 12), bg="#ffffff")
            self.asientos_info_label.pack(pady=10)

            self.seating_grid = tk.Frame(self.paso2_frame, bg="#ffffff")
            self.seating_grid.pack(pady=10)

            self.asientos_seleccionados = []
            filas, columnas = 7, 8
            letras = 'ABCDEFG'

            self.seats = {}
            for i in range(filas):
                for j in range(columnas):
                    seat_id = f"{letras[i]}{j+1}"  # A1, A2, etc.
                    btn = tk.Button(self.seating_grid, text=seat_id, width=4, height=2, 
                                    bg="#555", fg="#fff", relief="flat", font=("Arial", 10))
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    btn.config(command=lambda b=btn: self.toggle_seat(b))
                    self.seats[seat_id] = btn

            self.confirmar_asientos_btn = tk.Button(self.paso2_frame, text="Confirmar Asientos", 
                                                    command=self.show_comida, bg="#ff8c42", fg="white", 
                                                    font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.confirmar_asientos_btn.pack(pady=10)

            # Paso 3: Selección de comida
            self.paso3_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso3_frame, text="Elija su comida", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            self.comida_var = tk.StringVar(value="Combo 1")
            self.combos = {
                "Combo 1": "Palomitas + Bebida",
                "Combo 2": "Nachos + Refresco",
                "Combo 3": "Hot Dog + Bebida",
                "Sanchez": "Palomitas 2x1",
                "No gracias": "Ninguna"
            }

            for combo, descripcion in self.combos.items():
                tk.Radiobutton(self.paso3_frame, text=f"{combo}: {descripcion}", variable=self.comida_var, 
                               value=combo, bg="#ffffff", font=("Arial", 12)).pack(anchor="w")

            self.siguiente_comida_btn = tk.Button(self.paso3_frame, text="Siguiente", command=self.show_resumen, 
                                                  bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                                  relief="flat", padx=5, pady=5)
            self.siguiente_comida_btn.pack(pady=10)

            # Paso 4: Resumen del pedido
            self.paso4_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.resumen_label = tk.Label(self.paso4_frame, text="Resumen de la compra", font=("Arial", 16, "bold"), 
                                          bg="#ffffff")
            self.resumen_label.pack(pady=10)

            self.confirmar_compra_btn = tk.Button(self.paso4_frame, text="Confirmar Compra", command=self.confirmar_compra, 
                                                  bg="#ff5733", fg="white", font=("Arial", 12, "bold"), relief="flat", 
                                                  padx=5, pady=5)
            self.confirmar_compra_btn.pack(pady=10)

            self.detalles_pedido = tk.Label(self.paso4_frame, font=("Arial", 12), bg="#ffffff")
            self.detalles_pedido.pack(pady=10)

        def open_modal(self):
            self.modal_frame.deiconify()

        def toggle_seat(self, btn):
            seat_id = btn.cget("text")
            if seat_id in self.asientos_seleccionados:
                self.asientos_seleccionados.remove(seat_id)
                btn.config(bg="#555")
            else:
                self.asientos_seleccionados.append(seat_id)
                btn.config(bg="red")

            # Actualiza la información de asientos ocupados y disponibles
            ocupados = len(self.asientos_seleccionados)
            disponibles = 56 - ocupados  # Total de asientos: 56
            self.asientos_info_label.config(text=f"Asientos ocupados: {ocupados}\nAsientos disponibles: {disponibles}")

        def show_asientos(self):
            self.paso1_frame.pack_forget()  # Oculta paso 1
            self.paso2_frame.pack(pady=15)  # Muestra paso 2

        def show_comida(self):
            self.paso2_frame.pack_forget()  # Oculta paso 2
            self.paso3_frame.pack(pady=15)  # Muestra paso 3

        def show_resumen(self):
            self.paso3_frame.pack_forget()  # Oculta paso 3
            self.paso4_frame.pack(pady=15)  # Muestra paso 
            
            # Mostrar los detalles del resumen
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"
            self.detalles_pedido.config(text=resumen)

        def descargar_comprobante(self):
            # Crear el contenido del comprobante
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"

            # Asegúrate de asignar las variables necesarias
            dia_var = self.dia_var.get()
            horario = self.horario_var.get()
            asientos_seleccionados = asientos_texto
            email = "Losclasicosdelayer"    # Suponiendo que tienes un campo 'email_var' en la clase

            contenidoHTML = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: 'Helvetica Neue', Arial, sans-serif;
                        background-color: #f0f2f5;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        width: 70%;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ff6b6b;
                        font-size: 28px;
                        margin-bottom: 10px;
                    }}
                    h2 {{
                        color: #333;
                        font-size: 22px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        line-height: 1.6;
                        font-size: 16px;
                        color: #555;
                    }}
                    .details, .contact-info {{
                        margin-bottom: 30px;
                    }}
                    .details p, .contact-info p {{
                        margin: 8px 0;
                    }}
                    .details label, .contact-info label {{
                        font-weight: bold;
                        color: #333;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 12px 20px;
                        font-size: 16px;
                        color: #fff;
                        background-color: #ff6b6b;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        text-decoration: none;
                        transition: background-color 0.3s ease;
                    }}
                    .btn:hover {{
                        background-color: #ff4a4a;
                    }}
                    .note {{
                        font-style: italic;
                        color: #888;
                        margin-top: 20px;
                        font-size: 14px;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 40px;
                        color: #999;
                        font-size: 14px;
                    }}
                </style>
                <title>Confirmación de Compra - Cine</title>
            </head>
            <body>
                <div class="container">
                    <h1>¡Compra Confirmada!</h1>
                    <p>Gracias por tu compra en nuestro cine! A continuación, te mostramos los detalles de tu reserva.</p>

                    <div class="details">
                        <h2>Detalles de la Película</h2>
                        <p><strong>Película:</strong>Venom el ultimo baile</p>
                        <p><strong>Fecha:</strong> {dia_var}</p>
                        <p><strong>Hora:</strong> {horario}</p>
                        <p><strong>Asientos seleccionados:</strong> {asientos_seleccionados}</p>
                    </div>

                    <div class="contact-info">
                        <h2>Información de Contacto</h2>
                        <p><strong>Telefono:</strong>11 4870 7273</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p class="note">*Si tiene alguna consulta no dude en contactarnos</p>
                    </div>

                    <p class="note">*Por favor, presenta este comprobante en la entrada del cine. ¡Disfruta la película!</p>
                </div>

                <div class="footer">
                    <p>&copy; 2024 CinePlus. Todos los derechos reservados.</p>
                </div>
            </body>
            </html>
            """

            # Crear un archivo HTML con el contenido
            file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads',f"entrada.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(contenidoHTML)

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Comprobante generado", f"Comprobante guardado en: {file_path}")

        def confirmar_compra(self):
            
            # Botón para descargar el comprobante
            self.btn_descargar_comprobante = tk.Button(self.paso4_frame, text="Descargar Comprobante", 
                                                       command=self.descargar_comprobante, bg="#42a5f5", fg="white", 
                                                       font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.btn_descargar_comprobante.pack(pady=10)

    
    app = CinemaApp(peli3_window)  # Asegúrate de pasar peli1_window, no root
    peli3_window.mainloop()  # Asegúrate de que mainloop esté en la ventana emergente


def open_peli4(root):
    root.withdraw()
    peli4_window = tk.Toplevel(root)
    peli4_window.title("Cine Retro - El padrino")
    peli4_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    peli4_window.configure(bg="#d3d3d3")

    class CinemaApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Cine Retro - Película 1")

            # Sección de encabezado
            self.header_frame = tk.Frame(self.root, bg="#333333")
            self.header_frame.pack(fill=tk.X)

            # Logo y botón de "Volver"
            self.logo_image = tk.PhotoImage(file="imagenes/logo2.png")
            self.logo = tk.Label(self.header_frame, image=self.logo_image, bg="#333333")
            self.logo.pack(side=tk.LEFT, padx=20)

            self.btn_volver = tk.Button(
                self.header_frame, text="Volver", command=self.volver,
                bg="#ff5733", fg="white", font=("Arial", 12, "bold"), borderwidth=4, relief="raised"
            )
            self.btn_volver.pack(side=tk.RIGHT, padx=20)

            # Cuadro de la película con borde
            self.pelicula_frame = tk.Frame(self.root, bg="#ffffff", padx=15, pady=15, borderwidth=15, relief="ridge")
            self.pelicula_frame.pack(padx=20, pady=20)

            # Título de la película
            self.pelicula_titulo = tk.Label(self.pelicula_frame, text="Sonrie 2", font=("Arial", 22, "bold"), fg="#ff5733", bg="#ffffff")
            self.pelicula_titulo.pack(pady=(10, 5))

            # Imagen de la película
            imagen_peli = Image.open("peliculas/Sonrie 2.png")
            imagen_peli = imagen_peli.resize((400, 400))
            self.imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)
            self.imagen_label = tk.Label(self.pelicula_frame, image=self.imagen_peli_tk, bg="#ffffff")
            self.imagen_label.pack(side=tk.LEFT, padx=10, pady=10)

            # Información de la película y calificación
            self.info_frame = tk.Frame(self.pelicula_frame, bg="#ffffff")
            self.info_frame.pack(side=tk.LEFT, padx=20, pady=10)

            self.genero_label = tk.Label(self.info_frame, text="Género: Terror", font=("Arial", 14), bg="#ffffff")
            self.genero_label.pack(anchor="w", pady=5)

            self.director_label = tk.Label(self.info_frame, text="Idiomas:Español, Ingles Subtitulada", font=("Arial", 14), bg="#ffffff")
            self.director_label.pack(anchor="w", pady=5)

            self.protagonistas_label = tk.Label(self.info_frame, text="clasificacion: Para mayores de +16 ", font=("Arial", 14), bg="#ffffff")
            self.protagonistas_label.pack(anchor="w", pady=5)

            # Calificación con estrellas
            self.calificacion_label = tk.Label(self.info_frame, text="Calificación: ⭐⭐⭐⭐⭐", font=("Arial", 14), bg="#ffffff")
            self.calificacion_label.pack(anchor="w", pady=5)

            # Botón para comprar entradas
            self.btn_comprar = tk.Button(self.info_frame, text="Comprar Entradas", command=self.open_modal, bg="#ff5733", fg="white", font=("Arial", 16))
            self.btn_comprar.pack(pady=(20, 0))

            # Modal (ventana emergente)
            self.modal_frame = None
            self.setup_modal()

        def volver(self):
            self.root.destroy()  # Cierra la ventana de Película 1
            root.deiconify()  # Reabre la ventana principal

        def setup_modal(self):
            # Configuración del modal (ventana emergente)
            self.modal_frame = tk.Toplevel(self.root)
            self.modal_frame.title("Reserva de Entradas")
            self.modal_frame.geometry("500x600")
            self.modal_frame.config(bg="#f5f5f5")  # Fondo claro
            self.modal_frame.withdraw()  # Ocultar el modal inicialmente

            # Paso 1: Selección de horario y día
            self.paso1_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.paso1_frame.pack(pady=15)

            tk.Label(self.paso1_frame, text="Seleccione el horario y el día", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Opciones para horarios
            tk.Label(self.paso1_frame, text="Horario:", bg="#ffffff").pack()
            horarios = ["15:00", "18:00", "21:00"]
            self.horario_var = tk.StringVar(value=horarios[0])
            tk.OptionMenu(self.paso1_frame, self.horario_var, *horarios).pack(pady=5)

            # Opciones para días
            tk.Label(self.paso1_frame, text="Día:", bg="#ffffff").pack()
            dias = ["10/10/2024", "11/10/2024", "12/10/2024"]
            self.dia_var = tk.StringVar(value=dias[0])
            tk.OptionMenu(self.paso1_frame, self.dia_var, *dias).pack(pady=5)

            self.siguiente_btn = tk.Button(self.paso1_frame, text="Siguiente", command=self.show_asientos, 
                                           bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                           relief="flat", padx=5, pady=5)
            self.siguiente_btn.pack(pady=10)

            # Paso 2: Selección de asientos
            self.paso2_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso2_frame, text="Elija sus asientos", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Label para mostrar la cantidad de asientos ocupados y disponibles
            self.asientos_info_label = tk.Label(self.paso2_frame, text="Asientos ocupados: 0\nAsientos disponibles: 56", 
                                                font=("Arial", 12), bg="#ffffff")
            self.asientos_info_label.pack(pady=10)

            self.seating_grid = tk.Frame(self.paso2_frame, bg="#ffffff")
            self.seating_grid.pack(pady=10)

            self.asientos_seleccionados = []
            filas, columnas = 7, 8
            letras = 'ABCDEFG'

            self.seats = {}
            for i in range(filas):
                for j in range(columnas):
                    seat_id = f"{letras[i]}{j+1}"  # A1, A2, etc.
                    btn = tk.Button(self.seating_grid, text=seat_id, width=4, height=2, 
                                    bg="#555", fg="#fff", relief="flat", font=("Arial", 10))
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    btn.config(command=lambda b=btn: self.toggle_seat(b))
                    self.seats[seat_id] = btn

            self.confirmar_asientos_btn = tk.Button(self.paso2_frame, text="Confirmar Asientos", 
                                                    command=self.show_comida, bg="#ff8c42", fg="white", 
                                                    font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.confirmar_asientos_btn.pack(pady=10)

            # Paso 3: Selección de comida
            self.paso3_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso3_frame, text="Elija su comida", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            self.comida_var = tk.StringVar(value="Combo 1")
            self.combos = {
                "Combo 1": "Palomitas + Bebida",
                "Combo 2": "Nachos + Refresco",
                "Combo 3": "Hot Dog + Bebida",
                "Sanchez": "Palomitas 2x1",
                "No gracias": "Ninguna"
            }

            for combo, descripcion in self.combos.items():
                tk.Radiobutton(self.paso3_frame, text=f"{combo}: {descripcion}", variable=self.comida_var, 
                               value=combo, bg="#ffffff", font=("Arial", 12)).pack(anchor="w")

            self.siguiente_comida_btn = tk.Button(self.paso3_frame, text="Siguiente", command=self.show_resumen, 
                                                  bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                                  relief="flat", padx=5, pady=5)
            self.siguiente_comida_btn.pack(pady=10)

            # Paso 4: Resumen del pedido
            self.paso4_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.resumen_label = tk.Label(self.paso4_frame, text="Resumen de la compra", font=("Arial", 16, "bold"), 
                                          bg="#ffffff")
            self.resumen_label.pack(pady=10)

            self.confirmar_compra_btn = tk.Button(self.paso4_frame, text="Confirmar Compra", command=self.confirmar_compra, 
                                                  bg="#ff5733", fg="white", font=("Arial", 12, "bold"), relief="flat", 
                                                  padx=5, pady=5)
            self.confirmar_compra_btn.pack(pady=10)

            self.detalles_pedido = tk.Label(self.paso4_frame, font=("Arial", 12), bg="#ffffff")
            self.detalles_pedido.pack(pady=10)

        def open_modal(self):
            self.modal_frame.deiconify()

        def toggle_seat(self, btn):
            seat_id = btn.cget("text")
            if seat_id in self.asientos_seleccionados:
                self.asientos_seleccionados.remove(seat_id)
                btn.config(bg="#555")
            else:
                self.asientos_seleccionados.append(seat_id)
                btn.config(bg="red")

            # Actualiza la información de asientos ocupados y disponibles
            ocupados = len(self.asientos_seleccionados)
            disponibles = 56 - ocupados  # Total de asientos: 56
            self.asientos_info_label.config(text=f"Asientos ocupados: {ocupados}\nAsientos disponibles: {disponibles}")

        def show_asientos(self):
            self.paso1_frame.pack_forget()  # Oculta paso 1
            self.paso2_frame.pack(pady=15)  # Muestra paso 2

        def show_comida(self):
            self.paso2_frame.pack_forget()  # Oculta paso 2
            self.paso3_frame.pack(pady=15)  # Muestra paso 3

        def show_resumen(self):
            self.paso3_frame.pack_forget()  # Oculta paso 3
            self.paso4_frame.pack(pady=15)  # Muestra paso 
            
            # Mostrar los detalles del resumen
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"
            self.detalles_pedido.config(text=resumen)

        def descargar_comprobante(self):
            # Crear el contenido del comprobante
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"

            # Asegúrate de asignar las variables necesarias
            dia_var = self.dia_var.get()
            horario = self.horario_var.get()
            asientos_seleccionados = asientos_texto
            email = "Losclasicosdelayer"    # Suponiendo que tienes un campo 'email_var' en la clase

            contenidoHTML = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: 'Helvetica Neue', Arial, sans-serif;
                        background-color: #f0f2f5;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        width: 70%;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ff6b6b;
                        font-size: 28px;
                        margin-bottom: 10px;
                    }}
                    h2 {{
                        color: #333;
                        font-size: 22px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        line-height: 1.6;
                        font-size: 16px;
                        color: #555;
                    }}
                    .details, .contact-info {{
                        margin-bottom: 30px;
                    }}
                    .details p, .contact-info p {{
                        margin: 8px 0;
                    }}
                    .details label, .contact-info label {{
                        font-weight: bold;
                        color: #333;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 12px 20px;
                        font-size: 16px;
                        color: #fff;
                        background-color: #ff6b6b;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        text-decoration: none;
                        transition: background-color 0.3s ease;
                    }}
                    .btn:hover {{
                        background-color: #ff4a4a;
                    }}
                    .note {{
                        font-style: italic;
                        color: #888;
                        margin-top: 20px;
                        font-size: 14px;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 40px;
                        color: #999;
                        font-size: 14px;
                    }}
                </style>
                <title>Confirmación de Compra - Cine</title>
            </head>
            <body>
                <div class="container">
                    <h1>¡Compra Confirmada!</h1>
                    <p>Gracias por tu compra en nuestro cine! A continuación, te mostramos los detalles de tu reserva.</p>

                    <div class="details">
                        <h2>Detalles de la Película</h2>
                        <p><strong>Película:</strong>Sonrie 2</p>
                        <p><strong>Fecha:</strong> {dia_var}</p>
                        <p><strong>Hora:</strong> {horario}</p>
                        <p><strong>Asientos seleccionados:</strong> {asientos_seleccionados}</p>
                    </div>

                    <div class="contact-info">
                        <h2>Información de Contacto</h2>
                        <p><strong>Telefono:</strong>11 4870 7273</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p class="note">*Si tiene alguna consulta no dude en contactarnos</p>
                    </div>

                    <p class="note">*Por favor, presenta este comprobante en la entrada del cine. ¡Disfruta la película!</p>
                </div>

                <div class="footer">
                    <p>&copy; 2024 CinePlus. Todos los derechos reservados.</p>
                </div>
            </body>
            </html>
            """

            # Crear un archivo HTML con el contenido
            file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads',f"entrada.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(contenidoHTML)

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Comprobante generado", f"Comprobante guardado en: {file_path}")

        def confirmar_compra(self):
            
            # Botón para descargar el comprobante
            self.btn_descargar_comprobante = tk.Button(self.paso4_frame, text="Descargar Comprobante", 
                                                       command=self.descargar_comprobante, bg="#42a5f5", fg="white", 
                                                       font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.btn_descargar_comprobante.pack(pady=10)

    
    app = CinemaApp(peli4_window)  # Asegúrate de pasar peli1_window, no root
    peli4_window.mainloop()  # Asegúrate de que mainloop esté en la ventana emergente


def open_peli5(root):
    root.withdraw()
    peli5_window = tk.Toplevel(root)
    peli5_window.title("Cine Retro - El padrino")
    peli5_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    peli5_window.configure(bg="#d3d3d3")

    class CinemaApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Cine Retro - Película 1")

            # Sección de encabezado
            self.header_frame = tk.Frame(self.root, bg="#333333")
            self.header_frame.pack(fill=tk.X)

            # Logo y botón de "Volver"
            self.logo_image = tk.PhotoImage(file="imagenes/logo2.png")
            self.logo = tk.Label(self.header_frame, image=self.logo_image, bg="#333333")
            self.logo.pack(side=tk.LEFT, padx=20)

            self.btn_volver = tk.Button(
                self.header_frame, text="Volver", command=self.volver,
                bg="#ff5733", fg="white", font=("Arial", 12, "bold"), borderwidth=4, relief="raised"
            )
            self.btn_volver.pack(side=tk.RIGHT, padx=20)

            # Cuadro de la película con borde
            self.pelicula_frame = tk.Frame(self.root, bg="#ffffff", padx=15, pady=15, borderwidth=15, relief="ridge")
            self.pelicula_frame.pack(padx=20, pady=20)

            # Título de la película
            self.pelicula_titulo = tk.Label(self.pelicula_frame, text="Coraline y la puerta secreta", font=("Arial", 22, "bold"), fg="#ff5733", bg="#ffffff")
            self.pelicula_titulo.pack(pady=(10, 5))

            # Imagen de la película
            imagen_peli = Image.open("peliculas/coraline2.png")
            imagen_peli = imagen_peli.resize((400, 400))
            self.imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)
            self.imagen_label = tk.Label(self.pelicula_frame, image=self.imagen_peli_tk, bg="#ffffff")
            self.imagen_label.pack(side=tk.LEFT, padx=10, pady=10)

            # Información de la película y calificación
            # Información de la película y calificación
            self.info_frame = tk.Frame(self.pelicula_frame, bg="#ffffff")
            self.info_frame.pack(side=tk.LEFT, padx=20, pady=10)

            self.genero_label = tk.Label(self.info_frame, text="Género: Terror", font=("Arial", 14), bg="#ffffff")
            self.genero_label.pack(anchor="w", pady=5)

            self.director_label = tk.Label(self.info_frame, text="Idiomas:español, ingles y subtitulada", font=("Arial", 14), bg="#ffffff")
            self.director_label.pack(anchor="w", pady=5)

            self.protagonistas_label = tk.Label(self.info_frame, text="clasificacion: PG (control parental)", font=("Arial", 14), bg="#ffffff")
            self.protagonistas_label.pack(anchor="w", pady=5)

            # Calificación con estrellas
            self.calificacion_label = tk.Label(self.info_frame, text="Calificación: ⭐⭐⭐", font=("Arial", 14), bg="#ffffff")
            self.calificacion_label.pack(anchor="w", pady=5)

            # Botón para comprar entradas
            self.btn_comprar = tk.Button(self.info_frame, text="Comprar Entradas", command=self.open_modal, bg="#ff5733", fg="white", font=("Arial", 16))
            self.btn_comprar.pack(pady=(20, 0))

            # Modal (ventana emergente)
            self.modal_frame = None
            self.setup_modal()

        def volver(self):
            self.root.destroy()  # Cierra la ventana de Película 1
            root.deiconify()  # Reabre la ventana principal

        def setup_modal(self):
            # Configuración del modal (ventana emergente)
            self.modal_frame = tk.Toplevel(self.root)
            self.modal_frame.title("Reserva de Entradas")
            self.modal_frame.geometry("500x600")
            self.modal_frame.config(bg="#f5f5f5")  # Fondo claro
            self.modal_frame.withdraw()  # Ocultar el modal inicialmente

            # Paso 1: Selección de horario y día
            self.paso1_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.paso1_frame.pack(pady=15)

            tk.Label(self.paso1_frame, text="Seleccione el horario y el día", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Opciones para horarios
            tk.Label(self.paso1_frame, text="Horario:", bg="#ffffff").pack()
            horarios = ["15:00", "18:00", "21:00"]
            self.horario_var = tk.StringVar(value=horarios[0])
            tk.OptionMenu(self.paso1_frame, self.horario_var, *horarios).pack(pady=5)

            # Opciones para días
            tk.Label(self.paso1_frame, text="Día:", bg="#ffffff").pack()
            dias = ["10/10/2024", "11/10/2024", "12/10/2024"]
            self.dia_var = tk.StringVar(value=dias[0])
            tk.OptionMenu(self.paso1_frame, self.dia_var, *dias).pack(pady=5)

            self.siguiente_btn = tk.Button(self.paso1_frame, text="Siguiente", command=self.show_asientos, 
                                           bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                           relief="flat", padx=5, pady=5)
            self.siguiente_btn.pack(pady=10)

            # Paso 2: Selección de asientos
            self.paso2_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso2_frame, text="Elija sus asientos", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            # Label para mostrar la cantidad de asientos ocupados y disponibles
            self.asientos_info_label = tk.Label(self.paso2_frame, text="Asientos ocupados: 0\nAsientos disponibles: 56", 
                                                font=("Arial", 12), bg="#ffffff")
            self.asientos_info_label.pack(pady=10)

            self.seating_grid = tk.Frame(self.paso2_frame, bg="#ffffff")
            self.seating_grid.pack(pady=10)

            self.asientos_seleccionados = []
            filas, columnas = 7, 8
            letras = 'ABCDEFG'

            self.seats = {}
            for i in range(filas):
                for j in range(columnas):
                    seat_id = f"{letras[i]}{j+1}"  # A1, A2, etc.
                    btn = tk.Button(self.seating_grid, text=seat_id, width=4, height=2, 
                                    bg="#555", fg="#fff", relief="flat", font=("Arial", 10))
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    btn.config(command=lambda b=btn: self.toggle_seat(b))
                    self.seats[seat_id] = btn

            self.confirmar_asientos_btn = tk.Button(self.paso2_frame, text="Confirmar Asientos", 
                                                    command=self.show_comida, bg="#ff8c42", fg="white", 
                                                    font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.confirmar_asientos_btn.pack(pady=10)

            # Paso 3: Selección de comida
            self.paso3_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            tk.Label(self.paso3_frame, text="Elija su comida", font=("Arial", 16, "bold"), bg="#ffffff").pack()

            self.comida_var = tk.StringVar(value="Combo 1")
            self.combos = {
                "Combo 1": "Palomitas + Bebida",
                "Combo 2": "Nachos + Refresco",
                "Combo 3": "Hot Dog + Bebida",
                "Sanchez": "Palomitas 2x1",
                "No gracias": "Ninguna"
            }

            for combo, descripcion in self.combos.items():
                tk.Radiobutton(self.paso3_frame, text=f"{combo}: {descripcion}", variable=self.comida_var, 
                               value=combo, bg="#ffffff", font=("Arial", 12)).pack(anchor="w")

            self.siguiente_comida_btn = tk.Button(self.paso3_frame, text="Siguiente", command=self.show_resumen, 
                                                  bg="#ff8c42", fg="white", font=("Arial", 12, "bold"), 
                                                  relief="flat", padx=5, pady=5)
            self.siguiente_comida_btn.pack(pady=10)

            # Paso 4: Resumen del pedido
            self.paso4_frame = tk.Frame(self.modal_frame, bg="#ffffff", bd=2, relief="solid", padx=10, pady=10)
            self.resumen_label = tk.Label(self.paso4_frame, text="Resumen de la compra", font=("Arial", 16, "bold"), 
                                          bg="#ffffff")
            self.resumen_label.pack(pady=10)

            self.confirmar_compra_btn = tk.Button(self.paso4_frame, text="Confirmar Compra", command=self.confirmar_compra, 
                                                  bg="#ff5733", fg="white", font=("Arial", 12, "bold"), relief="flat", 
                                                  padx=5, pady=5)
            self.confirmar_compra_btn.pack(pady=10)

            self.detalles_pedido = tk.Label(self.paso4_frame, font=("Arial", 12), bg="#ffffff")
            self.detalles_pedido.pack(pady=10)

        def open_modal(self):
            self.modal_frame.deiconify()

        def toggle_seat(self, btn):
            seat_id = btn.cget("text")
            if seat_id in self.asientos_seleccionados:
                self.asientos_seleccionados.remove(seat_id)
                btn.config(bg="#555")
            else:
                self.asientos_seleccionados.append(seat_id)
                btn.config(bg="red")

            # Actualiza la información de asientos ocupados y disponibles
            ocupados = len(self.asientos_seleccionados)
            disponibles = 56 - ocupados  # Total de asientos: 56
            self.asientos_info_label.config(text=f"Asientos ocupados: {ocupados}\nAsientos disponibles: {disponibles}")

        def show_asientos(self):
            self.paso1_frame.pack_forget()  # Oculta paso 1
            self.paso2_frame.pack(pady=15)  # Muestra paso 2

        def show_comida(self):
            self.paso2_frame.pack_forget()  # Oculta paso 2
            self.paso3_frame.pack(pady=15)  # Muestra paso 3

        def show_resumen(self):
            self.paso3_frame.pack_forget()  # Oculta paso 3
            self.paso4_frame.pack(pady=15)  # Muestra paso 
            
            # Mostrar los detalles del resumen
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"
            self.detalles_pedido.config(text=resumen)

        def descargar_comprobante(self):
            # Crear el contenido del comprobante
            asientos_texto = ", ".join(self.asientos_seleccionados)
            resumen_texto = f"Día: {self.dia_var.get()}\nHorario: {self.horario_var.get()}\n"
            comida = self.comida_var.get()
            resumen = f"{resumen_texto}Asientos seleccionados: {asientos_texto}\nComida: {self.combos[comida]}"

            # Asegúrate de asignar las variables necesarias
            dia_var = self.dia_var.get()
            horario = self.horario_var.get()
            asientos_seleccionados = asientos_texto
            email = "Losclasicosdelayer"    # Suponiendo que tienes un campo 'email_var' en la clase

            contenidoHTML = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: 'Helvetica Neue', Arial, sans-serif;
                        background-color: #f0f2f5;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        width: 70%;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ff6b6b;
                        font-size: 28px;
                        margin-bottom: 10px;
                    }}
                    h2 {{
                        color: #333;
                        font-size: 22px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        line-height: 1.6;
                        font-size: 16px;
                        color: #555;
                    }}
                    .details, .contact-info {{
                        margin-bottom: 30px;
                    }}
                    .details p, .contact-info p {{
                        margin: 8px 0;
                    }}
                    .details label, .contact-info label {{
                        font-weight: bold;
                        color: #333;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 12px 20px;
                        font-size: 16px;
                        color: #fff;
                        background-color: #ff6b6b;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        text-decoration: none;
                        transition: background-color 0.3s ease;
                    }}
                    .btn:hover {{
                        background-color: #ff4a4a;
                    }}
                    .note {{
                        font-style: italic;
                        color: #888;
                        margin-top: 20px;
                        font-size: 14px;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 40px;
                        color: #999;
                        font-size: 14px;
                    }}
                </style>
                <title>Confirmación de Compra - Cine</title>
            </head>
            <body>
                <div class="container">
                    <h1>¡Compra Confirmada!</h1>
                    <p>Gracias por tu compra en nuestro cine! A continuación, te mostramos los detalles de tu reserva.</p>

                    <div class="details">
                        <h2>Detalles de la Película</h2>
                        <p><strong>Película:</strong>Coraline y la puerta secreta</p>
                        <p><strong>Fecha:</strong> {dia_var}</p>
                        <p><strong>Hora:</strong> {horario}</p>
                        <p><strong>Asientos seleccionados:</strong> {asientos_seleccionados}</p>
                    </div>

                    <div class="contact-info">
                        <h2>Información de Contacto</h2>
                        <p><strong>Telefono:</strong>11 4870 7273</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p class="note">*Si tiene alguna consulta no dude en contactarnos</p>
                    </div>

                    <p class="note">*Por favor, presenta este comprobante en la entrada del cine. ¡Disfruta la película!</p>
                </div>

                <div class="footer">
                    <p>&copy; 2024 CinePlus. Todos los derechos reservados.</p>
                </div>
            </body>
            </html>
            """

            # Crear un archivo HTML con el contenido
            file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads',f"entrada.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(contenidoHTML)

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Comprobante generado", f"Comprobante guardado en: {file_path}")

        def confirmar_compra(self):
            
            # Botón para descargar el comprobante
            self.btn_descargar_comprobante = tk.Button(self.paso4_frame, text="Descargar Comprobante", 
                                                       command=self.descargar_comprobante, bg="#42a5f5", fg="white", 
                                                       font=("Arial", 12, "bold"), relief="flat", padx=5, pady=5)
            self.btn_descargar_comprobante.pack(pady=10)

    
    app = CinemaApp(peli5_window)  # Asegúrate de pasar peli1_window, no root
    peli5_window.mainloop()  # Asegúrate de que mainloop esté en la ventana emergente


def open_cartelera(current_window): 
    root.withdraw()  # Oculta la ventana principal
    cartelera_window = tk.Toplevel(root)  # Crea una nueva ventana
    cartelera_window.title("Cine Retro - Cartelera")
    cartelera_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    cartelera_window.configure(bg=gris_claro)

    # Sección de encabezado
    header_frame = tk.Frame(cartelera_window, bg=gris_oscuro)
    header_frame.pack(fill=tk.X)

    # <----------------------------------Logo---------------------------------->
    logo = tk.PhotoImage(file="imagenes/logo2.PNG")  # Ruta de la imagen
    logo_label = tk.Label(header_frame, image=logo, bg=gris_oscuro)
    logo_label.image = logo  # Necesario para evitar que la imagen se recolecte como basura
    logo_label.pack(side="left", padx=20)

    # Navegación
    nav_frame = tk.Frame(header_frame, bg=gris_oscuro)
    nav_frame.pack(side=tk.RIGHT, padx=20)

    # Crear botones de navegación
    btn_inicio = tk.Button(nav_frame, text="Inicio", bg=naranja, fg=blanco, font=("Arial", 16),
                           borderwidth=4, command=lambda: [cartelera_window.withdraw(), root.deiconify()])  # Cambia a la función que deseas abrir
    btn_inicio.grid(row=0, column=0, padx=10)


    btn_cartelera = tk.Button(nav_frame, text="Cartelera", bg=naranja, fg=blanco, font=("Arial", 16),
                              borderwidth=4)
    btn_cartelera.grid(row=0, column=1, padx=10)

    btn_estrenos = tk.Button(nav_frame, text="Estrenos", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda:[cartelera_window.withdraw(), open_estrenos(current_window)])
    btn_estrenos.grid(row=0, column=2, padx=10)

    btn_horarios = tk.Button(nav_frame, text="Horarios", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda:[cartelera_window.withdraw(), open_horarios(current_window)])
    btn_horarios.grid(row=0, column=3, padx=10)

    btn_contacto = tk.Button(nav_frame, text="Contacto", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda:[cartelera_window.withdraw(), open_contacto(current_window)])
    btn_contacto.grid(row=0, column=4, padx=10)

    # Sección de cartelera
    main_frame = tk.Frame(cartelera_window, bg=gris_claro, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)


    # Función para crear una película
    def create_movie(frame, title, director, actors, schedule, img_file, peli_num):
        pelicula_frame = tk.Frame(frame, bg="#7f7f7f", bd=2, relief="solid", padx=10, pady=10)
        pelicula_frame.pack(fill="x", pady=10)

        # Cargar y redimensionar la imagen de la película
        imagen_peli = Image.open(img_file)  # Cargar la imagen
        imagen_peli = imagen_peli.resize((300, 200))  # Redimensionar la imagen
        imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)

        img_label = tk.Label(pelicula_frame, image=imagen_peli_tk, bg="#7f7f7f")
        img_label.image = imagen_peli_tk  # Mantener referencia para evitar que se elimine
        img_label.pack(side="left", padx=10)

        # Crear el marco de información
        info_frame = tk.Frame(pelicula_frame, bg="#7f7f7f")
        info_frame.pack(side="left", padx=10)

        title_label = tk.Label(info_frame, text=title, bg="#7f7f7f", fg="#ffcc00", font=('Arial', 16, 'bold'))
        title_label.pack(anchor="w")

        director_label = tk.Label(info_frame, text=f"Genero: {director}", bg="#7f7f7f", fg="white", font=('Arial', 12))
        director_label.pack(anchor="w")

        actors_label = tk.Label(info_frame, text=f"Duracion: {actors}", bg="#7f7f7f", fg="white", font=('Arial', 12))
        actors_label.pack(anchor="w")

        schedule_label = tk.Label(info_frame, text=f"Horario: {schedule}", bg="#7f7f7f", fg="white", font=('Arial', 12))
        schedule_label.pack(anchor="w")

        
        if peli_num == 1:
            ver_mas_button = tk.Button(info_frame, text="Ver más", command=lambda: open_peli4(root),
                                       bg="#ff4747", fg="white", bd=0, padx=10, pady=5, relief="flat")
        elif peli_num == 2:
            ver_mas_button = tk.Button(info_frame, text="Ver más", command=lambda: open_peli5(root),
                                       bg="#ff4747", fg="white", bd=0, padx=10, pady=5, relief="flat")
    
        ver_mas_button.pack(anchor="w", pady=10)

    # Crear películas (Ejemplo)
    create_movie(main_frame, "Sonrie 2", " Terror", "2 hora 8 minutos", 
             "Lunes y Viernes - 17:00 y 20:00 y PM", "peliculas/Sonrie 2.png", peli_num=1)
    create_movie(main_frame, "Coraline y la puerta secreta", "Terror", "1 Hora 40 Minutos",
             "Lunes y miercoles - 16:00, 18:00, 20:00 PM", "peliculas/Coraline.png", peli_num=2)

    # Footer (sección pie de página)
    footer = tk.Frame(cartelera_window, bg=gris_oscuro, padx=20, pady=10)
    footer.pack(fill="x", side="bottom")

    footer_text = tk.Label(footer, text="© 2024 Clasicos Del Ayer - Todos los derechos reservados", bg=gris_oscuro, 
                           fg=blanco, font=('Arial', 10))
    footer_text.pack()


def open_estrenos(current_window): 
    root.withdraw()  # Oculta la ventana principal
    estrenos_window = tk.Toplevel(root)  # Crea una nueva ventana
    estrenos_window.title("Cine Retro - estrenos")
    estrenos_window.attributes("-fullscreen", True)  # Tamaño de la ventana
    estrenos_window.configure(bg=gris_claro)

    # Sección de encabezado
    header_frame = tk.Frame(estrenos_window, bg=gris_oscuro)
    header_frame.pack(fill=tk.X)

    # <----------------------------------Logo---------------------------------->
    logo = tk.PhotoImage(file="imagenes/logo2.PNG")  # Ruta de la imagen
    logo_label = tk.Label(header_frame, image=logo, bg=gris_oscuro)
    logo_label.image = logo  # Necesario para evitar que la imagen se recolecte como basura
    logo_label.pack(side="left", padx=20)

    # Navegación
    nav_frame = tk.Frame(header_frame, bg=gris_oscuro)
    nav_frame.pack(side=tk.RIGHT, padx=20)

    # Crear botones de navegación
    btn_inicio = tk.Button(nav_frame, text="Inicio", bg=naranja, fg=blanco, font=("Arial", 16),
                           borderwidth=4, command=lambda: [estrenos_window.withdraw(), root.deiconify()])  # Cambia a la función que deseas abrir
    btn_inicio.grid(row=0, column=0, padx=10)


    btn_estrenos = tk.Button(nav_frame, text="Cartelera", bg=naranja, fg=blanco, font=("Arial", 16),
                              borderwidth=4, command=lambda:[estrenos_window.withdraw(), open_cartelera(current_window)])
    btn_estrenos.grid(row=0, column=1, padx=10)

    btn_estrenos = tk.Button(nav_frame, text="Estrenos", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4)
    btn_estrenos.grid(row=0, column=2, padx=10)

    btn_horarios = tk.Button(nav_frame, text="Horarios", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda:[estrenos_window.withdraw(), open_horarios(current_window)])
    btn_horarios.grid(row=0, column=3, padx=10)

    btn_contacto = tk.Button(nav_frame, text="Contacto", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda:[estrenos_window.withdraw(), open_contacto(current_window)])
    btn_contacto.grid(row=0, column=4, padx=10)

    # Sección de estrenos
    main_frame = tk.Frame(estrenos_window, bg=gris_claro, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)

    title_label = tk.Label(main_frame, text=f"Proximos estrenos{current_window}", fg="#ffcc00", bg=gris_claro, font=('Arial', 24, 'bold'))
    title_label.pack(pady=20)

    # Función para crear una película
    def create_movie(frame, title, director, actors, schedule, img_file, peli_num):
        pelicula_frame = tk.Frame(frame, bg="#7f7f7f", bd=2, relief="solid", padx=10, pady=10)
        pelicula_frame.pack(fill="x", pady=10)

        # Cargar y redimensionar la imagen de la película
        imagen_peli = Image.open(img_file)  # Cargar la imagen
        imagen_peli = imagen_peli.resize((300, 200))  # Redimensionar la imagen
        imagen_peli_tk = ImageTk.PhotoImage(imagen_peli)

        img_label = tk.Label(pelicula_frame, image=imagen_peli_tk, bg="#7f7f7f")
        img_label.image = imagen_peli_tk  # Mantener referencia para evitar que se elimine
        img_label.pack(side="left", padx=10)

        # Crear el marco de información
        info_frame = tk.Frame(pelicula_frame, bg="#7f7f7f")
        info_frame.pack(side="left", padx=10)

        title_label = tk.Label(info_frame, text=title, bg="#7f7f7f", fg="#ffcc00", font=('Arial', 16, 'bold'))
        title_label.pack(anchor="w")

        director_label = tk.Label(info_frame, text=f"Genero: {director}", bg="#7f7f7f", fg="white", font=('Arial', 12))
        director_label.pack(anchor="w")

        actors_label = tk.Label(info_frame, text=f"Duracion: {actors}", bg="#7f7f7f", fg="white", font=('Arial', 12))
        actors_label.pack(anchor="w")

        schedule_label = tk.Label(info_frame, text=f"clasificacion: {schedule}", bg="#7f7f7f", fg="white", font=('Arial', 12))
        schedule_label.pack(anchor="w")

        
        if peli_num == 1:
            ver_mas_button = tk.Button(info_frame, text="proximamente",
                                       bg="#ff4747", fg="white", bd=0, padx=10, pady=5, relief="flat")
        elif peli_num == 2:
            ver_mas_button = tk.Button(info_frame, text="proximamente",
                                       bg="#ff4747", fg="white", bd=0, padx=10, pady=5, relief="flat")
    
        ver_mas_button.pack(anchor="w", pady=10)

    # Crear películas (Ejemplo)
    create_movie(main_frame, "Codigo traje rojo", "Acción", "2 hora 4 minutos", 
             "Apta mayores de 13 años", "estrenos/traje rojo.png", peli_num=1)
    create_movie(main_frame, "NO TE SUELTES", "Terror", "1 Hora 42 Minutos",
             "Apta mayores de 16 años", "estrenos/no te sueltes.png", peli_num=2)

    # Footer (sección pie de página)
    footer = tk.Frame(estrenos_window, bg=gris_oscuro, padx=20, pady=10)
    footer.pack(fill="x", side="bottom")

    footer_text = tk.Label(footer, text="© 2024 Los Clasicos Del Ayer - Todos los derechos reservados", bg=gris_oscuro, 
                           fg=blanco, font=('Arial', 10))
    footer_text.pack()


def open_horarios(current_window):
    """Abre la ventana de horarios de películas."""
    # Oculta la ventana actual
    current_window.withdraw()

    # Crea la nueva ventana
    app = tk.Toplevel()  # Cambiar a Toplevel para mantener la referencia
    app.title("Horarios de Películas")
    app.attributes("-fullscreen", True)  # Tamaño de la ventana
    app.configure(bg="#525252")

    # <----------------------------------Header---------------------------------->
    header_frame = tk.Frame(app, bg="#333")
    header_frame.pack(fill="x", pady=0)

    # <----------------------------------Logo---------------------------------->
    logo = tk.PhotoImage(file="imagenes/logo2.PNG")  # Ruta de la imagen
    logo_label = tk.Label(header_frame, image=logo, bg="#333")
    logo_label.image = logo  # Necesario para evitar que la imagen se recolecte como basura
    logo_label.pack(side="left", padx=20)

    # <----------------------------------Navegación---------------------------------->
    nav_frame = tk.Frame(header_frame, bg="#333")
    nav_frame.pack(side="right", padx=20)

    # Crear botones de navegación
    btn_inicio = tk.Button(nav_frame, text="Inicio", bg=naranja, fg=blanco, font=("Arial", 16),
                           borderwidth=4, command=lambda: [app.withdraw(), current_window.deiconify()])
    btn_inicio.grid(row=0, column=0, padx=10)

    btn_cartelera = tk.Button(nav_frame, text="Cartelera", bg=naranja, fg=blanco, font=("Arial", 16),
                              borderwidth=4, command=lambda: [app.withdraw(), open_cartelera(current_window)])
    btn_cartelera.grid(row=0, column=1, padx=10)

    btn_estrenos = tk.Button(nav_frame, text="Estrenos", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda: [app.withdraw(), open_estrenos(current_window)])
    btn_estrenos.grid(row=0, column=2, padx=10)

    btn_horarios = tk.Button(nav_frame, text="Horarios", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4)
    btn_horarios.grid(row=0, column=3, padx=10)

    btn_contacto = tk.Button(nav_frame, text="Contacto", bg=naranja, fg=blanco, font=("Arial", 16),
                             borderwidth=4, command=lambda: [app.withdraw(), open_contacto(current_window)])
    btn_contacto.grid(row=0, column=4, padx=10)

    # <----------------------------------Container para Horarios---------------------------------->
    container_frame = tk.Frame(app, bg="#525252")
    container_frame.pack(pady=20)

    # Colocar las películas 1, 2 y 3 en la primera fila y 4, 5, y 6 en la segunda fila
    contenedor_de_horarios(container_frame, "Robot Salvaje", "Horario: 12:00 PM, 14:00 PM, 16:00 PM", 0, 0)
    contenedor_de_horarios(container_frame, "La Sustancia", "Horario: 15:00 PM, 17:00 PM, 19:00 PM", 0, 1)
    contenedor_de_horarios(container_frame, "Venom el ultimo baile", "Horario: 16:00 PM, 18:00 PM, 20:00 PM", 0, 2)
    contenedor_de_horarios(container_frame, "Sonrie 2", "Horario: 17:00 PM, 19:00 PM, 21:00 PM", 1, 0)
    contenedor_de_horarios(container_frame, "Terrifier 3", "Horario: 18:00 PM, 20:00 PM, 22:00 PM", 1, 1)
    contenedor_de_horarios(container_frame, "Volver al futuro", "Horario: 13:00 PM, 15:00 PM, 17:00 PM", 1, 2)

    # <----------------------------------Footer---------------------------------->
    footer = tk.Frame(app, bg=gris_oscuro, padx=20, pady=10)
    footer.pack(fill="x", side="bottom")

    footer_text = tk.Label(footer, text="© 2024 Cine Clasicos Del Ayer - Todos los derechos reservados", bg=gris_oscuro, 
                           fg=blanco, font=('Arial', 10))
    footer_text.pack()

    app.mainloop()


def open_contacto(current_window):
    """Abre la ventana de contacto."""
    # Oculta la ventana actual
    current_window.withdraw()

    # Crea la nueva ventana
    app = tk.Toplevel()  # Usar Toplevel para crear una ventana hija
    app.title("Contacto")
    app.attributes("-fullscreen", True)  # Tamaño de la ventana
    app.configure(bg="#525252")

    # <----------------------------------Header---------------------------------->
    header_frame = tk.Frame(app, bg="#333")
    header_frame.pack(fill="x", pady=0)

    # <----------------------------------Logo---------------------------------->
    logo = tk.PhotoImage(file="imagenes/logo2.PNG")  # Ruta de la imagen
    logo_label = tk.Label(header_frame, image=logo, bg="#333")
    logo_label.image = logo  # Necesario para evitar que la imagen se recolecte como basura
    logo_label.pack(side="left", padx=20)

    # <----------------------------------Navegación---------------------------------->
    nav_frame = tk.Frame(header_frame, bg="#333")
    nav_frame.pack(side="right", padx=20)

    nav_buttons = ["Inicio", "Cartelera", "Estrenos", "Horarios", "Contacto"]
    for button_text in nav_buttons:
        # Cambiar el comando según el botón
        if button_text == "Inicio":
            btn_command = lambda: [app.withdraw(), current_window.deiconify()]  # Regresa a la ventana inicial
        elif button_text == "Cartelera":
            btn_command = lambda: [app.withdraw(), open_cartelera(current_window)]
        elif button_text == "Estrenos":
            btn_command = lambda: [app.withdraw(), open_estrenos(current_window)]
        elif button_text == "Horarios":
            btn_command = lambda: [app.withdraw(), open_horarios(current_window)]
        else:  # "Contacto"
            btn_command = None  # Este botón no necesita acción, ya estamos en la ventana de contacto

        btn = tk.Button(nav_frame, text=button_text,
                        bg=naranja, fg=blanco, font=("Arial", 16),
                        borderwidth=4, relief="raised", 
                        command=btn_command)  # Asigna el comando correspondiente
        btn.pack(side=tk.LEFT, padx=10)

    # <----------------------------------Formulario de Contacto---------------------------------->

    # Marco para el contenido principal (QR y volante)
    content_frame = tk.Frame(app, bg="#525252")
    content_frame.pack(pady=50, padx=20, fill="both", expand=True)

    # Frame para los códigos QR y sus descripciones
    qr_frame = tk.Frame(content_frame, bg="#525252")
    qr_frame.pack(side="left", padx=20)

    # Generar los códigos QR con qrcode
    qr1_data = "https://clasiclosdelayer.modysistemas.tecnica4berazategui.edu.ar/inicio-cel.html"  # URL o información para el primer QR
    qr2_data = "https://www.instagram.com/losclasicosdelayer/"    # URL o información para el segundo QR

    qr1 = qrcode.make(qr1_data)
    qr2 = qrcode.make(qr2_data)

    # Convertir a formato compatible con Tkinter
    qr1_img = ImageTk.PhotoImage(qr1.resize((150, 150)))
    qr2_img = ImageTk.PhotoImage(qr2.resize((150, 150)))

    # Primer QR y descripción al lado
    qr1_container = tk.Frame(qr_frame, bg="#525252")
    qr1_container.pack(pady=10, anchor="w")

    qr1_label = tk.Label(qr1_container, image=qr1_img, bg="#525252")
    qr1_label.image = qr1_img
    qr1_label.pack(side="left")

    qr1_text = tk.Label(qr1_container, text="Escanea el QR y descubre una experiencia cinematográfica única. Sumérgete en nuestro cine retro, donde cada película se disfruta en un ambiente que revive el encanto de épocas pasadas. Desde películas de estreno hasta clásicos inolvidables, aquí encontrarás el mejor lugar para disfrutar del cine con estilo vintage", fg=blanco, bg="#525252", font=("Arial", 12),wraplength=400)
    qr1_text.pack(side="left", padx=10)

    # Segundo QR y descripción al lado
    qr2_container = tk.Frame(qr_frame, bg="#525252")
    qr2_container.pack(pady=10, anchor="w")

    qr2_label = tk.Label(qr2_container, image=qr2_img, bg="#525252")
    qr2_label.image = qr2_img
    qr2_label.pack(side="left")

    qr2_text = tk.Label(qr2_container, text="A través de nuestro perfil, podrás disfrutar de contenido exclusivo, novedades sobre nuestra cartelera y mucho más. Únete a nuestra comunidad de cinéfilos y mantente al tanto de todas nuestras proyecciones especiales y eventos únicos. ¡No olvides compartir tus momentos más memorables con nosotros usando nuestro hashtag!", fg=blanco, bg="#525252", font=("Arial", 12),wraplength=400)
    qr2_text.pack(side="left", padx=10)

    # <----------------------------------Volante---------------------------------->
    # Cargar imagen del volante
    volante_img = Image.open("imagenes/1.PNG")  # Asegúrate de ajustar la ruta y tamaño de la imagen
    volante_img = volante_img.resize((400, 550))  # Ajusta el tamaño según sea necesario
    volante_photo = ImageTk.PhotoImage(volante_img)

    volante_label = tk.Label(content_frame, image=volante_photo, bg="#525252")
    volante_label.image = volante_photo  # Necesario para evitar que la imagen se recolecte como basura
    volante_label.pack(side="right", padx=20)

    app.mainloop()



# <-----------------------------Inicio-------------------------------------------->
root = tk.Tk()
root.title("Clasicos Del Ayer")  # Título de la ventana
root.attributes("-fullscreen", True)  # Tamaño de la ventana
root.configure(bg=gris_claro)  # Color de fondo de la ventana

# Crear el encabezado
header_frame = tk.Frame(root, bg=gris_oscuro)
header_frame.pack(fill=tk.X)

# Cargar y redimensionar la imagen
ruta_imagen = "imagenes/logo2.PNG"
imagen_original = Image.open(ruta_imagen)
nuevo_tamaño = (250, 150)
imagen_redimensionada = imagen_original.resize(nuevo_tamaño)
imagen = ImageTk.PhotoImage(imagen_redimensionada)

# Colocar la imagen en el encabezado
etiqueta_imagen = tk.Label(header_frame, image=imagen, bg=gris_oscuro)
etiqueta_imagen.pack(side=tk.LEFT, padx=20)

# Crear el marco para los botones de navegación
nav_frame = tk.Frame(header_frame, bg=gris_oscuro)
nav_frame.pack(side=tk.RIGHT, padx=20)

# Crear botones de navegación
btn_inicio = tk.Button(nav_frame, text="Inicio", bg=naranja, fg=blanco, font=("Arial", 16),
                       borderwidth=4)  # abrir inicio
btn_inicio.grid(row=0, column=0, padx=10)

btn_cartelera = tk.Button(nav_frame, text="Cartelera", bg=naranja, fg=blanco, font=("Arial", 16),
                          borderwidth=4, command=lambda: open_cartelera(root))  # abrir cartelera
btn_cartelera.grid(row=0, column=1, padx=10)

btn_estrenos = tk.Button(nav_frame, text="Estrenos", bg=naranja, fg=blanco, font=("Arial", 16),
                         borderwidth=4, command=lambda: open_estrenos(root))  # abrir estrenos
btn_estrenos.grid(row=0, column=2, padx=10)

btn_horarios = tk.Button(nav_frame, text="Horarios", bg=naranja, fg=blanco, font=("Arial", 16),
                         borderwidth=4, command=lambda: open_horarios(root))  # abrir horarios
btn_horarios.grid(row=0, column=3, padx=10)

btn_contacto = tk.Button(nav_frame, text="Contacto", bg=naranja, fg=blanco, font=("Arial", 16),
                         borderwidth=4, command=lambda: open_contacto(root))  # abrir contacto
btn_contacto.grid(row=0, column=4, padx=10)


# Contenedor de películas
contenedor1 = tk.Frame(root, bg=negro_palido)
contenedor1.pack(pady=40, padx=30)

# agregar imagenes a las películas
agregar_pelicula(contenedor1, "El Padrino", "peliculas/Elpadrino.png", command=lambda: open_peli1(root))
agregar_pelicula(contenedor1, "Robot salvaje", "peliculas/Robot Salvaje.png", command=lambda: open_peli2(root))
agregar_pelicula(contenedor1, "el ultimo baile", "peliculas/venom el ultimo baile.png", command=lambda: open_peli3(root))

# Iniciar el bucle principal
root.mainloop()
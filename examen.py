import sys
from PyQt6.QtCore import QSize, Qt, QAbstractTableModel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox,  QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView)
#from modeloTaboa import ModeloTaboa
from conexionBD   import ConexionBD
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class ModeloTaboa(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self.datos = datos

    def rowCount(self, index):
        return len(self.datos)

    def columnCount(self, index):
        return len(self.datos[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self.datos[index.row()][index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            self.datos[index.row()][index.column()] = value
            return True
        return False


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 12-03-2024")

        self.estado= 'None'


        caixaV = QVBoxLayout()
        grid = QGridLayout()


        gpbCliente = QGroupBox("Cliente")
        gpbCliente.setLayout(grid)
        caixaV.addWidget(gpbCliente)

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")
        lblCodigoPostal = QLabel("Código postal")
        lblTelefono = QLabel("Teléfono")
        lblPais = QLabel ("País")
        lblAxenteComercial = QLabel("AxenteComercial")
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()
        self.txtProvinciaEstado = QLineEdit()
        self.txtCodigoPostal = QLineEdit()
        self.txtTelefono = QLineEdit()
        self.txtPais = QLineEdit()
        self.txtAxenteComercial = QLineEdit()


        grid.addWidget(lblNumeroCliente, 0,0,1,1)
        grid.addWidget(self.txtNumeroCliente, 0, 1, 1, 1)
        grid.addWidget(lblNomeCliente, 0,2,1,1)
        grid.addWidget(self.txtNomeCliente, 0, 3, 1, 1)
        grid.addWidget(lblApelidosCliente, 2,0,1,1)
        grid.addWidget(self.txtApelidosCliente, 2,1,1,3)
        grid.addWidget(lblDirección, 3,0,1,1)
        grid.addWidget(self.txtDireccion, 3,1,1,3)
        grid.addWidget(lblCidade,4, 0, 1,1)
        grid.addWidget(self.txtCidade, 4, 1, 1,1)
        grid.addWidget(lblProvinciaEstado, 4,2, 1,1)
        grid.addWidget(self.txtProvinciaEstado, 4,3, 1,1)
        grid.addWidget(lblCodigoPostal, 5,0,1,1)
        grid.addWidget(self.txtCodigoPostal, 5,1,1,1)
        grid.addWidget(lblTelefono, 5, 2, 1, 1)
        grid.addWidget(self.txtTelefono, 5, 3, 1, 1)
        grid.addWidget(lblPais,6,0,1,1)
        grid.addWidget(self.txtPais,6,1,1,1)
        grid.addWidget(lblAxenteComercial,6,2,1,1)
        grid.addWidget(self.txtAxenteComercial,6,3,1,1)


        caixaHTaboa = QHBoxLayout()


        self.tvwClientes = QTableView()
        self.tvwClientes.verticalHeader().hide()
        self.tvwClientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tvwClientes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        caixaHTaboa.addWidget(self.tvwClientes)
        conxBD = ConexionBD("modelosClasicos.dat")
        conxBD.conectaBD()
        conxBD.creaCursor()

        clientes = conxBD.consultaSenParametros("Select * from clientes")
        conxBD.pechaBD()

        self.tabla_data = clientes

        self.columna0 = []
        self.columna1 = []
        self.columna2 = []
        self.columna3 = []
        self.columna4 = []
        self.columna5 = []
        self.columna6 = []
        self.columna7 = []
        self.columna8 = []
        self.columna9 = []



        for fila in clientes:
            self.columna0.append(fila[0])  # Suponiendo que la primera columna es la columna 1
            self.columna1.append(fila[1])  # Suponiendo que la segunda columna es la columna 2
            self.columna2.append(fila[2])  # Suponiendo que la tercera columna es la columna 3
            self.columna3.append(fila[3])
            self.columna4.append(fila[4])
            self.columna5.append(fila[5])
            self.columna6.append(fila[6])
            self.columna7.append(fila[7])
            self.columna8.append(fila[8])
            self.columna9.append(fila[9])



        self.modelo = ModeloTaboa(clientes)
        self.tvwClientes.setModel(self.modelo)
        self.seleccion = self.tvwClientes.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_modelo_selectionChanged)



        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.setEnabled(True)
        self.btnEngadir.pressed.connect(self.on_btnEngadir_pressed)
        self.btnEditar = QPushButton("Editar")
        self.btnEditar.setEnabled(False)
        self.btnEditar.pressed.connect(self.on_btnEditar_pressed)
        self.btnBorrar = QPushButton("Borrar")
        self.btnBorrar.setEnabled(False)
        self.btnBorrar.pressed.connect(self.on_btnBorrar_pressed)

        caixaBotonsCorreo = QVBoxLayout()
        caixaBotonsCorreo.setAlignment(Qt.AlignmentFlag.AlignTop)
        caixaBotonsCorreo.addWidget(self.btnEngadir)
        caixaBotonsCorreo.addWidget(self.btnEditar)
        caixaBotonsCorreo.addWidget(self.btnBorrar)

        caixaHTaboa.addLayout(caixaBotonsCorreo)

        caixaV.addLayout(caixaHTaboa)

        caixaBtnAceptar = QHBoxLayout()
        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.pressed.connect(self.on_btnAceptar_pressed)
        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.pressed.connect(self.on_btnCancelar_pressed)
        caixaBtnAceptar.setAlignment(Qt.AlignmentFlag.AlignRight)
        caixaBtnAceptar.addWidget(self.btnCancelar)
        caixaBtnAceptar.addWidget(self.btnAceptar)
        caixaV.addLayout(caixaBtnAceptar)
        # BOTÓN GENERAR FACTURA
        self.botonGenerarFactura=QPushButton("Generar Factura")
        self.botonGenerarFactura.clicked.connect(self.on_botonGenerarFactura_clicked)
        caixaV.addWidget(self.botonGenerarFactura)


        contedor = QWidget()

        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)

        #self.setFixedSize (400,300)
        self.show()

    def on_btnEngadir_pressed(self):
        self.estado = 'Engadir'
        self.borrarCampos()
        self.btnEngadir.setEnabled(False)
        self.btnEditar.setEnabled(False)
        self.btnBorrar.setEnabled(False)


    def on_btnEditar_pressed(self):

        if self.seleccion.hasSelection():
            self.estado = 'Editar'
            self.cargarCamposDendeSeleccion()
            self.btnEngadir.setEnabled(False)
            self.btnEditar.setEnabled(False)
            self.btnBorrar.setEnabled(False)

    def on_btnBorrar_pressed(self):

        if self.seleccion.hasSelection():
            self.estado ="Borrar"
            self.cargarCamposDendeSeleccion()
            self.btnEngadir.setEnabled(False)
            self.btnEditar.setEnabled(False)
            self.btnBorrar.setEnabled(False)


    def on_btnAceptar_pressed(self):
        if self.estado == 'Engadir':
            conxBD = ConexionBD("modelosClasicos.dat")
            conxBD.conectaBD()
            conxBD.creaCursor()
            conxBD.engadeRexistro("""INSERT INTO clientes (numeroCliente, nomeCliente, apelidosCliente, telefono, direccion, cidade, provinciaEstado, codigoPostal, pais, axenteComercial)
                                           VALUES (?,?,?,?,?,?,?,?,?,?)""",
                                  int(self.txtNumeroCliente.text()),
                                  self.txtNomeCliente.text(),
                                  self.txtApelidosCliente.text(),
                                  self.txtTelefono.text(),
                                  self.txtDireccion.text(),
                                  self.txtCidade.text(),
                                  self.txtProvinciaEstado.text(),
                                  self.txtCodigoPostal.text(),
                                  self.txtPais.text(),
                                  int(self.txtAxenteComercial.text()))
            self.modelo.datos.append((int(self.txtNumeroCliente.text()),
                                      self.txtNomeCliente.text(),
                                      self.txtApelidosCliente.text(),
                                      self.txtTelefono.text(),
                                      self.txtDireccion.text(),
                                      self.txtCidade.text(),
                                      self.txtProvinciaEstado.text(),
                                      self.txtCodigoPostal.text(),
                                      self.txtPais.text(),
                                      int(self.txtAxenteComercial.text())))
            self.modelo.layoutChanged.emit()

        elif self.estado == 'Borrar':
            filas = self.seleccion.selectedRows()
            for fila in filas:
                i = fila.row()
                conxBD = ConexionBD("modelosClasicos.dat")
                conxBD.conectaBD()
                conxBD.creaCursor()
                conxBD.borraRexistro("DELETE FROM clientes WHERE numeroCliente = ?", self.modelo.datos[i][0] )
                del (self.modelo.datos[i])
                self.modelo.layoutChanged.emit()

        elif self.estado == 'Editar':
            filas =self.seleccion.selectedRows()
            for fila in filas:
                i = fila.row()
                conxBD = ConexionBD("modelosClasicos.dat")
                conxBD.conectaBD()
                conxBD.creaCursor()
                conxBD.actualizaRexistro("""UPDATE clientes SET 
                                                nomeCliente = ?,
                                                apelidosCliente = ?,
                                                telefono = ?,
                                                direccion = ?,
                                                cidade = ?,
                                                provinciaEstado = ?,
                                                codigoPostal = ?,
                                                pais = ?,
                                                axenteComercial = ?
                                            Where numeroCliente = ?""",
                                              self.txtNomeCliente.text(),
                                              self.txtApelidosCliente.text(),
                                              self.txtTelefono.text(),
                                              self.txtDireccion.text(),
                                              self.txtCidade.text(),
                                              self.txtProvinciaEstado.text(),
                                              self.txtCodigoPostal.text(),
                                              self.txtPais.text(),
                                              int(self.txtAxenteComercial.text()),
                                              int(self.txtNumeroCliente.text())
                                            )
                self.modelo.datos [i] = (
                self.modelo.datos[i][0],
                self.txtNomeCliente.text(),
                self.txtApelidosCliente.text(),
                self.txtTelefono.text(),
                self.txtDireccion.text(),
                self.txtCidade.text(),
                self.txtProvinciaEstado.text(),
                self.txtCodigoPostal.text(),
                self.txtPais.text(),
                int(self.txtAxenteComercial.text())
                )
                self.modelo.layoutChanged.emit()

        self.seleccion.clear()
        self.borrarCampos()
        self.estado= 'None'
        self.btnEngadir.setEnabled(True)
    def on_btnCancelar_pressed(self):
        self.seleccion.clear()
        self.btnEngadir.setEnabled(True)
        self.btnEditar.setEnabled (False)
        self.btnBorrar.setEnabled(False)
        self.borrarCampos()


    def on_modelo_selectionChanged(self):
        self.btnEngadir.setEnabled(True)
        self.btnBorrar.setEnabled (True)
        self.btnEditar.setEnabled(True)


    def cargarCamposDendeSeleccion(self):
        filas = self.seleccion.selectedRows()
        for fila in filas:
            i = fila.row()
            self.txtNumeroCliente.setText(str(self.modelo.datos[i][0]))
            self.txtNomeCliente.setText(self.modelo.datos[i][1])
            self.txtApelidosCliente.setText(self.modelo.datos[i][2])
            self.txtTelefono.setText(self.modelo.datos[i][3])
            self.txtDireccion.setText(self.modelo.datos[i][4])
            self.txtCidade.setText(self.modelo.datos[i][5])
            self.txtProvinciaEstado.setText(self.modelo.datos[i][6])
            self.txtCodigoPostal.setText(self.modelo.datos[i][7])
            self.txtPais.setText(self.modelo.datos[i][8])
            self.txtAxenteComercial.setText(str(self.modelo.datos[i][9]))

    def borrarCampos(self):
        self.txtNumeroCliente.setText('')
        self.txtNomeCliente.setText('')
        self.txtApelidosCliente.setText('')
        self.txtTelefono.setText('')
        self.txtDireccion.setText('')
        self.txtCidade.setText('')
        self.txtProvinciaEstado.setText('')
        self.txtCodigoPostal.setText('')
        self.txtPais.setText('')
        self.txtAxenteComercial.setText('')

    def on_botonGenerarFactura_clicked(self):
        """Generar factura al hacer clic en el botón."""
        try:
            print("Generando factura...")

            # Crear el archivo PDF
            c = canvas.Canvas("PDFExamen.pdf", pagesize=A4)
            c.setFont("Helvetica", 12)
            c.drawString(80, 765, "Ficha cliente")

            # Crear datos para la tabla
            #encabezadoTabla = ['ID', 'Fecha1', 'Fecha2', 'Numero']
            #infoTabla = self.tabla_data


            tabla_data2 = [['Numero cliente','1', 'Nome Cliente', 'Ana'],
                          ['Apelidos', 'Perez Diz'],
                          ['Direccion', 'Garcia Barbon'],
                          ['Cidade', 'Vigo', 'Provincia', 'Pontevedra'],
                          ['Codigo postal', '36201', 'Telefono', '986456780'],
                          ['Pais', 'España', 'Axente Comercial', '1'],
                          ]


            # Configurar el estilo de la tabla
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey), # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black), # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),# Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                #('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND', (2, 0), (-2, 0), colors.lightgrey),# Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                ('BACKGROUND', (2, 3), (-2, -1), colors.lightgrey),
                #('BACKGROUND', (0, -1), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                #('TEXTCOLOR', (0, -1), (-1, -1), colors.white),# Establece el color del texto en blanco para la última fila
                #('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                #('BACKGROUND', (0, -1), (1, -1), colors.white),# Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),  # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, 0), 1, colors.grey), # Agrega bordes a todas las celdas
                ('GRID', (0, 1), (0, 2), 1, colors.grey),
                ('GRID', (0, 3), (-1, -1), 1, colors.grey),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
            ])

            # TAMAÑO TABLA
            tabla = Table(data=tabla_data2)
            tabla.setStyle(estilo)

            # POSICION TABLA EN LIENZO
            tabla.wrapOn(c, 0, 0)
            tabla.drawOn(c, 80, 600)  # Ajusta las coordenadas


            infoTabla = self.tabla_data

            tabla_data3 = [['Numero cliente', '', 'Nome Cliente', ''],
                           ['Apelidos', ''],
                           ['Direccion', ''],
                           ['Cidade', '', 'Provincia', ''],
                           ['Codigo postal', '', 'Telefono', ''],
                           ['Pais', '', 'Axente Comercial', ''],
                           ]

            # Configurar el estilo de la tabla
            estilo3 = TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                # Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                # ('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND', (2, 0), (-2, 0), colors.lightgrey),
                # Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                ('BACKGROUND', (2, 3), (-2, -1), colors.lightgrey),
                # ('BACKGROUND', (0, -1), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                # ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),# Establece el color del texto en blanco para la última fila
                # ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                # ('BACKGROUND', (0, -1), (1, -1), colors.white),# Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),  # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, 0), 1, colors.grey),  # Agrega bordes a todas las celdas
                ('GRID', (0, 1), (0, 2), 1, colors.grey),
                ('GRID', (0, 3), (-1, -1), 1, colors.grey),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
            ])

            # TAMAÑO TABLA
            tabla3 = Table(data=infoTabla)
            tabla3.setStyle(estilo3)

            # POSICION TABLA EN LIENZO
            tabla3.wrapOn(c, 0, 0)
            tabla3.drawOn(c, 0, 400)

            tabla_data4 = [['Numero cliente', str(self.columna0), 'Nome Cliente', str(self.columna1)],
                           ['Apelidos', str(self.columna2)],
                           ['Direccion', str(self.columna3)],
                           ['Cidade', str(self.columna4), 'Provincia', str(self.columna5)],
                           ['Codigo postal', str(self.columna6), 'Telefono', str(self.columna7)],
                           ['Pais', str(self.columna8), 'Axente Comercial', str(self.columna9)],
                           ]

            # Configurar el estilo de la tabla
            estilo4 = TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                # Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                # ('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND', (2, 0), (-2, 0), colors.lightgrey),
                # Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                ('BACKGROUND', (2, 3), (-2, -1), colors.lightgrey),
                # ('BACKGROUND', (0, -1), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                # ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),# Establece el color del texto en blanco para la última fila
                # ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                # ('BACKGROUND', (0, -1), (1, -1), colors.white),# Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),  # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, 0), 1, colors.grey),  # Agrega bordes a todas las celdas
                ('GRID', (0, 1), (0, 2), 1, colors.grey),
                ('GRID', (0, 3), (-1, -1), 1, colors.grey),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
            ])

            # TAMAÑO TABLA
            tabla4 = Table(data=tabla_data4, colWidths=[100, 100, 100, 100])
            tabla4.setStyle(estilo3)

            # POSICION TABLA EN LIENZO
            tabla4.wrapOn(c, 0, 0)
            tabla4.drawOn(c, 10, 10)



            c.showPage()
            c.save()

            print("Factura generada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")


if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()
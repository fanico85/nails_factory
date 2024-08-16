=======================================================ENTREGA FINAL=====================================================

Requirements:
#Python 3.11.9
#django 4.2.15
La aplicacion es solo compatible con el explorador IE=edge, debido el temaplate conseguido. Se podrá acceder mediante la ruta: http://127.0.0.1:8000/core/
El servidor deberá levantarse con "python manage.py runserver" desde la ubicacion "nails_factory"

Introduccion:
La aplicacion tiene por objetivo facilitar la administracion de un negocio dedicado a brindar servicios de Belleza y Manicuria de uñas.
El modelo del negocio, es reducido. No se entrará en detalles del negocio, aperturas de caja, promociones, administracion de empleados, etc.

La funcionalidades disponibles son:
CRUD de Gastos
CRUD de Servicios
CRUD de Insumos y Marcas
CRUD de Formas de pago
CRUD de Clientes
Manejo de usuarios y su grupo de permisos
Registro de Atenciones realizadas

Comenzamos..
Ingreso al sitio:
    - Inicio de sesion
    - Registro de usuario sin rol alguno -> sera el aministrador quien asigne un rol

Pantalla principal:
    - Inicio -> informacion principal con tarjetas informativas mas informacion simulada en dos graficos
    - Administracion de servicios que brinda el negocio
    - Administracion de Gastos del negocio
    - Administracion de Insumos que utilizan para realizar los servicios y su stock
    - Atenciones que se realizan los clientes. Ademas incluyen la carga de una foto (ya que luego se subira a las redes sociales del negocio)
    - Usuarios donde solo el administrador puede visualizar los usuarios de la aplicacion y asignar un rol
    - Acerca de mi con el perfil del desarrollador

Panel superior:
    - Mi cuenta, donde se podra editar los datos del usuario conectado y asignarse un Avatar
    - Salir de la aplicacion


Aclaraciones:
    - Las Cards del inicio son:
        * Servicios disponibles -> es un contador de los servicios disponibles para los clientes; se puede navegar hasta una tabla con todos los servicios registrados
        * Gastos realizados -> es una sumatoria de todos los gastos realizados por el negocio (a futuro, solo incluiran los gastos del mes en curso). Actualmente la card
          esta en color azul, si supera los $100.000 se pondra en amarilla y si supera los $200.000 se pintará de rojo
        * Servicios realizados -> a futuro mostrara un contador de la cantidad de servicios realizados por los clientes durante el mes en curso
        * Atenciones realizadas -> es un contador de las atenciones realizadas (a futuro, solo incluiran las atenciones del mes en curso); se puede navegar hasta una tabla con todas las atenciones registrados
        * Insumos con Stock minimo -> es un contador de insumos que tienen un sotck por debajo de lo recomendado; se puede navegar hasta una tabla con todos los insumos 
          registrados; a futuro, la tabla tendra solo los insumos con stock minimo. Se pinta de azul cuando todos los insumos tienen un stock recomendado. se pinta de rojo
          cuando al menos 1 insumo tiene menos del stock minimo.
    
    - Permisos:
      * El administrador (usuario admin) es quien inicialmente tiene acceso a todas las funcionalidades.
      * El administrador podrá asignar o cambiar el rol de cualquier usuario
      * El administrador puede asignar nuevos administradores
      * Quien no sea administrador, solo podrá registrar Atenciones.

    - Dentro del repositorio, se encuentra la carpeta "others" con imagenes para Avatars, Atenciones, y el video explicativo sobre el funcioamiento del sitio 
    - Se podrán ejecutar las pruebas unitarias, validando la creacion y eliminacion de Servcios, Gastos, Marcas e Insumos, con el siguiente comando: python manage.py test
 
    - Usuarios de prueba:
      * admin       - password AB1234567  - rol Administrador
      * pruebaadmin - password 12345678ab - rol Administrador
      * pruebagral  - password 12345678ab - rol General
      * pruebacons  - password 12345678ab - rol Consulta
      * colli       - password F1234567   - rol Sin rol
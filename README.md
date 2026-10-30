# Tienda online

**Autor:** Pablo González Ferro

## Descripción

Aplicación en Python que gestiona una tienda online: usuarios (clientes y
administradores), productos (genéricos, electrónicos y de ropa) y pedidos.

Parte del modelo orientado a objetos de la Práctica 1 (clases `Producto`,
`ProductoElectronico`, `ProductoRopa`, `Usuario`, `Cliente`, `Administrador`,
`Pedido` y `TiendaService`) y expone su funcionalidad como una API REST hecha con
FastAPI. Los datos de entrada y salida se validan con esquemas Pydantic.

Los datos se guardan en una base de datos SQLite mediante SQLAlchemy, así que se
mantienen aunque se reinicie el servidor. Las clases del dominio son a la vez las
tablas de la base de datos (`usuarios`, `productos`, `pedidos` y `lineas_pedido`).

## Estructura del proyecto

```text
├── models/
│   ├── Producto.py        Clases/tablas de producto y esquemas ProductoCreate / ProductoRead
│   ├── Usuario.py         Clases/tablas de usuario y esquemas UsuarioCreate / UsuarioRead
│   └── Pedido.py          Clases/tablas de pedido y sus líneas, y esquemas de pedido
├── Services/
│   └── Tienda_service.py  TiendaService: lógica de la tienda sobre la base de datos
├── database.py            Conexión con SQLite (engine, sesiones y Base de SQLAlchemy)
├── main.py                Aplicación FastAPI y endpoints
└── requirements.txt       Dependencias
```

## Requisitos

- Python 3.10 o superior

## Instalación y ejecución

Desde la carpeta del proyecto:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

La API queda disponible en http://127.0.0.1:8000 y su documentación interactiva
(Swagger) en http://127.0.0.1:8000/docs.

Al arrancar se crea el fichero `tienda.db` (en la carpeta desde la que se lanza el
servidor) con las tablas necesarias. Para empezar con la base de datos vacía basta con
parar el servidor y borrar ese fichero. `tienda.db` no se sube al repositorio
(está en `.gitignore`).

## Endpoints

| Método | Ruta | Descripción |
| --- | --- | --- |
| POST | `/usuarios` | Crea un usuario (cliente o administrador) |
| GET | `/usuarios` | Lista los usuarios |
| GET | `/usuarios/{usuario_id}` | Devuelve un usuario |
| POST | `/productos` | Crea un producto (genérico, electrónico o ropa) |
| GET | `/productos` | Lista los productos |
| GET | `/productos/{producto_id}` | Devuelve un producto |
| DELETE | `/productos/{producto_id}` | Elimina un producto |
| POST | `/pedidos` | Crea un pedido comprobando cliente, productos y stock |
| GET | `/usuarios/{cliente_id}/pedidos` | Lista los pedidos de un cliente |

Los listados admiten parámetros de consulta:

- `GET /usuarios?nombre=juan`: filtra por nombre (coincidencia parcial).
- `GET /productos?tipo=ropa&nombre=cami`: filtra por tipo y por nombre.
- `skip` y `limit` en los dos listados para paginar, por ejemplo `?skip=0&limit=10`.

## Códigos de respuesta

- `201`: recurso creado.
- `400`: el usuario no es un cliente.
- `404`: usuario o producto no encontrado.
- `409`: email ya registrado o stock insuficiente.
- `422`: datos de entrada no válidos.

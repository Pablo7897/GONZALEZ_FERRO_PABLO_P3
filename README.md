# Tienda online

**Autor:** Pablo González Ferro

## Descripción

Aplicación en Python que gestiona una tienda online: usuarios (clientes y
administradores), productos (genéricos, electrónicos y de ropa) y pedidos.

Parte del modelo orientado a objetos de la Práctica 1 (clases `Producto`,
`ProductoElectronico`, `ProductoRopa`, `Usuario`, `Cliente`, `Administrador`,
`Pedido` y `TiendaService`) y expone su funcionalidad como una API REST hecha con
FastAPI. Los datos de entrada y salida se validan con esquemas Pydantic.

En esta versión los datos se guardan en memoria, dentro de `TiendaService`, y se
pierden al reiniciar el servidor.

## Estructura del proyecto

```text
Tienda_online/
├── models/
│   ├── Producto.py        Clases de producto y esquemas ProductoCreate / ProductoRead
│   ├── Usuario.py         Clases de usuario y esquemas UsuarioCreate / UsuarioRead
│   └── Pedido.py          Clase Pedido y esquemas de pedido
├── Services/
│   └── Tienda_service.py  TiendaService: lógica de la tienda
├── main.py                Aplicación FastAPI y endpoints
└── requirements.txt       Dependencias
```

## Requisitos

- Python 3.10 o superior

## Instalación y ejecución

```bash
cd Tienda_online
pip install -r requirements.txt
uvicorn main:app --reload
```

La API queda disponible en http://127.0.0.1:8000 y su documentación interactiva
(Swagger) en http://127.0.0.1:8000/docs.

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

## Códigos de respuesta

- `201`: recurso creado.
- `400`: el usuario no es un cliente.
- `404`: usuario o producto no encontrado.
- `409`: email ya registrado o stock insuficiente.
- `422`: datos de entrada no válidos.

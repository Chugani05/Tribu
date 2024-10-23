# Tribu

## Content
- [Descripción](#descripción)
- [Estructura](#estructura)

## Descripción

## Estructura
### Apps
- main
- shared
- echos (historias)
- waves (comentarios)

### Models
1. Echo:
   - Content
   - Created_at
   - Updated_at
   - User (FK)
    
2. Waves:
   - Content
   - Created_at
   - Updated_at
   - User (FK)
   - Echo (FK)

### URLs
- users/: listado de todos los usuarios
- echo/@(user)/: ver echos de un usuario
- echos/: listado de todos los echos de la aplicación
- echo/add/: añadir un echo
- echos/(id)/: detalle de un echo con un resúmen de los waves (los últimos 10)
- echo/(id)/edit/: editar echo
- echo/(id)/delete/: eliminar echo
- echo/(id)/waves/: visualiza el echo con todos sus waves
- echo/(id)/waves/add/: añadir un wave a un echo
- waves/(wave-id)/: detalles de un wave de un echo
- waves/(wave-id)/edit/: editar el wave de un echo
- waves/(wave-id)/delete/: eliminar el wave de un echo

# Tribu
<img src="shared/static/imgs/logo.png" alt="logo" width="30%">

## Content
- [Description](#description)
- [Structure](#structure)

## Description
Tribu is a social network built with Django, Python, and Bootstrap, where users can post echos (posts) and waves (comments) on the echos, along with having their own personal profiles.

## Structure
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
- users/@(user)/: muestra el perfil de un usuario
- @(user)/echos/: ver echos de un usuario
- echos/: listado de todos los echos de la aplicación
- echos/add/: añadir un echo
- echos/(id)/: detalle de un echo con un resúmen de los waves (los últimos 10)
- echos/(id)/edit/: editar echo
- echos/(id)/delete/: eliminar echo
- echos/(id)/waves/: visualiza el echo con todos sus waves
- echos/(id)/waves/add/: añadir un wave a un echo
- waves/(wave-id)/: detalles de un wave de un echo
- waves/(wave-id)/edit/: editar el wave de un echo
- waves/(wave-id)/delete/: eliminar el wave de un echo

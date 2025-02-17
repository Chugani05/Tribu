# Tribu
<img src="shared/static/imgs/logo.png" alt="logo" width="30%">

## Content
- [Description](#description)
- [Structure](#structure)
   - [Apps](#apps)
   - [Models](#models)
   - [URLs](#urls) 

## Description
Tribu is a social network built with Django, Python, and Bootstrap, where users can post echos (posts) and waves (comments) on the echos, along with having their own personal profiles.

## Structure
### Apps
- main
- shared
- accounts
- echos (historias)
- waves (comentarios)
- users

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
  
3. Users:
   - User
   - Avatar
   - Bio

### URLs

#### Accounts
- login/
- logout/
- signup/

#### Users
- users/: listado de todos los usuarios
- users/<@me>/: perfil de un usuario logeado
- users/<username>/: perfil de un usuario con un resúmen de los echos (los últimos 5)
- users/<username>/echos/: perfil de un usuario con todos sus echos
- users/<username>/edit/: editar el perfil de usuario

#### Echos
- echos/: listado de todos los echos de la aplicación
- echos/add/: añadir un echo
- echos/<pk:echo_pk>/: detalle de un echo con un resúmen de los waves (los últimos 10)
- echos/<pk:echo_pk>/edit/: editar echo
- echos/<pk:echo_pk>/delete/: eliminar echo
- echos/<pk:echo_pk>/waves/: visualiza el echo con todos sus waves
- echos/<pk:echo_pk>/waves/add/: añadir un wave a un echo

#### Waves
- waves/<pk:wave_pk>/edit/: editar el wave de un echo
- waves/<pk:wave_pk>/delete/: eliminar el wave de un echo

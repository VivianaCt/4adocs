from .usuarios import CrearUsuarioView, DetalleUsuarioView
from .login import LoginView, ManualLoginView, LoginCustomView, CheckToken
from .login_simple_jwt import *

#VISTAS DEL CRUD DE PRODUCTOS
from .producCreateView import ProductCreateView
from .productAllDetailView import ProductAllDetailView
from .productDeleteView import ProductDeleteView
from .productDetailView import ProductDetailView
from .productUpdateView import ProductUpdateView

#VISTA DEL CRUD USUARIO
from .userCreate import UserCreate
from .userDetail import UserDetail
from .userAllDetail import UserAllDetail
from .userDelete import UserDelete
from .userUpdate import UserUpdate

#VISTA DEL CRUD ADMINISTRADOR
from .adminCreate import AdminCreate
from .adminDetail import AdminDetail
from .adminAllDetail import AdminAllDetail
from .adminDelete import AdminDelete
from .adminUpdate import AdminUpdate



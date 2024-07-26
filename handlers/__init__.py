from .start_handler import register_handlers_start
from .user_handler import register_handlers_user
from .file_handler import register_handlers_file
from .shop_handler import register_handlers_shop
from .admin_handler import register_handlers_admin

__all__ = [
    "register_handlers_start",
    "register_handlers_user",
    "register_handlers_file",
    "register_handlers_shop",
    "register_handlers_admin",
]

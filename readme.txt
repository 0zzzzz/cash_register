Пользователь/пароль тестовой базы: admin/admin

JWT: Token a409759320766450ee077ad0ed3c2c8f72095fd1


{lockalhost}/api/cash_machine/
Принимает словарь с id'шниками товаров
{
	"items": [1, 2, 3, 4, 5, 6]
}


{lockalhost}/api/item_create/
POST принимает список словарей товаров
GET возвращает все товары в базе


{lockalhost}/api/item_update/<int:pk>/
PUT обновляет товар
DELETE удаляет товар
GET возвращает товар




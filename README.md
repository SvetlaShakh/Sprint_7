## Sprint_7
- #### Основа для написания теста - Pytest
- #### Установить внешние зависимости - requirements.txt
### Tests:

- **test_assert_order**

   Проверка запросов принятия заказа на ручку PUT /api/v1/orders/accept/:id
- **test_create_order**
   
   Проверка запросов создания заказа на ручку POST /api/v1/orders                        'в теле ответа указан track номер заказ
- **test_delete_courier**

   Проверка запросов удаления курьера на ручку DELETE /api/v1/courier/:id
- **test_get_list_orders**

   Проверка запроса получения списка заказов на ручку GET /api/v1/orders
-  **test_get_order_by_track**

   Проверка запросов получения заказа по track номеру на ручку GET /api/v1/orders/track
- **test_login_courier**

   Проверка запросов входа курьера в систему на ручку POST /api/v1/courier/login
-  **test_registration_courier**

   Проверка запросов создания курьера на ручку POST /api/v1/courier
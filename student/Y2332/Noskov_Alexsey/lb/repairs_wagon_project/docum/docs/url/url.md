``` python
path('worker/<int:pk>/', views.Worker_detail.as_view(), name="worker_d"),
# Вызов страницы выводящей заданного рабочего
path('worker/list/', views.Worker_List.as_view(), name='worker_l'),
# Вызов страницы выводящей всех рабочих
path('worker/<int:pk>/update/', views.WorkerUpdateView.as_view(), name="worker_u"),
# Вызов страницы обновляющей заданного рабочего
path('worker/add/', views.WorkerCreate.as_view()),
# Вызов страницы добавляющей рабочего
path('worker/<int:pk>/delete/', views.WorkerDelete.as_view(), name="worker_del"),
# Вызов страницы удаляющей рабочего
path('wagon/<int:pk>/', views.Wagon_detail.as_view(), name="wagon_d"),
# Вызов страницы выводящей заданный вагон
path('wagon/list/', views.Wagon_List.as_view(), name='wagon_l'),
# Вызов страницы выводящей все вагоны
path('wagon/<int:pk>/update/', views.WagonUpdateView.as_view(), name="wagon_u"),
# Вызов страницы обновляющей заданный вагон
path('wagon/add/', views.WagonCreate.as_view()),
# Вызов страницы добавляющей вагон
path('wagon/<int:pk>/delete/', views.WagonDelete.as_view(), name="wagon_del"),
# Вызов страницы удаляющей вагон
path('repair/<int:pk>/', views.Repair_detail.as_view(), name="repair_d"),
# Вызов страницы выводящей заданный ремонт
path('repair/list/', views.Repair_List.as_view(), name='repair_l'),
# Вызов страницы выводящей все ремонты
path('repair/<int:pk>/update/', views.RepairUpdateView.as_view(), name="repair_u"),
# Вызов страницы обновляющей заданного ремонт
path('repair/add/', views.RepairCreate.as_view()),
# Вызов страницы добавляющей ремонт
path('repair/<int:pk>/delete/', views.RepairDelete.as_view(), name="repair_del"),
# Вызов страницы удаляющей ремонт
path('menu_reliz/', views.Menu_reliz.as_view()),
# Вызов страницы показывающей начальную страницу сайта
```
# *Тестовое задание*

## *Ссылки и данные для входа*

Сайт - https://malikov123.pythonanywhere.com/

Админ-панель - https://malikov123.pythonanywhere.com/admin/

Для авторизации использовать следующие данные: 
  - login: **admin** 
  - password: **admin**

## *Описание*

stripe.com/docs - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 

Мы предлагаем вам познакомиться с этой прекрасной платежной системой, реализовав простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров. 

Для решения нужно использовать Django. Решение бонусных задач даст вам возможность прокачаться и показать свои умения, но это не обязательно. 

## *Задание*

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

Django Модель Item с полями (name, description, price) 

API с двумя методами:

GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

- Для перехода к выбранному объекту item можно с главной страницы нажать на кнопку **open** рядом с интересующим объектом.

- Для возвращения на главную страницу достаточно нажать на кнопку **Item list**

Залить решение на Github, описать запуск в Readme.md

Опубликовать свое решение чтобы его можно было быстро и легко протестировать. 

## *Бонусные задачи:* 

- Запуск используя Docker
  - **Выполнено**. 
  - Для запуска в корневом каталоге выполнить команду **docker-compose up --build**
Сайт будет доступен по адресу 
    - *127.0.0.1:8000* для windows 
    - *0.0.0.0:8000* для linux или mac

- Использование environment variables.
  - **Выполнено**

- Просмотр Django Моделей в Django Admin панели.
  - **Выполнено** 

- Запуск приложения на удаленном сервере, доступном для тестирования.
  - **Выполнено**.
  - Для тестирования приложения можно перейти на сайт **https://malikov123.pythonanywhere.com/**
  - Для авторизации использовать следующие данные: 
    - login: **admin** 
    - password: **admin**
  - Вход в админ-панель происходит по адресу **https://malikov123.pythonanywhere.com/admin/**

- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
  - Работает только для **авторизованных пользователей** - у заказа должен быть покупатель, который этот заказ собирает.
  - Можно добавить товары в заказ через админ-панель или при переходе к кажому товару, нажав на кноку **Add to order**
  - Для просмотра заказа на главной странице нажать на кнопку **Go to order**
  - Для покупки заказа нажать на кнопку **Buy order**
  - Для очистки заказа пользователя нажать на кнопку **Clear order**
- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
  - **Выполнено**
- Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте 
  - Не реализовал
- Реализовать не Stripe Session, а Stripe Payment Intent.
  - Не реализовал

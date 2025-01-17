# Лабораторная работа № 4. Реализация клиентской части приложения средствами Vue.js

## Задание

1. Выполнить практическую работу 4.1 Базовые конструкции языка JavaScript.
2. Выполнить практическую работу 4.2. Работа с Vue.JS.
3. Утвердить с одним из преподавателей список интерфейсов для взаимодействия с серверной частью в соответствии с вашей предметной областью.
4. Реализовать интерфейсы авторизации, регистрации и изменения учётных данных и настроить взаимодействие с серверной частью. 
5. Подключить vuetify или аналогичную библиотеку.
6. Реализовать документацию, описывающую работу разработанных интерфейсов средствами MkDocs.

## Страницы сайта

Была реализована клиентская часть для программной системы, предназначенной для администратора гостиницы:

- Без авторизации доступ к страницам ограничен

![](img\lab4\home-nologin.PNG)

- Можно зарегистрировать нового администратора (успешная регистрация подтверждается во всплывающем окне)

![](img\lab4\register.PNG)

- Можно войти по своему логину и паролю (успешный вход подтверждается во всплывающем окне)

![](img\lab4\login.PNG)

- После входа доступно отображение таблиц со свободными комнатами, бронированиями, клиентами, служащими и расписанием уборки этажей. Также можно выйти из своей учетной записи

![](img\lab4\home-login.PNG)

- В личном кабинете можно редактировать персональные данные

![](img\lab4\lk.PNG)

- Можно добавить в систему нового клиента

![](img\lab4\addclient.PNG)

- Можно "заселить клиента в комнату" - создать запись в модели бронирования

![](img\lab4\addbooking.PNG)

- Можно "выселить клиента из комнаты" - редактировать поле с датой выселения записи в модели бронирования

![](img\lab4\updatebooking.PNG)

- Можно добавить новую запись в модель с расписанием уборки этажей

![](img\lab4\addschedule.PNG)

- Можно удалить неактуальную запись в расписании уборки этажей

![](img\lab4\delsched.PNG)


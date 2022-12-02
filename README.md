# **Проверка света дома**
Для работы этого скрипта вам нужно одно из этих условий:
 - Роутер, который потдерживает скрипты (в моём случае это [MikroTik hAP ac](https://mikrotik.ua/ru/product/mikrotik-hap-ac-rb962uigs-5hact2hnt))
 - Статический IP
## **Навигация**
  * [Подготовка телеграма](#podgotovka_telegram)
    * [Создание бота и получение его токена](#podgotovka_telegram_token)
    * [Берем нужные данные из telegram](#podgotovka_telegram_dannie)



## <a name="podgotovka_telegram"></a>**Подготовка телеграма**
### <a name="podgotovka_telegram_token"></a>**Создание бота и получение его токена**
1. Заходим в телеграм и ищем **[@BotFather](https://t.me/BotFather)**<br>![BotFather](https://imgur.com/fQvoRo2.png)
2. Пишем команду ***```/start```***<br>![/start](https://imgur.com/5le8OEM.png)
3. Выбираем команду ***```/newbot```***<br>![/newbot](https://imgur.com/Ghr15C9.png)
4. Пишем **Имя** бота(любое имя, так будет подписан сам бот) затем его **username_bot**(например: test_bot)<br>![name and username_bot](https://imgur.com/RRJhhYe.png)
5. Нужно сохранить этот токен<br>![BotFather](https://imgur.com/gCICgY4.png)<br>
   В моем случае токен такой:
   ```
   5895410925:AAEQQUCagvTmFLkCe_SSikN8QveoqjpCnn8
   ```

### <a name="podgotovka_telegram_dannie"></a>**Берем нужные данные из telegram**
   если вам не нужен бот в группе и вы хотите что бы он присылал вам сообщения в личку - вам следует пропустить первые два пункта.
   1. Создаем группу телеграм и добавляем в нее тех, кому должно приходить уведомление
   2. Добавляем в нее бота по его **username_bot**, в моем случае это Your_name_with_bot_<br>![add bot](https://imgur.com/FCl1d22.png)<br>
   3. | Личные сообщения| Группа           |
      | ------------- | ------------------  |
      | 1. Ищем [@getmyid_bot](https://t.me/getmyid_bot)|1. Ищем [@getmyid_bot](https://t.me/getmyid_bot)|
      | 2.  Пишем ***```/start```*** | 2. Добавляем этого бота в нашу группу |
      | 3. Сохраняем ваш ID<br>в моем случае это ```833292637``` <br>![id](https://imgur.com/AkBSpmJ.png)| 3. Пишем ***```/start@getmyid_bot```***|
      ||4. Сохраняем айди чата<br>в моем случае это ```-895594889```<br>![id](https://imgur.com/8cjCaT5.png)|


## **Настройка Heroku**
|    |             |
| - | -  |
|1. Заходим на сайт [signup.heroku.com](https://signup.heroku.com/)<br><br>2. Заполняем форму регистрации<br><br>3. В *Role * выбираем *Hobbyist<br><br>4. В *Primary development language* выбираем ```Python```<br><br>5. Подтверждаем почту|![heroku_reg](https://imgur.com/ojVie5t.png)|
|6. Придумываем пароль и завершаем регистрацию|![heroku_pass](https://imgur.com/ckU3Pno.png)|
|7. Заходим на [dashboard.heroku.com/terms-of-service](https://dashboard.heroku.com/terms-of-service) и нажимаем ***Accept***<br><br>8. Заходим на [dashboard.heroku.com/account/billing](https://dashboard.heroku.com/account/billing). <br>Нажимаем ***Add credit card*** и добавляем банковскую карту,<br>(деньги с нее списываться не будут)<br><br>|![heroku_new_ap](https://imgur.com/llmJQ7D.png)|
|9. Нажимаем на [***Create new app***](https://dashboard.heroku.com/new-app)<br><br>10. В **App name** пишем название программы, в моем случае ```check-light-at-home```<br><br>10. В регионе выбираем ***Europe***<br><br>11. Нажимаем ***Create app***|![heroku_app-reg](https://imgur.com/OIE27RR.png)|

## **НастройкаPythonAnyWhere**

|    |             |
| - | -  |
|1. Заходим на сайт [pythonanywhere.com/registration/register/beginner/](https://www.pythonanywhere.com/registration/register/beginner/)<br><br>2. Заполняем форму регистрации<br><br>3. Подтверждаем почту|![](https://imgur.com/zsBHJVJ.png)|
|4. Заходим во вкладку Web<br><br>5. Нажимаем  Add a new web app > Next > <br>> Выбираем Flask > Python 3.10 > Next > Ждем|![](https://imgur.com/GdSoaW2.png)|
|6. Попадаем на страницу нашего web-приложения.<br><br>7. Сохраняем ссылку на ваш сайт(синяя):|![](https://imgur.com/p7EG9QL.png)|
|8. Листаем ниже > во вкладке Code переходим в <br>Source code: смотреть на фото|![](https://imgur.com/Cxhib2L.png)|
|9. Нажимаем на файл с именем ***flask_app.py***<br><br>10. Удаляем все с файла и вставляем код с [flask_code.txt](https://github.com/Corkerro/checkLightAtHome/blob/main/flask_code.txt)||

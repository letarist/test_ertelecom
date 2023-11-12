<h1>Тестовое задание в ЭРТЕЛЕКОМ</h1>
<h2>Реализовано на чистой Django 4.2.7</h2>
Реализовано, наверняка много лишнего, потому что возникло несколько вопросов по ТЗ, реализовал как понял, некоторые задачи в 2 экземплярах.
<h2>Основные вопросы:</h2>
<ol>
<li>...Модуль и функцию необходимо подгружать динамически по строковому
названию, указанному в полях "module" и "function".
В случае, если в параметрах указан отсутствующий на сервере
модуль/функция, возвращать ошибку 500: "Unknown module NAME" или
"Unknown function NAME" соответственно.</li>
несовсем понятно что подразумевается под динамической загрузкой.
<b>Реализовано следующим образом:</b>
<ul>При отправке GET запроса на http://127.0.0.1/json/ открывается страница с 2 текстовыми полями, при вводе данных в которые происходит динамический поиск данных по названию модуля или функции (реализовал на jquery+ajax)</ul><br>
<ul>Реализован поиск по get параметрам. Чтобы проверить, есть ли тот или иной модуль или функция в базе, нужно в адресной строке вбить http://127.0.0.1:8000/json/?module=название_искомого_модуля для поиска модуля, и http://127.0.0.1:8000/json/?function=название_искомой_функции для поиска функции соответственно. На выходе получаем массив Json-объектов, так как объектов с одинаковыми названиями модулей или функций может быть несколько.</ul><br>
<li>Реализовать на серверной стороне второй маршрут /html/ - веб-страница с
таблицей, на которой отображаются все функции доступные для
автоимпорта, а так же исходный код этих функций и docstring из этих
функций.</li>
<b>опять же, непонятно, что требуется. Выгрузить все данные которые мы загрузили из json-файла, или все модули которые были загружены для реализации проекта.</b><br>
<b>Реализовано следующим образом:</b>
<ul>При переходе на http://127.0.0.1/html/ откроется страница с данными, подгруженными из JSON файла, абсолютно все</ul><br>
<ul>При переходе на http://127.0.0.1:8000/my_func/ откроется страница с автоподгружаемыми модулями django, там только ORM модули</ul>
</ol>
<h2>Как развернуть окружение:</h2>
<ol>
<li>Переходим в папку проекта:</li>
<code>cd show_json/</code>
<li>Создаем и активируем виртуальное окружение:<br>
<code>python -m venv env<br>
source env/bin/activate</code></li>
<li>Установить все данные из файла requirements.txt с помощью команды
<code>pip install -r requirements.txt</code>
После установки запустить локальный сервер командой
<code>python manage.py runserver</code></li>
  <li>Проводим и применяем миграции:
  <code>python manage.py makemigrations</code><br>
  <code>python manage.py migrate</code></li>
</ol>
<br>
И еще один момент, нужно было записать массив в таблицу, насколько я знаю, этого сделать нельзя. Для этого я использовал JsonField.
В Postgres можно, но в ТЗ не написано что нужно его использовать. В этом случае можно было бы использовать ArrayField или ListField из django.contrib.postgres.fields

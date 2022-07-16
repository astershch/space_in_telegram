# Space Telegram

Набор скриптов для загрузки фотографий NASA и SpaceX в канал Telegram.

## Как установить

Для работы скриптов необходимо добавить переменные окружения (или файл .env в корне скриптов):
- NASA_API_TOKEN - токен для работы с [API NASA](https://api.nasa.gov/)
- NASA_APOD_URL - адрес API NASA APOD (https://api.nasa.gov/planetary/apod)
- NASA_EPIC_URL - адрес API NASA EPIC (https://api.nasa.gov/EPIC/api/natural/images)
- SPACEX_URL - адрес API SpaceX (https://api.spacexdata.com/v5/launches)
- IMAGES_DIRECTORY - директория для хранения изображений
- TG_BOT_TOKEN - токен бота Telegram
- TG_CHAT_ID - название канала, в который будут опубликованы изображения
- TG_PUBLICATONS_DELAY - задержка в часах после публикации каждой фотографии через [send_telegram_photos.py](#send_telegram_photos.py)

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```bash
pip install -r requirements.txt
```

## Как использовать

### fetch_spacex_images.py
Загружает фотографии с запуска SpaceX в директорию `IMAGES_DIRECTORY`.

Для загрузки фотографий с последнего запуска:
```bash
python fetch_spacex_images.py
```
Для загрузки фотографий по известному flight_id:
```bash
python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```

### fetch_nasa_apod_imagex.py
Загружает не более 30 фотографий NASA Astronomy Picture of the Day в директорию `IMAGES_DIRECTORY`:
```bash
python fetch_nasa_apod_images.py
```

### fetch_nasa_epic_images.py
Загружает еждневные фотографии NASA Earth Polychromatic Imaging Camera в директорию `IMAGES_DIRECTORY`:
```bash
python fetch_nasa_epic_images.py
```

### send_telegram_photo.py
Публикует фотографию в канал Telegram `TG_CHAT_ID`.

Для публикации случайной фотографии из `IMAGES_DIRECTORY`:
```bash
python send_telegram_photo.py
```
Для публикации фотографии по пути `./images/nasa_01.jpg`:
```bash
python send_telegram_photo.py ./images/nasa_01.jpg
```

### send_telegram_photos.py
Публикует одну фотографию в канал Telegram `TG_CHAT_ID` из директории `IMAGES_DIRECTORY` раз в 4 часа
или если задано значение - раз в `TG_PUBLICATONS_DELAY` часов.
```bash
python send_telegram_photos.py
```

### send_telegram_photos.py
Набор вспомогательных функций для работы скриптов.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)
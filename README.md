# wan27_tg_bot

Стартовый шаблон Telegram-бота на Python с использованием `python-telegram-bot`.

## Что внутри

- `bot.py` — точка входа бота
- `requirements.txt` — зависимости проекта
- `.env.example` — пример переменных окружения
- `.gitignore` — исключения для Git

## Быстрый старт

1. Создайте виртуальное окружение:

```bash
python -m venv .venv
```

2. Активируйте его:

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` на основе `.env.example`:

```bash
cp .env.example .env
```

5. Добавьте токен бота от BotFather в `.env`:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

6. Запустите бота:

```bash
python bot.py
```

## Команды

- `/start` — приветствие
- `/help` — список доступных команд

## Важно

Не коммитьте `.env` и токены в репозиторий.

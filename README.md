# One-page website for a service company.
### Stack:
- Django
- SQLite
- Jinja Temlate
- Bootstrap
- TelegramBotApi
### Applications inside:
- slider (changing text, background pictures is available),
- prices (the user can change the services and prices for them),
- telegram bot (data about a new application from the completed form is sent to telegram),
- crm (user account: orders and status with comments to them are displayed).

### Quickstart with Docker
1. Clone the repository:

```
git clone https://github.com/ktlog/service_sales_app.git
cd service_sales_app

```

2. Create .env file in the root and set environment variable for application:

```
touch .env
echo DEBUG=True >> .env
echo DJANGO_KEY=$(openssl rand -hex 30) >> .env
```

3. Finally, run:

```
docker compose up --build
```

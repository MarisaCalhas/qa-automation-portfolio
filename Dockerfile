FROM python:3.11-slim

WORKDIR /app

# dependências do sistema para Playwright
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxrandr2 \
    libasound2 \
    libxdamage1 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN playwright install --with-deps

COPY . .

CMD ["pytest", "-n", "2", "--alluredir=allure-results"]
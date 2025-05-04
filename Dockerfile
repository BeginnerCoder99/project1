# 1) Use a slim Python image
FROM python:3.11-slim

# 2) Install OS deps for Chrome + Puppeteer
RUN apt-get update && apt-get install -y \
      wget gnupg2 unzip curl \
      # Chrome needs these fonts + glibc bits
      fonts-liberation libnss3 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
      libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
      libxss1 libxtst6 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 \
      libdrm2 libgbm1 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3) Install Google Chrome Stable
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
      | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# 4) Set working directory
WORKDIR /app

# 5) Copy Python requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy the rest of your project code
COPY . .

# 7) Default command to run your scraper + sentiment pipeline
CMD ["python", "main.py"]

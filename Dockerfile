# Puts python in docker
FROM python:3.11-slim

# Installs chrome
RUN apt-get update && apt-get install -y \

      fonts-liberation libnss3 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
      libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 \
      libxss1 libxtst6 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 \
      libdrm2 libgbm1 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Sets up chrome for headless
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
      | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Sets up directory for image
WORKDIR /app

# installs everything needed for program
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copies codes
COPY . .

# 7) Default command to run program
CMD ["python", "main.py"]

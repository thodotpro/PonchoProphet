FROM node:20-slim

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source
COPY . .

EXPOSE 5173

# The command is overridden in docker-compose.yml for dev, 
# but we provide a default here.
CMD ["npm", "run", "dev", "--", "--host"]

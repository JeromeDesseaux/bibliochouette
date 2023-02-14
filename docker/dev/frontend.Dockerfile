FROM node:lts-alpine AS development
ENV NODE_ENV development
# Add a work directory
WORKDIR /app
# Cache and Install dependencies
COPY frontend/package.json .
RUN yarn install

# Expose port
EXPOSE 3000
# Use nginx image
FROM nginx:latest

# Copy our website files into nginx
COPY index.html /usr/share/nginx/html/index.html

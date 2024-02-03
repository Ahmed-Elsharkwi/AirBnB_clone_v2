#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static
sudo apt upgrade
sudo apt install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<h1> Ahmed is the best </h1>" > /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ]
then
  ln -sf /data/web_static/releases/test /data/web_static/current
else
  ln -s /data/web_static/releases/test /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    add_header X-Served-By "$HOSTNAME";
    error_page 404 /error-page.html;
    location /error-page.html {
        root /var/www/html;
        internal;
    }
    location /hbnb_static/{
	alias /data/web_static/current/;
    }
 }" > /etc/nginx/sites-available/default
 service nginx restart

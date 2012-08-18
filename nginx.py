#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
For:
by Lerry  http://lerry.org
Start from 2012-08-18 20:59
Last edit at 2012-08-18 20:59
'''
server {
    server_name img.ldev.tk;
    listen 80;
    charset utf-8;
    expires max;

	location / {
		expires -1;
		proxy_set_header Host $host;
		proxy_pass http://127.0.0.1:8080/;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		
    #access_log /var/log/nginx/main.access_log info;
    #error_log /var/log/nginx/main.error_log info;
    }

    location /static {
        autoindex off;
        alias  /home/lerry/My-Photo-Lib/static;
    }

    location /favicon.ico {
        alias  /home/lerry/My-Photo-Lib/static/favicon.ico;
    }

    location /robots.txt {
        alias  /home/lerry/My-Photo-Lib/static/robots.txt;
    }
}
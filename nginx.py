#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Start from 2012-08-18 20:59
Last edit at 2012-08-18 20:59
'''
import _env
from os.path import join
from jinja2 import Template
from config import HOST, IMG_ROOT, PWD

static_path = join(PWD, 'static')

NGINX_TMP =\
'''
server {
    server_name {{ host }};
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
{% for i in ['', '/favicon.ico', '/robots.txt'] %}
    location /static{{ i }} { 
        autoindex off;
        alias {{ static_path }}{{ i }}; 
    }
{% endfor %}
}
'''

tml = Template(NGINX_TMP).render(host=HOST, static_path=static_path).strip()

if __name__ == '__main__':
    print tml
    f = open(join(PWD, 'photo_lib.conf'), 'w')
    f.write(tml)
    f.close()
    print 'Nginx config file created successfully'

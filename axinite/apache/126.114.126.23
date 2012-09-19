<VirtualHost *:80>
   ServerName 126.114.126.23
   ServerAlias 126.114.126.23.*.com
   ServerAdmin 126.114.126.23@126.114.126.23.com

   DocumentRoot /home/axinite/axinite/axinite/


   Alias /robots.txt /home/axinite/axinite/axinite/static/robots.txt
   Alias /favicon.ico /home/axinite/axinite/axinite/static/favicon.ico

   Alias /static/ /home/axinite/axinite/axinite/static/
   Alias /media/ /home/axinite/axinite/axinite/static/

   <Directory /home/axinite/axinite/axinite/static>
       Options None
       Order deny,allow
       Allow from all
   </Directory>

   WSGIDaemonProcess 126.114.126.23 user=axinite group=axinite processes=5 threads=1 maximum-requests=100
   WSGIProcessGroup  126.114.126.23
   WSGIScriptAlias / /home/axinite/axinite/axinite/django.wsgi

   <Directory /home/axinite/axinite/axinite/apache>
      Order allow,deny
      Allow from all
   </Directory>

   ErrorLog /home/axinite/axinite/axinite/log/error.log
   CustomLog /home/axinite/axinite/axinite/log/access.log combined
</VirtualHost>
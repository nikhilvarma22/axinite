<VirtualHost *:80>
   ServerName www.axinite.com
   ServerAlias axinite.*.com
   ServerAdmin axinite@axinite.com

   DocumentRoot /home/vermani/axinite/axinite/


   Alias /robots.txt /home/vermani/axinite/axinite/static/robots.txt
   Alias /favicon.ico /home/vermani/axinite/axinite/static/favicon.ico

   Alias /static/ /home/vermani/axinite/axinite/static/
   Alias /media/ /home/vermani/axinite/axinite/static/

   <Directory /home/vermani/axinite/axinite/static>
       Options None
       Order deny,allow
       Allow from all
   </Directory>

   WSGIDaemonProcess www.axinite.com user=axinite group=axinite processes=5 threads=1 maximum-requests=100
   WSGIProcessGroup  www.axinite.com
   WSGIScriptAlias / /home/vermani/axinite/axinite/django.wsgi

   <Directory /home/vermani/axinite/axinite/apache>
      Order allow,deny
      Allow from all
   </Directory>

   ErrorLog /home/vermani/axinite/axinite/log/error.log
   CustomLog /home/vermani/axinite/axinite/log/access.log combined
</VirtualHost>
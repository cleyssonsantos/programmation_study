FROM php:7.4-cli

WORKDIR /var/www

RUN apt-get update && \
    apt-get install libzip-dev -y && \
    docker-php-ext-install zip

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');"

RUN php composer.phar create-project laravel/laravel laravel

ENTRYPOINT [ "php","laravel/artisan","serve" ]

# Esse comando é substituível, caso eu passe algum argumento depois de subir a imagem, ele vai substituir, ex:
# docker run --rm -d --name laravel -p 8002:8002 cleyssonsantosestudo/laravel --host=0.0.0.0 --port=8002
CMD [ "--host=0.0.0.0" ]

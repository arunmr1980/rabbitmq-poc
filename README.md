Starting a docker container

The following command is used to start a docker container

docker run --name rabbit_mq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=arunmr -e RABBITMQ_DEFAULT_PASS=milktreat -v /home/arun/Learning/rabbitmq-poc/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf bitnami/rabbitmq:3.12.1

These are the options and why they are used

-p Port mapping is used for to map the default port in rabbitmq to the local. Port 15672 is used for web console and 5672 is used for rabbitmq service
-e The username and password are set as environment variables. Use these to login to the web console
-v Volume mounting is required only if you need to override the default rabbitmq.conf


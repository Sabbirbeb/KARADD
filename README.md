pip install -r requirements.txt

docker build -t testt
docker run -d --name mycontainer -p 8080:8080 testt
docker run testt

docker container rm mycontainer -f 



https://www.atlantic.net/dedicated-server-hosting/how-to-deploy-and-run-redis-in-docker/


docker pull redis:latest 
docker run --net host --name redis-instance -dit redis
docker exec -it redis-instance /bin/bash
redis-cli

set key aaaaaa
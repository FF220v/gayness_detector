docker network create -d bridge lecture_network

docker rm -f lecture_server
docker rm -f lecture_redis
docker rm -f lecture_webdis
docker run -d --name lecture_redis --network lecture_network redis
docker run -d --name lecture_webdis --link lecture_redis:redis --network lecture_network anapsix/webdis
docker run -it --name lecture_server --network lecture_network -p 8080:8080 lecture_server_image

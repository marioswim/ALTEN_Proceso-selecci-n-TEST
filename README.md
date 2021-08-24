# ALTEN_Proceso-selecci-n-TEST
powerplant-coding-challenge


## Building the image

In order to build the docker container, It needed use the next command:
```
docker build . -t power_plant_production:mario-quesada
```

I provide the tag "mario-quesada" to differentiate this image from other with the same image name

## Deploy the contianer

To deploy the container use the next command:

```
docker run -d --restart unless-stopped -p 8888:8888 --name power_plant_production power_plant_production:mario-quesada
```

The container will be executed in background, to stop and kill it use:

```
docker stop power_plant_production
docker rm power_plant_production
```
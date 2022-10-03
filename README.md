# MultiServices in Parallelism

This webApps was made for communicated multiple clients with a custom developent made in [VVVV](https://vvvv.org/) who made real time data representation. 

## Backend 
Is made in python and run multiple services like UDP, Websocket, Flask and the database is Mongo. 

## EndPoint Flask
We have two endpoint:
+ /data: is use it for update the data base with new values, in that moment our server send the data through websocket to VVVV.
```bash
10.90.125.20:5000/data PUT
```
+ /jugadores: history of the total numbers of players base on days, moths and forever. 
```bash
10.90.125.20:5000/jugadores GET 
```

## Setup
+ For run the example you need docker and docker-compose. 
```docker
docker volume create munabidb 
```
```docker
docker build -t munabiservidor .
```
```docker
docker-compose up
```

## FlowChart
![image](https://i.ibb.co/pvCwmhB/Sharding-Database.jpg)
## Video Test
[![Alt text for your video](https://i.ytimg.com/vi/88Bb6BEX9Ng/frame0.jpg)](https://www.youtube.com/shorts/88Bb6BEX9Ng)

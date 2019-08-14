# view omdb movies #

### Clone github link
 git clone https://github.com/avnibarad/viewomdb.git

### Go to the directory viewomdb
 cd viewomdb/

### Now build docker image from Dockerfile
 docker image build -t viewomdb .

### run the container by passing movie name as an argumnet
 docker run -it viewomdb the lion king

### Output
 Movie name: the lion king
 Rotten Tomatoes Ratings: 93%

### Error handled
 1) No movie name passed
 2) Connection error
 3) Movie name is not present
 4) Rating not available
 5) Rotten tomatoes rating not available
 6) Apikey is incorrect

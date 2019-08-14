import requests, json, sys
from requests.exceptions import ConnectionError
if len(sys.argv)>1:
        movie=" ".join(sys.argv[1:])
        url='https://www.omdbapi.com/'
        movie_title=sys.argv[1:]
        try:
                para=dict(t=movie_title,apikey='b1b6806f')
                resp = requests.get(url=url, params=para).json()
                print('Movie name: '+movie)
                ratings_list=resp['Ratings']
                print(ratings_list)
                if len(ratings_list)>0:
                        data=list(filter(lambda rating: rating['Source']=='Rotten Tomatoes',ratings_list))
                        if len(data)==0:
                                print ('Rotten Tomatoes Ratings not available')
                                print('Displaying other ratings:')
                                for x in range(0,len(ratings_list)):
                                        print(ratings_list[x]['Source'] + ': '+ ratings_list[x]['Value'])
                        else:
                                print ('Rotten Tomatoes Ratings: '+ data[0]['Value'])
                else:
                        raise Exception('no Ratings Available for '+ movie)
        except ConnectionError as e:
                print(e)
                print('Either Url is not working or incorrect Url')
        except ValueError:
                print('Either Url is not working or incorrect Url')
        except KeyError:
                print(resp['Error'])

else:
        raise Exception('Please pass argument as a movie name')

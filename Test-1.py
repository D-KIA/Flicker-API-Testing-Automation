import requests

#This Funcion gives us status
def get_api(url):
    try:
        re = requests.get(url)

        #Response
        status = re.status_code
        response = re.json()
        if status == 200 and response['stat'] == 'ok':
            print('Response Successful')
            print('Response:-\n', response)
        else:
            print('Response Unsuccessful')
            print('Error:-\n', response['message'])
    except Exception as e:
        print(e)

#API url and Parameters
url = 'https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=aa468907ab3ac71a0a92d06186a359c1&user_id=196294394%40N08&format=json&nojsoncallback=1'

get_api(url)

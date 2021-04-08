import json
import requests


def get_data():
    url = 'https://movie.douban.com/j/search_subjects?' \
          'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

    response = requests.get(url, headers=headers)  # 请求json接口的整体数据

    print(response.text)
    data = response.text
    python_data = json.loads(response.text)  # json.loads将已编码的 JSON 字符串解码为 Python 对象
    print(python_data)
    result = []
    subjects = python_data['subjects']
    # print(subjects)
    i = 1
    for movie in subjects:
        # response1 = requests.get(movie['url'], headers)
        # print(response1.text)
        print('id:%d' % i, '电影名字:%s' % movie['title'], '评分:%s' % movie['rate'], 'url:%s' % movie['url'])
        i += 1
    # item = {'电影名称': movie['tittle']}
    # print(movie)

    # row = {
    #     'movie_rate': movie['rate'],
    #     'movie_name': movie['title'],
    #     'movie_url' : movie['url']
    # }
    # result.append(row)
    return result


if __name__ == '__main__':
    get_data()

from multiprocessing.dummy import Pool
import requests
import json


def get_goat_id(sku:str):
    url="https://www.goat.com/_next/data/LL2Qxgxoy1-tZTq_s-tHy/en-US/search.json?query="+sku
    while True:
        res=requests.get(url)
        if res.status_code==200:
            res=json.loads(res.text)
            try:
                id=res["pageProps"]["constructorResponse"]["response"]["results"][0]["data"]['slug']
                return id
            except:
                return(None)
        else:
            print('获取错误正在重试')
    pass

def get_goat_price(id:str,):
    url=f"https://www.goat.com/_next/data/LL2Qxgxoy1-tZTq_s-tHy/en-US/sneakers/{id}.json"
    while True:
        res=requests.get(url=url)
        if res.status_code==200:
            break
        else:
            print('获取错误正在重试')
    res=json.loads(res.text)
    price_list=res['pageProps']['offers']['offerData']
    brand=res['pageProps']['productTemplate']['brandName']
    gender=res['pageProps']['productTemplate']['gender'][0]
    print(price_list,brand,gender)
    pass 
        
def search_goat(sku:str):
    id=get_goat_id(sku)
    data=get_goat_price(id:str)

if __name__ == '__main__':
    pool = Pool(2)  #异步线程数
    pool.map(search_goat, sku_list)    
    #这里你需要将货号作为一个可迭代对象导入作为search_goat函数的参数




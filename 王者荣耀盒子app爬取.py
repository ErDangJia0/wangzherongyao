import requests
import json
base_url='http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.4.0&version_code=13040&cuid=EF8A5B70F25AE4BE0784DF6EA5C06864&ovr=8.0.0&device=Xiaomi_MI+5&net_type=1&client_id=VBGDasAdZHyEdvsEedfTOA%3D%3D&info_ms=ch5jX8N3W1S1CmjiyGNeJw%3D%3D&info_ma=eDsQOJp%2B5ldnzjTeK6%2FOWOBqSiTqaX6CRyzTr79zE5o%3D&mno=0&info_la=cWig7mExEWqcnez%2BkMOg%2BA%3D%3D&info_ci=cWig7mExEWqcnez%2BkMOg%2BA%3D%3D&mcc=0&clientversion=13.0.4.0&bssid=uM%2FOLc77BcbvhQflRWIWdl4xByQbN9hx4zOA3qoOEdY%3D&os_level=26&os_id=c1459e9d58676052&resolution=1080_1920&dpi=480&client_ip=192.168.1.5&pdunid=221f67b9'
res=requests.get(base_url)
res.encoding="utf-8"
wList=json.loads(res.text)['list']
for l in wList:
    url=l['cover']
    print(url)
    res=requests.get(url)
    data=res.content
    filename=l['name']+".jpg"
    with open('image/'+filename,"wb") as f:
        f.write(data)
    print(l['name']+'图片保存成功')
print("图片保存完毕")

        
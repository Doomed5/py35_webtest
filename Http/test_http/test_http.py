import requests

class TestHttp:
    def test_get(self):
        r = requests.get('https://httpbin.ceshiren.com/get',params={'a':1,'b':2})

        print(r.status_code)
        print(r.encoding)
        print(r.content)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        r = requests.post('https://httpbin.ceshiren.com/post',data={'custtel':15600534760})
        print(r.text)
        print(r.json())
        assert r.status_code == 200
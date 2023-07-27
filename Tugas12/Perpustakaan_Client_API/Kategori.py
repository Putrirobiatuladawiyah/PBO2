import requests
import json
class Kategori:
    def __init__(self):
        self.__id=None
        self.__kodekategori = None
        self.__nama_kategori = None
        self.__judulbuku = None
        self.__url = "http://localhost/perpustakaan/kategori_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodekategori(self):
        return self.__kodekategori
        
    @kodekategori.setter
    def kodekategori(self, value):
        self.__kodekategori = value
    @property
    def nama_kategori(self):
        return self.__nama_kategori
        
    @nama_kategori.setter
    def nama_kategori(self, value):
        self.__nama_kategori = value
    @property
    def judulbuku(self):
        return self.__judulbuku
        
    @judulbuku.setter
    def judulbuku(self, value):
        self.__judulbuku = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodekategori(self, kodekategori):
        url = self.__url+"?kodekategori="+kodekategori
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idkategori']
            self.__kodekategori = item['kodekategori']
            self.__nama_kategori = item['nama_kategori']
            self.__judulbuku = item['judulbuku']
        return data
    def simpan(self):
        payload = {
            "kodekategori":self.__kodekategori,
            "nama_kategori":self.__nama_kategori,
            "judulbuku":self.__judulbuku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodekategori(self, kodekategori):
        url = self.__url+"?kodekategori="+kodekategori
        payload = {
            "kodekategori":self.__kodekategori,
            "nama_kategori":self.__nama_kategori,
            "judulbuku":self.__judulbuku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodekategori(self,kodekategori):
        url = self.__url+"?kodekategori="+kodekategori
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text

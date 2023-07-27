import requests
import json
class Pinjam:
    def __init__(self):
        self.__id=None
        self.__nomorbukti = None
        self.__tglpinjam = None
        self.__kodeanggota = None
        self.__kodebuku1 = None
        self.__kodebuku2 = None
        self.__tglhrskembali = None
        self.__tgldikembalikan = None
        self.__statuspinjam = None
        self.__denda = None
        self.__url = "http://localhost/perpustakaan/pinjam_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nomorbukti(self):
        return self.__nomorbukti
        
    @nomorbukti.setter
    def nomorbukti(self, value):
        self.__nomorbukti = value
    @property
    def tglpinjam(self):
        return self.__tglpinjam
        
    @tglpinjam.setter
    def tglpinjam(self, value):
        self.__tglpinjam = value
    @property
    def kodeanggota(self):
        return self.__kodeanggota
        
    @kodeanggota.setter
    def kodeanggota(self, value):
        self.__kodeanggota = value
    @property
    def kodebuku1(self):
        return self.__kodebuku1
        
    @kodebuku1.setter
    def kodebuku1(self, value):
        self.__kodebuku1 = value
    @property
    def kodebuku2(self):
        return self.__kodebuku2
        
    @kodebuku2.setter
    def kodebuku2(self, value):
        self.__kodebuku2 = value
    @property
    def tglhrskembali(self):
        return self.__tglhrskembali
        
    @tglhrskembali.setter
    def tglhrskembali(self, value):
        self.__tglhrskembali = value
    @property
    def tgldikembalikan(self):
        return self.__tgldikembalikan
        
    @tgldikembalikan.setter
    def tgldikembalikan(self, value):
        self.__tgldikembalikan = value
    @property
    def statuspinjam(self):
        return self.__statuspinjam
        
    @statuspinjam.setter
    def statuspinjam(self, value):
        self.__statuspinjam = value
    @property
    def denda(self):
        return self.__denda
        
    @denda.setter
    def denda(self, value):
        self.__denda = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nomorbukti(self, nomorbukti):
        url = self.__url+"?nomorbukti="+nomorbukti
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idpinjam']
            self.__nomorbukti = item['nomorbukti']
            self.__tglpinjam = item['tglpinjam']
            self.__kodeanggota = item['kodeanggota']
            self.__kodebuku1 = item['kodebuku1']
            self.__kodebuku2 = item['kodebuku2']
            self.__tglhrskembali = item['tglhrskembali']
            self.__tgldikembalikan = item['tgldikembalikan']
            self.__statuspinjam = item['statuspinjam']
            self.__denda = item['denda']
        return data
    def simpan(self):
        payload = {
            "nomorbukti":self.__nomorbukti,
            "tglpinjam":self.__tglpinjam,
            "kodeanggota":self.__kodeanggota,
            "kodebuku1":self.__kodebuku1,
            "kodebuku2":self.__kodebuku2,
            "tglhrskembali":self.__tglhrskembali,
            "tgldikembalikan":self.__tgldikembalikan,
            "statuspinjam":self.__statuspinjam,
            "denda":self.__denda
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nomorbukti(self, nomorbukti):
        url = self.__url+"?nomorbukti="+nomorbukti
        payload = {
            "nomorbukti":self.__nomorbukti,
            "tglpinjam":self.__tglpinjam,
            "kodeanggota":self.__kodeanggota,
            "kodebuku1":self.__kodebuku1,
            "kodebuku2":self.__kodebuku2,
            "tglhrskembali":self.__tglhrskembali,
            "tgldikembalikan":self.__tgldikembalikan,
            "statuspinjam":self.__statuspinjam,
            "denda":self.__denda
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nomorbukti(self, nomorbukti):
        url = self.__url+"?nomorbukti="+nomorbukti
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers) 
        return response.text

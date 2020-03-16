from bs4 import BeautifulSoup
import requests
class Anime:
    def __init__(self,AnimeName):
        Anime_Name = AnimeName.replace(' ', '+')
        search = f'https://www.okanime.com/search/autocomplete?term={Anime_Name}'

        req = requests.get(search)
        value = req.json()
        try:
            value[0]
        except Exception:
            raise Exception("Anime Not Found")
        self.url = f"https://www.okanime.com{value[0]['redirection']}"
        req2 = requests.get(self.url).text
        soup = BeautifulSoup(req2, 'html.parser')

        try:
            self.search = [i for i in value]
        except Exception:
            self.search = (None)
        try:
            genre = soup.find(class_="col-md-8 no-padding-right text-right ltr_direction")
            genre = genre.find(class_='row genres').text
            self.genre = ' , '.join(map(str,genre.split()))
        except Exception:
            self.genre = (None)
        try:
            cover = soup.find(class_="col-md-3 col-md-offset-1 no-padding-left text-center cover").img['src']
            self.cover = f'https://www.okanime.com{cover}'
            try:
                req = requests.get(self.cover)
            except Exception:
                self.cover = cover
        except Exception:
            self.cover = (None)
        info = soup.find(class_="col-md-8 no-padding-right text-right ltr_direction")
        info = info.find_all(class_='col-md-1 pull-right')

        try:
            self.status = (info[1].text.split()[0])
        except Exception:
            self.status = (None)
        try:
            self.year = (info[0].text.split()[0])
        except Exception:
            self.year = (None)
        try:
            episodes = soup.find(class_="col-md-2 pull-right")
            self.episodes = (episodes.text.split()[0])
        except Exception:
            self.episodes = (None)
        try:
            self.age_classification = (info[2].text.split()[0])
        except Exception:
            self.age_classification = (None)
        try:
            rate = soup.find(class_="col-md-8 no-padding-right text-right ltr_direction")
            rate = rate.find(class_='ribbon pull-right average-rating')
            vote = soup.find(class_='col-md-3 col-md-offset-1 no-padding-left text-center cover')
            self.rate = f'{rate.text.split()[0]} {vote.p.text}'
        except Exception:
            self.rate = (None)

        try:
            description = soup.find_all(class_='col-md-12')
            self.description = (description[1].p.text)
        except Exception:
             self.description = (None)
        try:
            self.trailer = soup.find(class_="btn btn-block btn-trailer")['href']
        except Exception:
            self.trailer = (None)
        try:
            studio = soup.find_all(class_='col-md-2 pull-right')
            self.studio = (studio[1].find_all('a')[1].text)
        except Exception:
            self.studio = (None)
        try:
            director = soup.find_all(class_='col-md-2 pull-right')
            self.director = (director[2].a.text)
        except Exception:
            self.director=(None)
        try:
            title = soup.find_all(class_='latin')
            self.title = title[1].text
        except Exception:
            self.title=(None)
    def favorite_anime(self,yourname):
        r2 = requests.get(f'https://www.okanime.com/profiles/{yourname}#favorite').text
        soup = BeautifulSoup(r2, 'html.parser')
        find = soup.find_all(class_='info-box')
        val = '\n'.join(map(str, [i.text.replace('\n', '') for i in find]))
        return val

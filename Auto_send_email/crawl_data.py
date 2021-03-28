import requests
from bs4 import BeautifulSoup


class TrungTamDayKem_Scrapy:
    def __init__(self):
        self.response = requests.get('https://www.trungtamdaykem.com/lop-day-hien-co-dang-list.html')
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.table = self.soup.select("#main-content-3col > div > div.panel-body > table > tr")
        self.table.pop(0)

    def find_courses(self, loc=None, gen=None, return_dict=False):
        matched_courses = {'location': loc, 'gender': gen, 'courses': []}
        for row in self.table:
            info = row.select('td')
            code = info[0].text
            subject = info[1].strong.text
            time = info[1].span.text
            location = info[2].text
            tutor_gender = info[6].text
            if loc not in location:
                continue
            if gen not in tutor_gender:
                continue
            temp_dict = {'code': code, 'subject': subject, 'time': time, 'location': location}
            matched_courses['courses'].append(temp_dict.copy())
        if return_dict:
            return matched_courses
        else:
            return ''.join([f'{code} || {subject} \n{time} \n{location} \n\n' for course in matched_courses['courses']])

if __name__ == '__main__':
    result = TrungTamDayKem_Scrapy()
    print(result.find_courses(loc="Thủ Đức", gen="Sinh viên Nam"))
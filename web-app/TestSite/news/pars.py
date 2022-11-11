import requests
from bs4 import BeautifulSoup as bs

from .models import Articles




def CreateState():
    URL_TEMPLATE = "http://www.origins.org.ua/category/?id=53"
    r = requests.get(URL_TEMPLATE)
    content = r.content.decode('utf-8')

    soup = bs(content, 'lxml')

    states = soup.find_all('a', class_='stories-item')
    state_href_index_list = []

    count_for_i = 1
    for state in states:
        state_href = state.get('href')
        state_href_index = state_href[-4:]
        if state_href_index[-4] == '=':
            state_href_index_list.append(state_href_index[-3:])
        else:
            state_href_index_list.append(state_href_index)
    print(state_href_index_list)
    break_for = 0
    for i in state_href_index_list:
        # if break_for == 1:
        #     break
        print(f"http://www.origins.org.ua/page.php?id_story={i} Статья №{count_for_i}")
            #
        r = requests.get(f"http://www.origins.org.ua/page.php?id_story={i}")
        content = r.content.decode('utf-8')
        download_soup = bs(content, 'lxml')

        state_h1 = download_soup.find('h1')


        full_text = download_soup.find('div', class_='story-text page-story-text')
        resault_text = ''
        for text in full_text:
            if 'img' in str(text) or '<h2>Ссылки</h2>' in str(text) or '<a href="author?' in str(text) or '<a class="author"' in str(text) or '<!--' in str(text) or '<i>' in str(text) or 'blue' in str(text):
                pass
            else:
                resault_text += str(text)
        resault_text = '<div class="resault_pars_text">' + resault_text + '</div>'










        #     # print(state_h1.text)
        #     # print(count_for_i)
        #     #
        #     # os.chdir("pars_img_education")
        #     # if not os.path.isdir("folder"):
        #     #     os.makedirs(str(count_for_i))
        #     # os.chdir("..")
        #     #
        #     # with open(f'pars_img_education/{count_for_i}/Заголовок к №{count_for_i}.txt', 'w', encoding='utf-8') as f:
        #     #     f.write(state_h1.text)
        #     #
        # state_all_p = download_soup.find_all('p', class_='text')
        # full_text = ''
        # for p in state_all_p:
        #     full_text += p.text
        #     # print(full_text)
        #     #
        #     # with open(f'pars_img_education/{count_for_i}/Текст к №{count_for_i}.txt', 'w', encoding='utf-8') as f:
        #     #     f.write(full_text)
        #     #
        try:
            state_img_url = download_soup.find('img').get('src')
            full = requests.get(f"http://www.origins.org.ua/{state_img_url}").content
            image_name = str.split(state_img_url, '/')[-1]
            with open(f'media/images/pictures/{image_name}', 'wb') as f:
                f.write(full)
            img = f'images/{state_img_url}'
        except:
            img = ''
        #
        Articles.objects.create(title=state_h1.text, img=img, full_text=resault_text, categories_id=16, creater_id='1', creater_username='admin')
        count_for_i += 1
        break_for += 1

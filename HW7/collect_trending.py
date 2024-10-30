import requests
import bs4
import json
import argparse

def do(json_filename):
    url = 'https://montrealgazette.com'

    headers = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)

    with open('gazettte.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # with open('gazettte.html', 'r', encoding='utf-8') as file:
    #     soup = bs4.BeautifulSoup(file.read(), 'html.parser')

        
    upper_left_of_page = soup.find(class_="row row--xl list divider--right--lg-up")

    if upper_left_of_page:
        #articles = upper_left_of_page.find_all(attrs={"class":'article-card__headline-clamp'})
        articles = upper_left_of_page.find_all('a')

    newurls = []
    for individual_article in articles:
        link = individual_article['href']
        if link not in newurls and link[0:9] != '/category':
            newurls.append(link)

    article_data = []
    for link in newurls:
        print('https://montrealgazette.com' + link)
        response = requests.get('https://montrealgazette.com'+link, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        #TITLE
        title = soup.find('h1').get_text()
        print(title)
        #PUBLICATION DATE
        date = (soup.find(class_='published-date__since')).get_text()
        print(date)
        #AUTHOR
        auth = soup.find(class_='published-by__author').get_text()
        print(auth)
        #BLURB
        blurb = soup.find(class_='article-subtitle').get_text()
        print(blurb)

        article_data.append({
            "title": title,
            "publication_date": date,
            "author": auth,
            "blurb": blurb
        })

    with open('trending.json', 'w') as file:
        json.dump(article_data, file, indent=4)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Collect trending articles and save to a JSON file.")
    parser.add_argument('-o', '--output', type=str, default='articles.json', help='Output JSON file name')
    args = parser.parse_args()
    do(args.output)



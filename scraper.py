import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
# base_url='https://www.amazon.in/Apple-iPhone-13-128GB-Product/product-reviews/B09G99CW2N/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='
def scrape(base_url:str):

    review_list=[]
    for i in range(1, 11):
        url=base_url+f'{i}'
        print(url)
        try:
            time.sleep(3)
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                soup=BeautifulSoup(response.content,'html.parser')
                review_div=soup.find('div',{'id':'cm_cr-review_list'})
                reviews=review_div.find_all('div', {'data-hook':'review'})
                for rev in reviews:
                    author=rev.find('div',{'class':'a-profile-content'})
                    title=rev.find('a', {'data-hook':'review-title'})
                    description=rev.find('div', {'class':'a-row a-spacing-small review-data'})
                    span=rev.find('div', {'class': 'a-row a-spacing-mini review-data review-format-strip'})
                    if span:
                    # Extract color and size from the text content of the span
                        text_content = span.get_text(strip=True)
                    # Split the text based on the separator (assuming it's a colon in this case)
                        parts = re.findall('[A-Z][^A-Z]*', text_content)
                    # Extract color and size
                        if len(parts)==7:
                            color = parts[1].strip() if len(parts) > 1 else None
                            siz=parts[2:5]
                            siz=''.join(siz)
                            size=siz.split(':')
                            size = size[1]
                    verified_purchase=rev.find('span', {'data-hook':'avp-badge'})
                    if verified_purchase.text:
                        verified='yes'
                    else:
                        verified='no'
            
                    date=rev.find('span',{'data-hook':'review-date'})
                    
                    review_list.append({
                        'url':url,
                        'author':author.text,
                        'title':title.text,
                        'description':description.text,
                        'color':color,
                        'size':size,
                        'is_verified':verified,
                        'date':date.text})
        except Exception as err:
            print(err)
    df=pd.DataFrame(review_list)
    df.to_csv('review_list.csv', index=False)
import time
import pandas as pd
from comment_scraper import AmazonScraper

reviews = []
amz_scraper = AmazonScraper()

product_url = 'https://www.amazon.com/Big-Book-Dashboards-Visualizing-Real-World/product-reviews/1119282713/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2'

for page_num in range(2, 6):
    reviews.extend(amz_scraper.scrapeReviews(
        url=product_url, page_num=page_num))
    time.sleep(1)

df = pd.DataFrame(reviews)
df.to_excel('amazon product review ({0}).xlsx'.format(
    reviews[0].product_name), index=False)

import re
from collections import namedtuple
import requests
from bs4 import BeautifulSoup

UserReview = namedtuple('UserReview', ['product_name', 'review_title', 'comment',
                        'rating', 'date', 'username', 'profile_url', 'verified_purchase'])

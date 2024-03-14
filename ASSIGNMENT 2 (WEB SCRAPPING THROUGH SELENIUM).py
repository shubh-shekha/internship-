#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# now we will download the webdriver for the webbrowser
# 
# check the version of your browser
# go to the link https://chromedriver.chromium.org/downloads download the webdriver for your version of your browser

# In[7]:


browser = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1) \chromedriver.exe")


# In[8]:


browser.get("https://www.naukri.com/")


# In[10]:


designation = browser.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[ ]:


location = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[11]:


search = browser.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[12]:


job_title = []
job_location = []
company_name = []
experience_required = []


# In[13]:


title_tags = browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[14]:


location_tags = browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[15]:


company_tags = browser.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)


# In[16]:


experience_tags = browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    experience = i.text
    experience_required.append(experience)


# In[17]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[18]:


import pandas as pd
df = pd.DataFrame({'Job_title':job_title,'Job_location':job_location,'company_name':company_name,'experience_required':experience_required})
df


# In[20]:


url = browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
url[0:4]


# In[22]:


for i in url[0:4]:
    print(i.get_attribute('href'))


# In[23]:


job_titles = []


# In[24]:


start=0
end=2
for page in range(start,end):
    titles= browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
    for i in titles:
        job_titles.append(i.text)
    next_button = browser.find_element(By.XPATH,'//a[@class="fright fs14 btn-secondary br2"]')
    next_button.click()
    time.sleep(3)


# In[25]:


len(job_titles)


# In[26]:


job_titles


# # question 2

# In[27]:


browser = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1) \chromedriver.exe")


# In[28]:


browser.get("https://www.naukri.com/")


# In[29]:


designation = browser.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[30]:


location = browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[31]:


search = browser.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[32]:


job_title = []
job_location = []
company_name = []


# In[33]:


title_tags = browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[34]:


location_tags = browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[35]:


company_tags = browser.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)


# In[36]:


print(len(job_title),len(job_location),len(company_name))


# In[37]:


import pandas as pd
df1 = pd.DataFrame({'Job_title':job_title,'Job_location':job_location,'company_name':company_name})
df1


# # question 3

# In[38]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[39]:


driver = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1) \chromedriver.exe")


# In[40]:


driver.get("https://www.naukri.com/")


# In[42]:


designation = driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[44]:


search = driver.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[45]:


loc_filter=driver.find_elements(By.XPATH,'//div[@class="mt-8 chckBoxCont"]')


for i in loc_filter :
    if (i.text=='Delhi / NCR'):
        i.click()
        break


# In[46]:


sal_filter=driver.find_elements(By.XPATH,'//div[@class="mt-8 chckBoxCont"]')
for i in sal_filter:
    if(i.text=='3-6 Lakhs'):
        i.click()
        break


# In[47]:


job_title = []
job_location = []
company_name = []
experience_required = []


# In[48]:


title_tags = driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title = i.text
    job_title.append(title)


# In[49]:


location_tags = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location = i.text
    job_location.append(location)


# In[50]:


company_tags = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company = i.text
    company_name.append(company)


# In[51]:


experience_tags = driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 expwdth"]')
for i in experience_tags[0:10]:
    experience = i.text
    experience_required.append(experience)


# In[52]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[53]:


import pandas as pd
df2 = pd.DataFrame({'Job_title':job_title,'Job_location':job_location,'company_name':company_name,'experience_required':experience_required})
df2


# # question 4

# In[65]:


driver = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1) \chromedriver.exe")


# In[66]:


driver.get(" https://www.flipkart.com/")


# In[69]:


search_product = driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search_product.send_keys("sunglasses")


# In[70]:


search_btn = driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_btn.click


# In[71]:


brand_tit = []
product_tit = []
price_tit = []
discount_tit = []


# In[77]:


brand_title = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_title[0:100]:
    brand= i.text
    brand_tit.append(brand)


# In[86]:


product_title = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_title[0:100]:
    product = i.text
    product_tit.append(product)


# In[97]:


price_title = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_title[0:100]:
    price = i.text
    price_tit.append(price)


# In[80]:


discount_title =  driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
for i in discount_title[0:100]:
    discount = i.text
    discount_tit.append(discount)


# In[81]:


brand_tit


# In[87]:


product_tit


# In[98]:


price_tit


# In[95]:


discount_tit


# # question 5

# In[96]:


ratings = []
reviews = []
review_summary = []


# In[102]:


ratings_title = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK"]')
for i in ratings_title[0:10]:
    title = i.text
    ratings.append(title)


# In[ ]:


reviews_titles = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in reviews_titles[0:10]:
    reviews_titles =i.text
    reviews_titles.append(review)


# In[107]:


summary_title = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in summary_title[0:10]:
    title = i.text
    review_summary.append(title)


# In[113]:


print(len(ratings),len(reviews),len(review_summary))


# In[ ]:


df5 = pd.DataFrame({'reviews_titles':reviews,'review_summary':review_summary})
df5


# In[ ]:


df6 = [{'ratings':ratings}]
df6


# # question 6

# In[117]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[118]:


driver = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1) \chromedriver.exe")


# In[119]:


driver.get("https://www.flipkart.com/")


# In[120]:


search_product = driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search_product.send_keys("sneakers")


# In[121]:


search_btn = driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_btn.click()


# In[122]:


brand_name = []
product_description = []
price_val = []


# In[144]:


brand_title =  driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_title[0:200]:
    brand= i.text
    brand_name.append(brand)


# In[146]:


product_title= driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_title[0:200]:
    product = i.text
    product_description.append(i.text)
    
    
    
    


# In[147]:


price_tag = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tag[0:200]:
    price = i.text
    price_val.append(price)


# In[148]:


print(len(brand_name),len(product_description),len(price_val))


# In[130]:


import pandas as pd


# In[150]:


df6 = pd.DataFrame({"brand_name":brand_name})
df6


# In[151]:


df7 = pd.DataFrame({"product_description":product_description})
df7


# In[152]:


df8 = pd.DataFrame({"price_val":price_val})
df8


# # question 7

# In[154]:


driver = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[155]:


driver.get("https://www.amazon.in/")


# In[159]:


designation = driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
designation.send_keys('Laptop')


# In[157]:


search = driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search.click()


# In[160]:


filter1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul[6]/li[10]/span/a/span')
filter1.click


# In[161]:


lap_title = []
lap_rating = []
lap_price = []


# In[163]:


laptop_title = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in laptop_title[0:10]:
    laptop = i.text
    lap_title.append(laptop)


# In[164]:


laptop_rating = driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')
for i in laptop_rating[0:10]:
    laptop = i.text
    lap_rating.append(laptop)


# In[165]:


laptop_price =driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in laptop_price[0:10]:
    laptop = i.text
    lap_price.append(laptop)


# In[166]:


print(len(lap_title),len(lap_rating),len(lap_price))


# In[168]:


df9 = pd.DataFrame({'title':lap_title,})
df9


# In[170]:


df10= pd.DataFrame({'rating':lap_rating,'price':lap_price})
df10


# # question 8

# In[171]:


driver = webdriver.Chrome(r"C:\Users\MAYANK\Downloads\chromedriver_win32 (1)\chromedriver.exe")


# In[172]:


driver.get("https://www.azquotes.com/")


# In[173]:


designation = driver.find_element(By.XPATH,'//input[@class="ui-autocomplete-input"]')
designation.send_keys('TOP 100 Quotes')


# In[175]:


top = driver.find_element(By.XPATH,'//a[@class="collapse"]')
top.click()


# In[176]:


Quote_title = []
Author_name = []
Quotes_type = []


# In[177]:


title_tags = driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in title_tags[0:100]:
    title = i.text
    Quote_title.append(title)


# In[178]:


author_tags = driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in author_tags[0:100]:
    author = i.text
    Author_name.append(author)


# In[179]:


quote_tags = driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in quote_tags[0:100]:
    quote= i.text
    Quotes_type.append(quote)


# In[180]:


print(len(Quote_title),len(Author_name),len(Quotes_type))


# In[181]:


df12 = pd.DataFrame({'title':Quote_title,'author':Author_name,'type':Quotes_type})
df12


# In[ ]:





---

# **Shopclue Spider**

## **Description**  
**Shopclue Spider** is a **Scrapy-based web scraper** designed to extract product data from [Shopclues](https://www.shopclues.com) categories. The project effectively bypasses AJAX requests to collect detailed information about products, sellers, and their ratings.

---

## **Features**  
- Scrapes detailed product information, including:  
  - Product name  
  - Brand  
  - Price  
  - Average rating and number of reviews  
  - Seller name and location  
  - Seller store link  
- Handles pagination to automatically scrape all pages of a category.  
- Bypasses AJAX calls to directly collect data from the HTML pages.  

---

## **Requirements**  
- **Python**: Version 3.7 or higher  
- **Required libraries**:  
  - `scrapy`  

### **Installing Dependencies**  
Use the following command to install the required libraries:  
```bash
pip install scrapy
```

---

## **Usage**

### **Clone the Repository**  
Run the following commands to clone the repository:  
```bash
git clone https://github.com/yourusername/shopclue-spider.git
cd shopclue-spider
```

### **Run the Spider**  
To start scraping, execute the following command:  
```bash
scrapy crawl shopclueSpider -o output.csv
```  
This will generate a CSV file (`output.csv`) containing the extracted data.

---

## **Extracted Data Structure**  
The extracted data will include the following fields:  
- **name**: Product name.  
- **brand**: Brand of the product.  
- **price**: Product price (in ₹).  
- **rating_value**: Average rating of the product.  
- **rating_count**: Total number of ratings.  
- **total_reviews**: Total number of textual reviews available.  
- **seller_name**: Name of the seller.  
- **seller_location**: Seller's location.  
- **seller_store_link**: Link to the seller's store.  
- **seller_ratings**: Seller's average rating.  
- **seller_reviews**: Number of reviews for the seller.  

---

## **Technical Highlights**  
- **Scrapy Selector**: Uses CSS selectors to precisely extract data.  
- **Dynamic Pagination**: Automatically detects and follows the next pages.  
- **Data Cleaning**: Ensures clean output by preprocessing extracted fields.  

---

## **Customization**  
To scrape a different category, modify the `start_urls` variable in the spider file as shown below:  
```python
start_urls = ["https://www.shopclues.com/womens-western-wear-tops.html?page=1"]
```

---

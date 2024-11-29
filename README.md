# Shopclue Spider  

## 📖 **Overview**  
**Shopclue Spider** is a powerful web scraping tool built with [Scrapy](https://scrapy.org). This project extracts comprehensive product information from various categories on [Shopclues](https://www.shopclues.com), bypassing AJAX calls to deliver clean and structured data. It efficiently scrapes product details, seller information, ratings, and reviews while handling pagination dynamically.  

---

## 🚀 **Features**  
- Extracts detailed product information, including:  
  - **Product name**  
  - **Brand**  
  - **Price**  
  - **Average rating** and **number of reviews**  
  - **Seller name**, **location**, and **store link**  
- Handles pagination to scrape all pages in a category automatically.  
- Effectively bypasses AJAX requests to extract data directly from HTML pages.  

---

## 📋 **Requirements**  
To use this project, ensure the following dependencies are installed:  

- **Python**: Version 3.7+  
- **Python Libraries**:  
  - `scrapy`  

### 🛠️ **Installing Dependencies**  
Install the required libraries by running:  
```bash
pip install scrapy
```

---

## 📂 **Usage**  

### **1. Clone the Repository**  
Clone the repository and navigate into the project directory:  
```bash
git clone https://github.com/yourusername/shopclue-spider.git
cd shopclue-spider
```

### **2. Run the Spider**  
Execute the following command to start scraping:  
```bash
scrapy crawl shopclueSpider -o output.csv
```  
This will generate a file named `output.csv` containing the extracted data.  

---

## 📊 **Extracted Data Structure**  
The scraped data will include the following fields:  
| Field             | Description                                  |  
|--------------------|----------------------------------------------|  
| **name**          | Product name                                |  
| **brand**         | Brand of the product                        |  
| **price**         | Product price (in ₹)                        |  
| **rating_value**  | Average rating of the product               |  
| **rating_count**  | Total number of ratings                     |  
| **total_reviews** | Total number of textual reviews available   |  
| **seller_name**   | Name of the seller                          |  
| **seller_location**| Seller's location                          |  
| **seller_store_link** | Link to the seller's store              |  
| **seller_ratings**| Seller's average rating                     |  
| **seller_reviews**| Number of reviews for the seller            |  

---

## 🛠️ **Technical Highlights**  
- **Scrapy Selectors**: Utilizes CSS selectors to extract specific elements with precision.  
- **Dynamic Pagination**: Automatically detects and scrapes data across all category pages.  
- **Data Cleaning**: Extracted fields are preprocessed to ensure clean and accurate outputs.  

---

## ✏️ **Customization**  
To scrape a different category, update the `start_urls` variable in the spider file:  
```python
start_urls = ["https://www.shopclues.com/womens-western-wear-tops.html?page=1"]
```  
Replace the URL with the category URL of your choice.  

---

## 📜 **License**  
This project is licensed under the MIT License. Feel free to use and modify it according to your needs.  

---
## 📧 **Contact**  
For any questions or feedback, reach out at: **djambomarcellin@gmail.com**  

---

With **Shopclue Spider**, you can efficiently gather detailed product data for analytics, market research, or business insights. Happy scraping! 🚀  

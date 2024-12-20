# IKEA Price Tracker

## Description
The IKEA Price Tracker is a simple application that allows users to monitor the price of a product listed on IKEA's website. Users can set a desired price threshold and get notified via email when the product's price drops below the specified value.

### Important Note on Passwords
After running the project, in the password field, use an app-generated password instead of providing your email account password directly. For example:
```text
Type password of sender's email ID: <your-app-generated-password>
```
This ensures better security for your email account.

### Why IKEA?
This project specifically targets IKEA's website because its webpage structure is consistent and easier to parse using web scraping techniques. In contrast, websites like Amazon often have dynamic or varying page structures, making it challenging to implement a generalized solution for all e-commerce platforms.

---

## Features
- **Real-Time Price Monitoring**: Continuously checks the product price at regular intervals.
- **Email Notifications**: Sends an email alert when the product price drops below the specified threshold.
- **User-Friendly Interface**: Built with Streamlit for a clean and interactive user experience.
- **Background Tracking**: Runs the price tracking process in the background without interrupting the application.

---
Feel free to customize

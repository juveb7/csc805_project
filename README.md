# CSC805 - Data Visualization

## Visualization Project: Shopping Trends and Customer Behavior

**Author(s):** Abdoulfatah Abdillahi, Jason Avina, Juvenal F Barajas, & Rustam Mukhtarov

## Introduction
The "Shopping Trends and Customer Behavior" project was developed under the guidance of Dr. Shah Rukh Humayoun in the subject CSC 805 - Data Visualization at San Francisco State University. Our team created an interactive web-based visualization system to explore and analyze shopping data, identifying patterns in customer behavior and product popularity.

This project utilizes a rich dataset from Kaggle, comprising various customer variables such as age, gender, and purchase amount across approximately 3900 records. The primary objective is to provide valuable insights for business organizations to improve and optimize product offerings, thereby enhancing customer satisfaction. Additionally, the system serves as an educational tool for individuals seeking to understand visualization techniques and consumer analytics.

Using Python with the Dash framework, alongside data manipulation libraries like Pandas and Plotly, we developed an application for dynamic data querying. This allows users to filter information by criteria such as age, gender, or product category, ensuring the information presented is relevant and useful.

This documentation details the structure, functions, and implementation of our visualization system, offering an exhaustive review from a technical perspective while highlighting practical applications and benefits.

## System Architecture
The system follows a client-server model where the client interacts via a web browser, and the server runs a Dash application in Python. The main components include:

**Frontend:** Developed with Dash and HTML/CSS for dynamic interactivity and styled presentation.

**Backend:** Python handles data processing using Pandas and creates visualizations with Plotly.

**Data Handling:** The application loads data from CSV files, processes it with Pandas, and prepares it for visualization.

## Dataset Description
The dataset contains comprehensive details on customer transactions, including geographic data for visualizing shopping trends. Key steps in data processing include:

**Data Grouping and Aggregation:** Grouping data by 'Location' and 'Item Purchased' to calculate statistics like count, average age, total amount spent, and most common size and color.

**Handling Missing Values:** Filling missing values in categorical data to maintain data integrity.

**Pivoting Data:** Structuring data with 'Location' as the index and 'Item Purchased' as columns.

**Flattening Multi-level Columns:** Simplifying data access and manipulation by flattening columns.
## System Description
User Interface
The UI is divided into sections dedicated to specific data visualizations:

**Data Summary:**Overview of the dataset.

**Interactive Map:** Visualizes geographic data.

**Product Insights:** Explore product ratings, popularity, and purchase frequency.

**Seasonal Purchase Amount By Item:** Displays seasonal spending on selected items.

**Customer Demographics:** Insights based on demographic filters.

## Interactivity
Interactivity is achieved through Dash callbacks, updating visualizations based on user input like sliders and dropdowns for dynamic data exploration.
## Technologies Used
**Dash and Plotly:** For interactive components and visualizations.

**Pandas:** For data manipulation.

**Python:** For overall system functionality including server-side logic.

**HTML/CSS:** For styling and layout enhancements.

## Result: 
<img width="943" alt="Screenshot 2024-05-16 at 11 48 18 AM" src="https://github.com/juveb7/csc805_project/assets/43047286/7db8911f-76cb-45f0-9547-6d586a6ca248">
<img width="959" alt="Screenshot 2024-05-16 at 11 49 06 AM" src="https://github.com/juveb7/csc805_project/assets/43047286/bfbdc171-7163-4043-bf48-4f878a9a1222">
<img width="961" alt="Screenshot 2024-05-16 at 11 49 36 AM" src="https://github.com/juveb7/csc805_project/assets/43047286/6df4d849-5800-4905-8724-07f9b8eaf8f7">
<img width="958" alt="Screenshot 2024-05-16 at 11 50 00 AM" src="https://github.com/juveb7/csc805_project/assets/43047286/8d76fe95-dbba-477a-899b-98a4376c2e23">
<img width="1046" alt="Screenshot 2024-05-16 at 11 50 25 AM" src="https://github.com/juveb7/csc805_project/assets/43047286/cf1f07f5-fb75-4595-b953-e16edc9e6b0c">

## Appendices
**Video link:** https://drive.google.com/file/d/1ppQ-6MG7N-lurU2zg-hh4dGNqpnsPPqm/view?usp=sharing

**Kaggle Dataset:** https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset/data













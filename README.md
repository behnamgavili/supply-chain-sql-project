# Supply Chain Performance Analysis using SQL and Python

## 📌 Project Overview

This project analyzes a simulated supply chain system using SQL and Python to evaluate operational performance across warehouses, delivery companies, and seller companies.

The objective is to identify inefficiencies, delivery delays, and cost–performance trade-offs within a logistics network.

---

## 🛠️ Tools Used

* Python
* SQLite
* Pandas
* Matplotlib

---

## 🗂️ Dataset Description

The project uses a relational database consisting of three tables:

### Warehouses

* warehouse_id
* warehouse_name
* city
* capacity

### Orders

* order_id
* product_name
* quantity
* warehouse_id
* seller_company
* order_date

### Deliveries

* delivery_id
* order_id
* delivery_company
* delivery_time
* delivery_cost
* delay_flag

---

## 📊 Key Metrics (KPIs)

* Total throughput (volume of processed items)
* Average delivery time
* Average delivery cost
* Delay rate (% of delayed deliveries)
* Daily throughput percentage

---

## 📈 Analysis Performed

The analysis includes:

* Delivery company performance evaluation
* Warehouse performance and workload analysis
* Seller company performance assessment
* Identification of high-risk (inefficient) orders
* Cost vs delay trade-off analysis

---

## 🔍 Key Insights

* **DHL demonstrates the best reliability**, with the lowest delay rate (33.33%) and fastest delivery times, making it the most efficient delivery provider in this dataset.

* **FedEx shows the weakest delivery performance**, with the highest delay rate (49.12%), indicating potential inefficiencies in operations.

* **Central Hub operates under the highest workload**, but also exhibits elevated delay rates and longer delivery times, suggesting possible congestion or capacity limitations.

* **North Hub shows the strongest operational efficiency**, combining low delay rates with fast delivery times despite handling moderate throughput.

* **East Hub presents relatively high delay rates despite moderate workload**, indicating inefficiencies that are not solely driven by capacity constraints.

* **SmartShop has the highest delay rate among seller companies (45.45%)**, suggesting weaker logistics outcomes compared to competitors.

* A positive relationship is observed between **warehouse workload (throughput)** and **delay rates**, highlighting the impact of operational pressure on service performance.

---

## 📊 Visualizations

The project includes:

* Delay rate by delivery company
* Average delivery time by warehouse
* Delivery cost vs delay rate (trade-off analysis)

---

## 📁 Project Structure

```
supply-chain-sql-project/
│
├── main.py          # Runs the full pipeline  
├── database.py      # Database creation and data generation  
├── analysis.py      # SQL queries and analysis functions  
├── README.md  
└── supply_chain.db  
```

---

## 🚀 How to Run the Project

1. Clone the repository
2. Run:

```bash
python main.py
```

3. The script will:

   * create the database
   * insert sample data
   * run analysis
   * display results and charts

---

## 🎯 Future Improvements

* Incorporate real-world datasets
* Extend time-based analysis (daily/weekly trends)
* Develop optimization models (e.g., facility location, routing)
* Build interactive dashboards (Power BI / Streamlit)

---

## 💼 Project Purpose

This project demonstrates the ability to:

* Design and implement relational databases
* Perform SQL-based data analysis
* Integrate SQL with Python workflows
* Analyze supply chain performance using KPIs
* Communicate insights through data visualization

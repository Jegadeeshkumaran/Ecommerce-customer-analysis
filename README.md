Clustering the customers based on their purchase - "Monetary","Recency","Frequency" using K-Means clustering.
 * Data cleansing is done by removing the null values, Converting the CustomerId column from float to string and  InvoiceDate column form object to date time 
 * Data preparation is done on the basis of 
                             R (Recency): Number of days since last purchase
                              F (Frequency): Number of transactions
                             M (Monetary): Total amount of transactions (revenue contributed)
* Removing the outliers  
* Scaling the data using StandardScaller Method
* Building K_Means Model
* Using elbow method finding the k value
* Again fitting the data with the k means value found using the elbow method

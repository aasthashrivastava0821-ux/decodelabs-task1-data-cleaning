import pandas as pd

# load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

#fill missing coupon codes 
df["CouponCode"] = df["CouponCode"].fillna("No CouponCode")

#check missing values
print(df.isnull().sum())

#check duplicates
print("Duplicate Row:", df.duplicated().sum())
print("Duplicate  Order IDs:", df["OrderID"].duplicated().sum())

#save cleaned dataset 
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Data cleaning completed successfully!")
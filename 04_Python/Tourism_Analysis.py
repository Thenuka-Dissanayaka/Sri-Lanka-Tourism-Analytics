import pyodbc
import pandas as pd

# =====================================
# 1. SQL SERVER CONNECTION
# =====================================

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=SriLankaTourismDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    print("SQL Server Connected Successfully!")

    # =====================================
    # 2. LOAD FULL DATASET
    # =====================================

    query = """
    SELECT Country, Month, Arrivals, Year
    FROM dbo.TourismArrivals_Cleaned;
    """

    df = pd.read_sql(query, conn)

    # Standardize Month Names

    month_mapping = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
    }

    df["Month_Clean"] = (
        df["Month"]
        .str.strip()
        .str.title()
        .replace(month_mapping)
    )

    print("\n========== CLEANED MONTH VALUES ==========")
    print(sorted(df["Month_Clean"].unique()))

    print("\n========== MONTH VALUE COUNTS ==========")
    print(df["Month_Clean"].value_counts())

    print("\nDataset Loaded Successfully!")

    # =====================================
    # 3. DATASET INFORMATION
    # =====================================

    print("\n========== DATASET INFORMATION ==========")
    df.info()

    # =====================================
    # 4. DATASET SHAPE
    # =====================================

    print("\n========== DATASET SHAPE ==========")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # =====================================
    # 5. FIRST 5 RECORDS
    # =====================================

    print("\n========== FIRST 5 RECORDS ==========")
    print(df.head())

    # =====================================
    # 6. LAST 5 RECORDS
    # =====================================

    print("\n========== LAST 5 RECORDS ==========")
    print(df.tail())

    # =====================================
    # 7. COLUMN NAMES
    # =====================================

    print("\n========== COLUMN NAMES ==========")
    print(df.columns.tolist())

    # =====================================
    # 8. DATA TYPES
    # =====================================

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    # =====================================
    # 9. BASIC STATISTICS
    # =====================================

    print("\n========== BASIC STATISTICS ==========")
    print(df.describe())

    # =====================================
    # 10. MISSING VALUES CHECK
    # =====================================

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    # =====================================
    # 11. DUPLICATE RECORDS CHECK
    # =====================================

    print("\n========== DUPLICATE RECORDS ==========")
    print("Duplicate Rows:", df.duplicated().sum())

    print("\n========== DUPLICATE RECORD DETAILS ==========")

    duplicates = df[df.duplicated(keep=False)]

    print(duplicates.sort_values(
        by=["Year", "Country", "Month"]
    ).to_string(index=False))

    print("\nTotal Duplicate Rows:", len(duplicates))

    # =====================================
    # 12. UNIQUE COUNTRIES
    # =====================================

    print("\n========== UNIQUE COUNTRIES ==========")   
    print("Total Countries:", df["Country"].nunique())

    # =====================================
    # 13. UNIQUE MONTHS
    # =====================================

    print("\n========== UNIQUE MONTHS ==========")
    print(df["Month"].unique())

    # =====================================
    # 14. YEAR RANGE
    # =====================================

    print("\n========== YEAR RANGE ==========")
    print(sorted(df["Year"].unique()))

    # =====================================
    # 15. MONTH VALUE FREQUENCY
    # =====================================

    print("\n========== MONTH VALUE COUNTS ==========")
    print(df["Month"].value_counts().sort_index())

    # Aggregate duplicate country-month-year records

    df_clean = (
        df.groupby(
            ["Country", "Month_Clean", "Year"],
            as_index=False
        )["Arrivals"]
        .sum()
    )

    print("\n========== CLEANED DATASET ==========")
    print("Original Records:", len(df))
    print("Cleaned Records:", len(df_clean))

    print("\nRemaining Duplicates:",
          df_clean.duplicated(
              subset=["Country", "Month_Clean", "Year"]
          ).sum())

    print("\n2020 Total Arrivals:",
          df_clean.loc[df_clean["Year"] == 2020, "Arrivals"].sum())

    # =====================================
    # 16. YEAR-WISE TOTAL ARRIVALS
    # =====================================

    print("\n========== YEAR-WISE TOTAL ARRIVALS ==========")

    yearly_totals = df.groupby("Year")["Arrivals"].sum()

    print(yearly_totals)

    # =====================================
    # 17. UNEXPECTED MONTH VALUES
    # =====================================

    valid_months = [
        "JANUARY", "FEBRUARY", "MARCH", "APRIL",
        "MAY", "JUNE", "JULY", "AUGUST",
        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
    ]

    month_clean = df["Month"].str.strip().str.upper()

    unexpected_months = df.loc[~month_clean.isin(valid_months), "Month"]

    print("\n========== UNEXPECTED MONTH VALUES ==========")
    print(unexpected_months.value_counts())

    # =====================================
    # 18. INVESTIGATE 2020 DATA
    # =====================================

    print("\n========== 2020 DATA CHECK ==========")

    data_2020 = df[df["Year"] == 2020]

    print("Total 2020 Records:", len(data_2020))

    print("\n2020 Month Values:")
    print(data_2020["Month"].value_counts().to_string())

    print("\n2020 Unexpected Month Records:")

    valid_months = [
        "JANUARY", "FEBRUARY", "MARCH", "APRIL",
        "MAY", "JUNE", "JULY", "AUGUST",
        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
    ]

    month_clean = data_2020["Month"].str.strip().str.upper()

    invalid_2020 = data_2020[~month_clean.isin(valid_months)]

    print(invalid_2020.to_string(index=False))

    print("\nTotal Arrivals in 2020:")
    print(data_2020["Arrivals"].sum())

    # =====================================
    # 19. 2020 SUMMARY RECORDS
    # =====================================

    print("\n========== 2020 SUMMARY RECORDS ==========")

    summary_2020 = df[
        (df["Year"] == 2020) &
        (df["Month"].str.contains("_Sum|Total", case=False, na=False))
    ]

    print(summary_2020.head(20).to_string(index=False))

    print("\nTotal Summary Records:")
    print(len(summary_2020))

    # =====================================
    # 20. 2020 MONTHLY DATA CHECK
    # =====================================

    print("\n========== 2020 MONTHLY DATA ==========")

    monthly_2020 = df[df["Year"] == 2020].copy()

    monthly_2020["Month_Clean"] = (
        monthly_2020["Month"].str.strip().str.upper()
    )

    valid_months = [
        "JANUARY", "FEBRUARY", "MARCH", "APRIL",
        "MAY", "JUNE", "JULY", "AUGUST",
        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
    ]

    monthly_2020 = monthly_2020[
        monthly_2020["Month_Clean"].isin(valid_months)
    ]

    print("Monthly Records:", len(monthly_2020))

    print("\nMonthly Arrivals Total:")
    print(monthly_2020["Arrivals"].sum())

    print("\nMonthly Data Sample:")
    print(monthly_2020.head(20).to_string(index=False))

    print("\n========== DUPLICATE RECORD ANALYSIS ==========")

    duplicates = df[
        df.duplicated(
            subset=["Country", "Month_Clean", "Year"],
            keep=False
        )
    ]

    print(duplicates.sort_values(
        by=["Year", "Country", "Month_Clean"]
    ).to_string(index=False))

    print("\nTotal Duplicate Records:", len(duplicates))

    # Export Cleaned Dataset

    output_path = "Tourism_Cleaned_Dataset.csv"

    df_clean.to_csv(output_path, index=False)

    print("\nCleaned Dataset Exported Successfully!")
    print("File Name:", output_path)

except Exception as e:
    print("\nERROR OCCURRED:")
    print(e)

finally:
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("\nSQL Server Connection Closed.")

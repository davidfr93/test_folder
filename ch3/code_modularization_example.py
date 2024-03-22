import pandas as pd

def read_data(file_name):

    df = pd.read_csv(file_name)
    return df

def cap_outliers(feature, upper_percentile, lower_percentile):

    lower_thresh = feature.quantile(lower_percentile)
    upper_thresh = feature.quantile(upper_percentile)

    feature = feature.map(lambda val: \
                          lower_thresh if val < lower_thresh \
                          else upper_thresh if val > upper_thresh \
                          else val)

    return feature


def clean_data(df, upper_percentile, lower_percentile):

    df = df.fillna(df.median(numeric_only=True))

    for col in df.columns:
        if df.dtypes[col] in ("float64", "int64"):
            df[col] = cap_outliers(df[col], upper_percentile, lower_percentile)

    # additional cleaning...
    # [code block]

    return df

if __name__ == "__main__":

    customer_data = read_data("customer_data.csv")

    cleaned_data = clean_data(customer_data)

    # additional code
    # [code block]

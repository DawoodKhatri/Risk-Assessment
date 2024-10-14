import pandas as pd
import json


def getExtractedData():
    file_path = 'data/risk.xlsx'
    sheet_name = "RISK FACTORS INVENTORY"

    df = pd.read_excel(file_path, sheet_name=sheet_name)

    df = df.where(pd.notnull(df), None)

    data = []

    for i in range(1, len(df)):
        data.append({
            "category": df["Unnamed: 1"][i],
            "audience": df["Unnamed: 3"][i],
            "cause": df["Unnamed: 4"][i],
            "subCategory": df["Unnamed: 5"][i],
            "externalSubCategory": df["Unnamed: 6"][i],
            "explaination": df["Unnamed: 7"][i],
            "measures": {
                "units": df["Measures"][i],
                "type": df["Unnamed: 9"][i],
                "per": df["Unnamed: 10"][i],
                "other": df["Unnamed: 11"][i],
                "frequency": df["Unnamed: 12"][i],
            },
            "riskLevel": {
                "low": df["Risk Level"][i],
                "medium": df["Unnamed: 14"][i],
                "high": df["Unnamed: 15"][i],
            },
            "estimationRational": df["Unnamed: 16"][i],
            "mitigation": df["Unnamed: 17"][i],
        })

    return json.dumps(data)

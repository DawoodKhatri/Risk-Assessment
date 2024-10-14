import pandas as pd


def getExtractedData():
    file_path = 'data/risk.xlsx'
    sheet_name = "RISK FACTORS INVENTORY"

    df = pd.read_excel(file_path, sheet_name=sheet_name)

    df = df.where(pd.notnull(df), None)

    data = {
        "topLevelCategory": df["Unnamed: 1"].values[1:].tolist(),
        "audience": df["Unnamed: 3"].values[1:].tolist(),
        "cause": df["Unnamed: 4"].values[1:].tolist(),
        "subCategory": df["Unnamed: 5"].values[1:].tolist(),
        "externalSubCategory": df["Unnamed: 6"].values[1:].tolist(),
        "explaination": df["Unnamed: 7"].values[1:].tolist(),
        "measures": {
            "units": df["Measures"].values[1:].tolist(),
            "type": df["Unnamed: 9"].values[1:].tolist(),
            "per": df["Unnamed: 10"].values[1:].tolist(),
            "other": df["Unnamed: 11"].values[1:].tolist(),
            "frequency": df["Unnamed: 12"].values[1:].tolist(),
        },
        "riskLevel": {
            "low": df["Risk Level"].values[1:].tolist(),
            "medium": df["Unnamed: 14"].values[1:].tolist(),
            "high": df["Unnamed: 15"].values[1:].tolist(),
        },
        "estimationRational": df["Unnamed: 16"].values[1:].tolist(),
        "mitigation": df["Unnamed: 17"].values[1:].tolist(),
    }

    return data

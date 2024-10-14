from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import pandas as pd
import openai
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"  # Replace with your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define data models

class CostPerUnit(BaseModel):
    min: float
    max: float
    currency: str

class EstimatedTotalCost(BaseModel):
    min: Optional[float] = None
    max: Optional[float] = None

class Visual(BaseModel):
    type: str
    dataPoints: List[dict]
    description: str

class RiskData(BaseModel):
    topLevelCategory: str
    audience: str
    cause: str
    subcategory: str
    externalSubcategory: str
    explanation: str
    units: str
    type: str
    costPerUnit: CostPerUnit
    frequency: str
    estimationRationale: str
    numberOfTransactions: Optional[int] = None
    estimatedTotalCost: EstimatedTotalCost
    riskLevel: Optional[str] = None  # Possible values: Low, Medium, High
    mitigationStrategies: List[str]
    visuals: List[Visual]

# Initialize FastAPI app
app = FastAPI()

# Function to read risk data from an Excel file
def read_risk_data_from_excel(file_path: str) -> List[RiskData]:
    df = pd.read_excel(file_path)

    risk_data_list = []
    for _, row in df.iterrows():
        cost_per_unit = CostPerUnit(
            min=row['costPerUnit_min'],
            max=row['costPerUnit_max'],
            currency=row['costPerUnit_currency']
        )

        estimated_total_cost = EstimatedTotalCost(
            min=row.get('estimatedTotalCost_min'),
            max=row.get('estimatedTotalCost_max')
        )

        # Parse mitigation strategies (assuming comma-separated strings)
        mitigation_strategies = [s.strip() for s in row['mitigationStrategies'].split(',')]

        # Parse visuals if applicable (omitted for brevity)
        visuals = []

        risk_data = RiskData(
            topLevelCategory=row['topLevelCategory'],
            audience=row['audience'],
            cause=row['cause'],
            subcategory=row['subcategory'],
            externalSubcategory=row['externalSubcategory'],
            explanation=row['explanation'],
            units=row['units'],
            type=row['type'],
            costPerUnit=cost_per_unit,
            frequency=row['frequency'],
            estimationRationale=row['estimationRationale'],
            numberOfTransactions=row.get('numberOfTransactions'),
            estimatedTotalCost=estimated_total_cost,
            riskLevel=row.get('riskLevel'),
            mitigationStrategies=mitigation_strategies,
            visuals=visuals
        )

        risk_data_list.append(risk_data)

    return risk_data_list

@app.post("/analyze")
async def analyze_risk():
    # Path to your Excel file
    file_path = "risk_data.xlsx"  # Replace with the actual path to your Excel file

    # Read data from Excel
    risk_data_list = read_risk_data_from_excel(file_path)

    # Process each risk data item
    results = []
    for item in risk_data_list:
        # Prepare prompt based on the risk data
        prompt = f"""
You are an expert in risk management. Provide detailed risk mitigation strategies for the following risk:

Top Level Category: {item.topLevelCategory}
Audience: {item.audience}
Cause: {item.cause}
Subcategory: {item.subcategory}
External Subcategory: {item.externalSubcategory}
Explanation: {item.explanation}
Units: {item.units}
Type: {item.type}
Cost Per Unit: Min {item.costPerUnit.min} {item.costPerUnit.currency}, Max {item.costPerUnit.max} {item.costPerUnit.currency}
Frequency: {item.frequency}
Estimation Rationale: {item.estimationRationale}
Number of Transactions: {item.numberOfTransactions}
Estimated Total Cost: Min {item.estimatedTotalCost.min}, Max {item.estimatedTotalCost.max}
Risk Level: {item.riskLevel}

Provide Mitigation Strategies:
"""

        # Use OpenAI API to get risk mitigation strategies
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
            n=1,
            stop=None,
        )

        mitigation_strategies = response.choices[0].text.strip()

        # Collect the results
        results.append({
            "topLevelCategory": item.topLevelCategory,
            "mitigationStrategies": mitigation_strategies
        })

    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

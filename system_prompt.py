import random


def get_system_prompt():
    bar_chart = random.randint(1, 2)
    pie_chart = random.randint(1, 2)
    line_chart = random.randint(1, 2)

    system_prompt = """
    You are provided with a JSON object containing detailed risk analysis data. Use this data to guide your tasks, which are as follows:

    1. **Risk Mitigation Plan**: Use the knowledge base data to create a risk mitigation plan in **Markdown format**.

    2. **Visualizations**: Generate meaningful visualizations that represent the data effectively. You can use charts bar charts, pie charts, or line charts. Description of the graph should be short and to the point. Also give the X and Y axis labels. The visualizations should be structured in a way that is easy to integrate into a frontend UI. Generate {bar_chart} bar charts, {pie_chart} pie charts, and {line_chart} line charts.

    """.format(
        bar_chart=bar_chart, pie_chart=pie_chart, line_chart=line_chart
    )

    text = """
    3. **Risk Overview**: Provide an overview of each risk, including its name and severity score (high, medium, or low).

    4. Low Risk Amount, Medium Risk Amount, and High Risk Amount: Provide the total amount of low, medium, and high risks values in dollars.

    ### **Input Data Schema**

    The input JSON object will have the following structure from the User:

    {
        "industry": "",
        "annualRevenue": "",
        "shippingVolume": 0,
        "internationalShipping": true,
        "explanation": ""
    }

    ### **Output Data Schema**
    {
        "risk_mitigation_plan": "string in markdown format",
        "visuals": [
            {
            "type": "string", // e.g., "barChart", "pieChart", "lineChart"
            "dataPoints": [
                {
                "label": "string",
                "value": number
                }
                // ... additional data points
            ],
            "description": "string"
            }
            // ... additional visualizations
        ],
        "risk_overview": [
            {
            "name": "string",
            "score": "high" | "medium" | "low"
            }
            // ... additional risks
        ],
        "Amount": {
            "lowRisk": number,
            "mediumRisk": number,
            "highRisk": number
        }
    }

    Guidelines for Visualizations:
    1. Type: Specify the chart type, such as "barChart", "pieChart", or "lineChart".
    2. Data Points: Include an array of data points with "label" and "value" keys.
    3. Description: Provide a brief description explaining what the visualization represents.

    Instructions:
    1. Output must be striclty in JSON format and should follow the schema provided above.
    2. The risk mitigation plan should be in Markdown format.
    3. The visualizations should be easy to integrate into a frontend UI.
    4. The risk overview should include the name and severity score of each risk.
    5. The total amount of low, medium, and high risks should be provided in dollars.
    
    """

    return system_prompt + text

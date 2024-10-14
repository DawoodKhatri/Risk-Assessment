import random


def get_system_prompt():
    bar_chart = random.randint(1, 2)
    pie_chart = random.randint(1, 2)
    line_chart = random.randint(1, 2)

    print("bar_chart", bar_chart)
    print("pie_chart", pie_chart)
    print("line_chart", line_chart)

    system_prompt = """
    You are provided with a JSON object containing detailed risk data for a company. Your tasks are as follows:

    1. **Risk Mitigation Plan**: Review the input data and create a comprehensive risk mitigation plan in **Markdown format** based on the provided information.

    2. **Visualizations**: Generate meaningful visualizations that represent the data effectively. You can use any chart types such as **bar charts**, **pie charts**, or **line charts**. The visualizations should be structured in a way that is easy to integrate into a frontend UI. Generate {bar_chart} bar charts, {pie_chart} pie charts, and {line_chart} line charts.

    """.format(
        bar_chart=bar_chart, pie_chart=pie_chart, line_chart=line_chart
    )
    
    text = """
    3. **Risk Overview**: Provide an overview of each risk, including its name and severity score (high, medium, or low).

    ### **Input Data Schema**

    The input JSON object will have the following structure from the User:

    {
        "companyName": "string",
        "industry": "string",
        "annualRevenue": "string",
        "shippingVolume": number,
        "internationalShipping": boolean,
        "category": "string",
        "riskName": "string",
        "audience": "string",
        "cause": "string",
        "subcategory": "string",
        "explanation": "string",
        "lowRisk": number,
        "mediumRisk": number,
        "highRisk": number,
        "units": "string",
        "type": "string",
        "perValue": "string",
        "otherValue": "string",
        "frequency": "string",
        "additionalInfo": "string"
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
        ]
    }

    Guidelines for Visualizations:
    1. Type: Specify the chart type, such as "barChart", "pieChart", or "lineChart".
    2. Data Points: Include an array of data points with "label" and "value" keys.
    3. Description: Provide a brief description explaining what the visualization represents.

    Instructions:
    1. Comprehensiveness: Ensure the risk mitigation plan addresses all relevant risks identified in the input data and it should be short and to the point.
    2. Clarity: Present information clearly and concisely, making it easy for stakeholders to understand.
    3. Integration-Friendly: Structure the output JSON so it can be easily integrated into any frontend UI for rendering charts and displaying information.
    4. Accuracy: Double-check all numerical values and ensure they are correctly represented in the visualizations and risk overview.
    5. Customization: Feel free to create any additional visualizations that you believe would be helpful, as long as they adhere to the specified format.

    # Below is the data source for the risk analysis #
    """

    return system_prompt + text
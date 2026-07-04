# tools.py

from langchain.tools import tool


@tool
def crop_recommendation(state: str) -> str:
    """
    Use this tool to recommend suitable crops for a given state.
    Call this whenever the user asks what crop to grow.
    """

    crops = {
        "karnataka": "Maize",
        "punjab": "Wheat",
        "maharashtra": "Cotton",
        "west bengal": "Rice",
        "uttar pradesh": "Sugarcane",
        "andhra pradesh": "Rice",
        "telangana": "Cotton",
        "tamil nadu": "Rice",
        "kerala": "Coconut"
    }

    crop = crops.get(state.lower(), "Rice")

    return f"Recommended crop for {state} is {crop}."


@tool
def market_price(crop: str) -> str:
    """
    Use this tool whenever the user asks about crop prices,
    market value, selling price, profit, or income.
    """

    prices = {
        "maize": "₹1800 per quintal",
        "wheat": "₹2200 per quintal",
        "rice": "₹2500 per quintal",
        "cotton": "₹7000 per quintal",
        "sugarcane": "₹340 per quintal",
        "coconut": "₹35 per nut"
    }

    return prices.get(
        crop.lower(),
        "Market price not available."
    )


@tool
def weather_advisory(location: str) -> str:
    """
    Provide a simple weather advisory.
    """

    return (
        f"The weather in {location} is currently suitable "
        f"for farming activities. Ensure adequate irrigation "
        f"and monitor local weather updates."
    )


@tool
def fertilizer_recommendation(crop: str) -> str:
    """
     Use this tool whenever the user asks about fertilizers,
    nutrients, crop growth, or soil management.
    """

    fertilizers = {
        "rice": "NPK (20:20:20)",
        "wheat": "Urea",
        "maize": "DAP",
        "cotton": "Potash",
        "sugarcane": "Nitrogen-rich fertilizer",
        "coconut": "Organic compost"
    }

    return fertilizers.get(
        crop.lower(),
        "No fertilizer recommendation available."
    )


@tool
def pest_management(crop: str) -> str:
    """
    Use this tool whenever the user asks about pests,
    diseases, crop protection, or preventive measures.
    """

    advice = {
        "rice": "Monitor for stem borers and use recommended pesticides.",
        "wheat": "Watch for aphids and rust diseases.",
        "maize": "Inspect for fall armyworm infestation.",
        "cotton": "Monitor for bollworms regularly.",
        "sugarcane": "Check for early shoot borer attacks."
    }

    return advice.get(
        crop.lower(),
        "No pest advisory available."
    )


@tool
def irrigation_advice(crop: str) -> str:
    """
    Use this tool whenever the user asks about watering,
    irrigation schedules, moisture management, or farming practices.
    """

    irrigation = {
        "rice": "Maintain standing water during growth stages.",
        "wheat": "Irrigate every 10–15 days depending on soil moisture.",
        "maize": "Water during tasseling and grain filling stages.",
        "cotton": "Avoid over-irrigation; maintain moderate moisture.",
        "sugarcane": "Frequent irrigation is recommended."
    }

    return irrigation.get(
        crop.lower(),
        "No irrigation advice available."
    )
@tool
def farming_advisor(query: str) -> str:
    """
    Provides complete farming advice.
    """
    return (
        "Based on current conditions, maintain proper irrigation, "
        "apply recommended fertilizers, and monitor pest activity regularly."
    )

# List of all tools for easy import

TOOLS = [
    crop_recommendation,
    market_price,
    weather_advisory,
    fertilizer_recommendation,
    pest_management,
    irrigation_advice,
    farming_advisor
]
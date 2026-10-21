from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

predict_price_decl = types.FunctionDeclaration(
    name="predict_price",
    description="Estime le prix d'une maison au Nigeria, en nairas.",
    parameters={
        "type": "object",
        "properties": {
            "bedrooms": {"type": "number", "description": "Nombre de chambres"},
            "bathrooms": {"type": "number", "description": "Nombre de salles de bain"},
            "toilets": {"type": "number", "description": "Nombre de toilettes"},
            "parking_space": {"type": "number", "description": "Places de parking"},
            "town": {"type": "string", "description": "Ville"},
            "state": {"type": "string", "description": "État du Nigeria"},
            "title": {"type": "string", "description": "Type de bien, ex. Detached Duplex"},
        },
        "required": ["bedrooms", "bathrooms", "toilets", "parking_space",
                     "town", "state", "title"],
    },
)

tool = types.Tool(function_declarations=[predict_price_decl])

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Combien vaut une maison de 3 chambres, 3 salles de bain, 4 toilettes, "
             "2 places de parking, à Lekki, état de Lagos, de type Detached Duplex ?",
    config=types.GenerateContentConfig(tools=[tool]),
)

part = response.candidates[0].content.parts[0]
print(part.function_call)
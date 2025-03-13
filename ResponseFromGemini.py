from google import genai


def responseFromGemini(text):
    client = genai.Client(api_key="api_key")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=text
    )

    return response.text

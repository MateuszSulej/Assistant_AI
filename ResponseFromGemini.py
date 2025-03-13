from google import genai


def responseFromGemini(text):
    client = genai.Client(api_key="AIzaSyBgZZonW8TU-J_3Kb6lT4wx9xD64XQksBo")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=text
    )

    return response.text

import base64
import json
import os
from typing import List

from google import genai
from google.genai import types

# For whatever dumb reason google disabled system prompts
# MAKE_EMAIL_RESPONSE = '''The user will provide a corporate webpage in html. Respond with html for a marketing email inspired by the page. Use a similar comms strategy.

# Here is an example response
# <!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Keeper Security: Secure Your Digital Life</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            background-color: #f5f5f5;\n            margin: 0;\n            padding: 0;\n        }\n        .email-container {\n            max-width: 600px;\n            margin: 0 auto;\n            background-color: #ffffff;\n            padding: 20px;\n            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);\n        }\n        .header {\n            background-color: #000000;\n            color: #ffffff;\n            text-align: center;\n            padding: 20px;\n        }\n        .header h1 {\n            margin: 0;\n            font-size: 24px;\n        }\n        .content {\n            padding: 20px;\n            text-align: center;\n        }\n        .content h2 {\n            font-size: 20px;\n            color: #333333;\n        }\n        .content p {\n            font-size: 16px;\n            color: #666666;\n            line-height: 1.5;\n        }\n        .button {\n            display: inline-block;\n            background-color: #FFD700;\n            color: #000000;\n            padding: 10px 20px;\n            text-decoration: none;\n            margin-top: 20px;\n            border-radius: 5px;\n        }\n        .footer {\n            background-color: #000000;\n            color: #ffffff;\n            text-align: center;\n            padding: 10px;\n            font-size: 12px;\n        }\n        .footer a {\n            color: #FFD700;\n            text-decoration: none;\n        }\n    </style>\n</head>\n<body>\n    <div class="email-container">\n        <div class="header">\n            <h1>Keeper Security</h1>\n        </div>\n        <div class="content">\n            <h2>Secure Your Digital Life</h2>\n            <p>Every few seconds, a person or organization falls victim to ransomware. Protect yourself and your loved ones with Keeper's advanced security solutions.</p>\n            <p>Get started with the trusted AI-enabled cybersecurity platform to prevent data breaches and manage passwords securely.</p>\n            <a href="https://www.keepersecurity.com" class="button">Learn More</a>\n        </div>\n        <div class="footer">\n            &copy; 2025 Keeper Security, Inc. All rights reserved. <br>\n            <a href="https://www.keepersecurity.com/privacy">Privacy Policy</a> | <a href="https://www.keepersecurity.com/terms">Terms of Service</a>\n        </div>\n    </div>\n</body>\n</html>'''

MAKE_EMAIL_RESPONSE = '''Here is my corporate webpage in html. Respond with only html for a marketing email inspired by the page. Use a similar comms strategy. I do not want an explanation for the html.

Here is an example response  
<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Keeper Security: Secure Your Digital Life</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            background-color: #f5f5f5;\n            margin: 0;\n            padding: 0;\n        }\n        .email-container {\n            max-width: 600px;\n            margin: 0 auto;\n            background-color: #ffffff;\n            padding: 20px;\n            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);\n        }\n        .header {\n            background-color: #000000;\n            color: #ffffff;\n            text-align: center;\n            padding: 20px;\n        }\n        .header h1 {\n            margin: 0;\n            font-size: 24px;\n        }\n        .content {\n            padding: 20px;\n            text-align: center;\n        }\n        .content h2 {\n            font-size: 20px;\n            color: #333333;\n        }\n        .content p {\n            font-size: 16px;\n            color: #666666;\n            line-height: 1.5;\n        }\n        .button {\n            display: inline-block;\n            background-color: #FFD700;\n            color: #000000;\n            padding: 10px 20px;\n            text-decoration: none;\n            margin-top: 20px;\n            border-radius: 5px;\n        }\n        .footer {\n            background-color: #000000;\n            color: #ffffff;\n            text-align: center;\n            padding: 10px;\n            font-size: 12px;\n        }\n        .footer a {\n            color: #FFD700;\n            text-decoration: none;\n        }\n    </style>\n</head>\n<body>\n    <div class="email-container">\n        <div class="header">\n            <h1>Keeper Security</h1>\n        </div>\n        <div class="content">\n            <h2>Secure Your Digital Life</h2>\n            <p>Every few seconds, a person or organization falls victim to ransomware. Protect yourself and your loved ones with Keeper's advanced security solutions.</p>\n            <p>Get started with the trusted AI-enabled cybersecurity platform to prevent data breaches and manage passwords securely.</p>\n            <a href="https://www.keepersecurity.com" class="button">Learn More</a>\n        </div>\n        <div class="footer">\n            &copy; 2025 Keeper Security, Inc. All rights reserved. <br>\n            <a href="https://www.keepersecurity.com/privacy">Privacy Policy</a> | <a href="https://www.keepersecurity.com/terms">Terms of Service</a>\n        </div>\n    </div>\n</body>\n</html>'''

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)
MODEL = "gemini-2.0-flash"

MAKE_SUMMARY_TEXT = "Here are series of interviews from colleges who took the bait from our corporate anti-phishing training. The cybersecurity team would like you to summarize the interviews so they can plan next steps."


def complete_email_html(hompage_html: str):
    contents = [
        # types.Content(
        #     role="system", parts=[types.Part.from_text(text=MAKE_EMAIL_RESPONSE)]
        # ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f'{MAKE_EMAIL_RESPONSE}\nWebpage:\n{hompage_html}'
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    completion = client.models.generate_content(
        model=MODEL,
        contents=contents,
        config=generate_content_config,
    )
    return completion.text


def complete_summary(chats: List[str]) -> str:
    contents = [
        # types.Content(
        #     role="system", parts=[types.Part.from_text(text=MAKE_EMAIL_RESPONSE)]
        # ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f'{MAKE_SUMMARY_TEXT}\Interviews:\n{json.dumps(chats)}'
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    completion = client.models.generate_content(
        model=MODEL,
        contents=contents,
        config=generate_content_config,
    )
    return completion.text

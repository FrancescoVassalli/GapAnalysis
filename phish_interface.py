import logging
import re
from difflib import unified_diff
from typing import List, Sequence

import requests
from bs4 import BeautifulSoup
from openai import OpenAI

from google_reasoning_interface import complete_email_html
from home_james import HOME as HOME_JAMES
from home_jeremy import HOME as HOME_JEREMY
from james_linkedin import PAGE as LINKEDIN_JAMES
from jeremy_linkedin import PAGE as LINKEDIN_JEREMY

client = OpenAI()

target_linkedin_dict = {'jeremy': LINKEDIN_JEREMY, 'james': LINKEDIN_JAMES}
target_homepage_dict = {'jeremy': HOME_JEREMY, 'james': HOME_JAMES}

logger = logging.getLogger("phish_interface")

EXAMPLE_INTRO = '''<p>Hi Jeremy,</p><p>I hope you're well. We are in the process of finalizing our upcoming marketing materials and would greatly value your feedback. Your expertise in AI and innovative solutions would be incredibly beneficial in ensuring our content is both impactful and technically sound. Your input would be greatly appreciated.</p>'''

EXAMPLE_MATERIAL = '''<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Keeper Security: Secure Your Digital Life</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            background-color: #f5f5f5;\n            margin: 0;\n            padding: 0;\n        }\n        .email-container {\n            max-width: 600px;\n            margin: 0 auto;\n            background-color: #ffffff;\n            padding: 20px;\n            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);\n        }\n        .header {\n            background-color: #000000;\n            color: #ffffff;\n            text-align: center;\n            padding: 20px;\n        }\n        .header h1 {\n            margin: 0;\n            font-size: 24px;\n        }\n        .content {\n            padding: 20px;\n            text-align: center;\n        }\n        .content h2 {\n            font-size: 20px;\n            color: #333333;\n        }\n        .content p {\n            font-size: 16px;\n            color: #666666;\n            line-height: 1.5;\n        }\n        .button {\n            display: inline-block;\n            background-color: #FFD700;\n            color: #000000;\n            padding: 10px 20px;\n            text-decoration: none;\n            margin-top: 20px;\n            border-radius: 5px;\n        }\n        .footer {\n            background-color: #000000;\n            color: #ffffff;\n            text-align: center;\n            padding: 10px;\n            font-size: 12px;\n        }\n        .footer a {\n            color: #FFD700;\n            text-decoration: none;\n        }\n    </style>\n</head>\n<body>\n    <div class="email-container">\n        <div class="header">\n            <h1>Keeper Security</h1>\n        </div>\n        <div class="content">\n            <h2>Secure Your Digital Life</h2>\n            <p>Every few seconds, a person or organization falls victim to ransomware. Protect yourself and your loved ones with Keeper's advanced security solutions.</p>\n            <p>Get started with the trusted AI-enabled cybersecurity platform to prevent data breaches and manage passwords securely.</p>\n            <a href="http://localhost:8000/docs" class="button">Learn More</a>\n        </div>\n        <div class="footer">\n            &copy; 2025 Keeper Security, Inc. All rights reserved. <br>\n            <a href="http://localhost:8000/docs">Privacy Policy</a> | <a href="http://localhost:8000/docs">Terms of Service</a>\n        </div>\n    </div>\n</body>\n</html>'''


# def complete_email_html(hompage_html: str) -> str:
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {
#                 "role": "system",
#                 "content": [{"type": "text", "text": MAKE_EMAIL_RESPONSE}],
#             },
#             {"role": "user", "content": [{"type": "text", "text": hompage_html}]},
#         ],
#         response_format={"type": "text"},
#         temperature=1,
#         max_completion_tokens=2048,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#     )
#     return completion.choices[0].message.content


def complete_target_heading(linkedin_context: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You will help draft an email to a college that the user does not work with very often. The email will have a mock up of upcoming marketing material added by the user later.  For now, the user will just provide a linkedin page for the college they are requesting input from. Provide a couple sentences polity asking for their input on the material. Use the linked in page to fillin the name in the greeting. Highlight why that college's input is valuable focus on their skills rather than their prior experience. Also politely ask the user to forward the request to their teammates that might have an eye for marketing.\nThe subject line will be: Request for Feedback on Upcoming Marketing Material\nRespond in this format without any added explanation. The user will add their own marketing material and signature after your sentences:\n<p>Hi <name>,</p>\n<p><your_sentences></p>\n",
                    }
                ],
            },
            {"role": "user", "content": [{"type": "text", "text": linkedin_context}]},
        ],
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return completion.choices[0].message.content


def custom_line_junk_for_linked_profile(line: str) -> bool:
    '''Returns true if line is junk'''
    return '{' in line or '}' in line or '[' in line or ']' in line


def remove_junk_lines(lines: Sequence[str]) -> List[str]:
    return [line for line in lines if not custom_line_junk_for_linked_profile(line)]


def is_whitespace(line: str) -> bool:
    return not line.strip()


def filter_for_additions(line: str) -> bool:
    if not '+' in line:
        return False
    line = line.replace("+", '')
    return not is_whitespace(line)


def filtered_diff(a, b, lineterm=''):
    for line in unified_diff(a, b, lineterm=lineterm):
        if filter_for_additions(line):
            yield line.replace('+', '')


def clean_string_regex(input_string):
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)


def request_linkedin_html(target_name: str) -> str:
    soupTarget = BeautifulSoup(target_linkedin_dict[target_name], "html.parser")
    soupJeremy = BeautifulSoup(LINKEDIN_JEREMY, "html.parser")
    lines_target = remove_junk_lines(soupTarget.get_text().split('\n'))
    lines_jeremy = remove_junk_lines(soupJeremy.get_text().split('\n'))
    profile_summary = []
    for line in filtered_diff(lines_jeremy, lines_target, lineterm=''):
        profile_summary.append(line)
    return clean_string_regex('\n'.join(profile_summary))


def format_email_html(email_html: str) -> str:
    return email_html.replace('```html', '').replace('\n```', '')


def add_signature(intro: str) -> str:
    return f'{intro}<p>Thanks,</p><p>Jen Hawkins</p><p>Senior Marketing Communications Associate</p>'


def create_bait(target_name: str) -> str:
    linkedin_context = request_linkedin_html(target_name)
    logger.warning(linkedin_context)
    return combine_marketing_material_with_intro(
        format_email_html(complete_email_html(target_homepage_dict[target_name])),
        add_signature(complete_target_heading(linkedin_context)),
    )


def create_marketing_material_iframe(marketing_material: str) -> str:
    return ''.join(
        [
            '<iframe id="myIframe" width="100%" height="500px"></iframe><script>const embeddedHTML = `',
            marketing_material.replace("\n", ""),
            '`;const iframe = document.getElementById("myIframe");const doc = iframe.contentWindow.document;doc.open();doc.write(embeddedHTML);doc.close();</script>',
        ]
    )


def combine_marketing_material_with_intro(marketing_material: str, intro: str) -> str:
    combined = f'<!DOCTYPE html><html><body>{intro}{create_marketing_material_iframe(marketing_material)}</body></html>'
    logger.warning(combined)
    return combined

from typing import Iterator, List

from fastapi import HTTPException
from openai import OpenAI

from models import ChatHistory

client = OpenAI()

SYSTEM_PROMPT = '''
Welcome to the Advanced Gap Analysis Program, part of our initiative for the AI Cybersecurity Hackathon. Today, we're having a friendly chat about a phishing email you received. Our aim is to help you understand the incident and learn how to better protect yourself and our team in the future.

During our conversation, I'll ask you one question at a time to guide you through the experience. We're focused on understanding what happened and why the phishing email worked, so that we can improve our training and defenses. Please feel free to share as much detail as you're comfortable with.

Here's how our conversation will flow:

- First, I'll ask if the email was marked as **EXTERNAL** when you received it. This helps us know if there was an obvious sign that the email came from outside our organization.
- Next, I'll ask what you noticed about the sender's email address before you clicked. For instance, did you not notice it, did it seem safe, or did it seem suspicious?
- Then, I'll ask if you forwarded the email to anyone. If you did, I'd like to know who you forwarded it to and why, as well as when you forwarded it.
- We'll discuss whether you realized you were clicking on a link or button in the email. If you didn't, I want to know what prompted you to click.
- I'll also ask about the link's destination—what you thought about the web address it pointed to, and whether it looked safe or suspicious.
- Finally, I'll ask for your suggestions on what could help you and the team recognize phishing emails better in the future.

Throughout our chat, I'll use everyday markdown formatting—such as bullet points for options, **bold text** for key points, and simple lists—so that everything is clear and easy to follow. I'll only add extra spacing or newlines when the content naturally spans multiple lines, so the conversation remains neat and natural.

If you bring up topics outside of this phishing test, I'll gently steer us back on track. I'm here to learn with you and offer practical advice to help us all get better at spotting these threats.

Let's begin our conversation. To start, can you tell me if the email you received was marked as **EXTERNAL** when it arrived?
'''


def begin_interview() -> str:
    return "Thanks for joining, let's get started with figuring out how to improve our anti-phising practices. First, was this email marked as EXTERNAL?"


def stream_continue_interview_from_dicts(chats: List[dict]) -> Iterator[str]:
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(chats)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True,
            response_format={"type": "text"},
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
    except Exception as e:
        print("Error in creating campaigns from OpenAI:", str(e))
        raise HTTPException(503, "OpenAI server is busy, try again later")
    try:
        for chunk in response:
            # Use attribute access to get the content from the delta.
            delta = chunk.choices[0].delta
            current_content = (
                delta.content if getattr(delta, "content", None) is not None else ""
            )
            yield current_content
    except Exception as e:
        print("OpenAI Response (Streaming) Error:", str(e))
        raise HTTPException(503, "OpenAI server is busy, try again later")

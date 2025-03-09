

from openai import OpenAI
client = OpenAI()

SYSTEM_PROMPT = "You are interviewing a college that clicked on a bait email to check their vigilance against phishing campaigns. Interview the user to find information useful to the cybersecurity team for uncovering gaps in their training. The user will begin the interview with the html for the email they clicked on. You should then take the lead in the interview by asking them questions.\nKey questions: \nWas this email marked as EXTERNAL?\nDid you forward this to anyone?\nWhat did you think of the sender's email address before clicking on the email? (multiple choice a. didn't notice b. Thought is was safe c. Thought it was suspicious )\nDid you know you were clicking on a link? (yes/no)\nWhat did you think of the link's web address? (Similar multiple choice)\nDid you want to go to that address?\n\nAsk the questions one at a time, and add follow up questions based on their answers to better understand gaps in the company's anti-phising practice.  For example if they noticed that the email was external you should then find out what company they thought the email was from. If they forwarded the email you should find out who they forwarded it to and when. More broadly, your goal is to find out the who,what,where,when,how for broader context around these key questions. However the user will not answer well if you ask them multiple questions at one time.\n"

def begin_interview(bait_context:str)->str:
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "system",
          "content": [
            {
              "type": "text",
              "text": SYSTEM_PROMPT
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": bait_context
            }
          ]
        }
      ],
      response_format={
        "type": "text"
      },
      temperature=1,
      max_completion_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return completion.choices[0].message.content
import Bubbles from "@components/chat/Bubbles";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute, useParams } from "@tanstack/react-router";

const fetchChatMessages = async (
  chatId: string
): Promise<{ type: "user" | "bot"; text: string }[]> => {
  return new Promise((resolve) => {
    // A collection of sample messages representing several conversation fragments.
    // Each message is part of a longer conversational exchange with multiple sentences.
    const sampleMessages: { type: "user" | "bot"; text: string }[] = [
      // Conversation Sample 1 (Existing)
      { type: "user", text: `Hi, this is Chat ${chatId}.` },
      {
        type: "bot",
        text: `Thank you for sharing that email, James. Let's start with a quick question: **Was this email marked as EXTERNAL?**`,
      },
      { type: "user", text: "Yes" },
      {
        type: "bot",
        text: `Did the external marking make you question the sender's identity? For example, did you immediately recognize who it was from, or was there uncertainty?`,
      },
      { type: "user", text: "I was a bit unsure who the sender was." },
      {
        type: "bot",
        text: `Regarding the sender's email address, what was your impression?  
- **a)** I didn't notice it  
- **b)** It looked safe  
- **c)** It seemed suspicious`,
      },
      { type: "user", text: "c" },
      {
        type: "bot",
        text: `Thank you for clarifying. Did you forward the email to anyone? If yes, who did you forward it to?`,
      },
      {
        type: "user",
        text: "I forwarded it to Jim because he is great at marketing.",
      },
      {
        type: "bot",
        text: `Did you send the email immediately, or did you wait a little before forwarding it?`,
      },
      { type: "user", text: "I sent it immediately." },
      {
        type: "bot",
        text: `Let’s discuss the link in the email. **Did you realize you were clicking on a link or a button at that time?**`,
      },
      {
        type: "user",
        text: "No, I just thought it was a button to get more information.",
      },
      {
        type: "bot",
        text: `Understood. What did you think about the destination URL?  
- **a)** I didn't really notice it  
- **b)** It appeared safe  
- **c)** It seemed suspicious`,
      },
      { type: "user", text: "a" },
      {
        type: "bot",
        text: `Great, thanks for that. Finally, what is one improvement you think could help prevent these situations in the future?`,
      },
      {
        type: "user",
        text: "Maybe making the buttons more obviously phishing-like would help.",
      },
      {
        type: "bot",
        text: `That's a valuable suggestion, James. Your feedback is very useful for our security training improvements. Thank you for your time!`,
      },

      // Conversation Sample 2
      {
        type: "user",
        text: `Hello, I'm following up on a suspicious email I received regarding our quarterly report. I feel it might be part of a phishing attempt, and I want to be cautious.`,
      },
      {
        type: "bot",
        text: `Hi there! Thanks for reaching out. I understand you have concerns about an email that seemed off. Could you tell me if the email had any **unusual sender details** or if it was marked as **EXTERNAL**?  
      
*Your detailed response will help us pinpoint the issue more accurately.*`,
      },
      {
        type: "user",
        text: `The email looked generic and the sender's address did not match any of our usual contacts. It was clearly marked as external, which raised my suspicions immediately.`,
      },
      {
        type: "bot",
        text: `I appreciate your insight. Emails that use vague sender details and unusual markings are classic red flags. Could you elaborate on the email's content? For example, did it include urgent calls to action or requests for sensitive information?  
      
This additional context is very valuable.`,
      },
      {
        type: "user",
        text: `Yes, it urged me to click a link to update my account details immediately, which felt very urgent and off. The language was overly dramatic and filled with exclamation points.`,
      },
      {
        type: "bot",
        text: `That's very concerning. Urgency and dramatic language are often tactics used in phishing attempts.  
      
- **Did you click on the link at all?**  
- **Were there any attachments?**  
      
Your cautious approach is exactly what we want to see.`,
      },
      {
        type: "user",
        text: `I didn't click the link, and there were no attachments. I simply reported it because I wasn't sure.`,
      },
      {
        type: "bot",
        text: `Thank you for your vigilance. Your actions help protect not only you but the entire organization. Could you share if you have any suggestions for improving our email verification process?  
      
For example, do you think additional training or a more robust alert system might help?`,
      },
      {
        type: "user",
        text: `I believe more frequent training sessions along with simulated phishing exercises could really help improve our defenses.`,
      },
      {
        type: "bot",
        text: `Great suggestion. Your feedback is crucial and will be passed on to our security team. Thank you for your thorough response.`,
      },

      // Conversation Sample 3
      {
        type: "user",
        text: `Hey, I received an email that felt very off and I wanted to report it immediately. It seemed unprofessional and the formatting was all over the place.`,
      },
      {
        type: "bot",
        text: `Hello, thanks for getting in touch. I understand that you noticed some inconsistencies in the email.  
      
Could you tell me more about the overall tone and structure?  
      
For instance, did it seem hastily put together with random capitalization or punctuation?  
      
*Any extra detail can really help us analyze the risk.*`,
      },
      {
        type: "user",
        text: `Absolutely, the email had inconsistent capitalization and the punctuation was erratic. It felt like it was thrown together quickly without proper editing.`,
      },
      {
        type: "bot",
        text: `That's definitely a red flag.  
      
Did the email contain any specific requests or instructions, such as asking you to verify your identity or click on a particular link?  
      
Understanding the full context of its content is very helpful.`,
      },
      {
        type: "user",
        text: `Yes, it instructed me to click on a link to confirm some details about my account, but the link looked suspicious.`,
      },
      {
        type: "bot",
        text: `Thank you for that information. It sounds like the email was designed to create urgency.  
      
Based on what you've described, do you have any ideas on what additional measures we could take to help users recognize these warning signs in the future?`,
      },
      {
        type: "user",
        text: `Perhaps a clear visual indicator in our internal email client could help highlight emails that are flagged as external or suspicious.`,
      },
      {
        type: "bot",
        text: `Excellent suggestion. Your feedback is highly appreciated. We'll consider this when updating our security protocols.`,
      },

      // Conversation Sample 4
      {
        type: "user",
        text: `Hi, I got an email today about a new update for our security system, but something felt off about it. I'm a bit confused and worried.`,
      },
      {
        type: "bot",
        text: `Hello, thank you for reaching out. I understand that the email's tone and content raised some concerns.  
      
Could you describe the email in detail? For instance, was the language formal or did it seem rushed?  
      
*Any specific examples or phrases you remember would be extremely helpful.*`,
      },
      {
        type: "user",
        text: `The email was quite long, filled with technical jargon, but it also had a casual, almost chatty tone that didn't match our usual formal communications. I felt like the sentences were too long and some parts seemed off-topic.`,
      },
      {
        type: "bot",
        text: `That definitely sounds unusual.  
      
Did the email include any links or requests for immediate action, such as updating your information?  
      
Sometimes, a mixture of formal technical language with casual tones is used to confuse the recipient.`,
      },
      {
        type: "user",
        text: `Yes, it insisted that I update my details right away, but I noticed some spelling mistakes and inconsistent formatting throughout the email.`,
      },
      {
        type: "bot",
        text: `Thank you for that detailed explanation.  
      
Your insights are very important, and I can see why you felt uneasy.  
      
Could you also let me know if the email contained any visual cues (like logos or specific color schemes) that were different from our standard communications?`,
      },
      {
        type: "user",
        text: `The logos seemed slightly off and the color palette was not what I expected from our IT department.`,
      },
      {
        type: "bot",
        text: `I appreciate your thorough response. It appears there are multiple inconsistencies that point toward a phishing attempt.  
      
Your feedback will be passed along to help refine our email security training.`,
      },

      // Conversation Sample 5
      {
        type: "user",
        text: `Good morning, I received an email this morning that seemed to be from our HR department, but it felt very unusual and informal.`,
      },
      {
        type: "bot",
        text: `Good morning! Thanks for reporting this. I understand that you’re concerned about the authenticity of the email.  
      
Could you provide some details on what made it feel unusual?  
      
For example, did it use casual language or contain any formatting that was out of place?  
      
*The more detailed your description, the better we can assess the situation.*`,
      },
      {
        type: "user",
        text: `The email was overly friendly and used a lot of emojis, which is not typical for HR communications. It also mentioned something about an urgent policy update in a very casual manner.`,
      },
      {
        type: "bot",
        text: `That's very interesting. Emojis and casual language in official communications are often a sign of phishing.  
      
Did the email ask you to click on a link or provide any personal information?  
      
Your input here is critical to our investigation.`,
      },
      {
        type: "user",
        text: `Yes, it asked me to verify my employee details by clicking a link, which made me even more suspicious.`,
      },
      {
        type: "bot",
        text: `Thank you for the details.  
      
Based on your description, it seems like this phishing attempt was designed to appear friendly and informal.  
      
Do you have any suggestions on how we might improve our email verification process to prevent such attempts in the future?`,
      },
      {
        type: "user",
        text: `Maybe a more robust internal verification badge for official communications could help differentiate genuine emails from suspicious ones.`,
      },
      {
        type: "bot",
        text: `That's a thoughtful suggestion. Thank you for your valuable feedback.`,
      },

      // Conversation Sample 6
      {
        type: "user",
        text: `Hey, I received an email from our finance team that seemed very strange. It talked about urgent budget approvals in a very informal manner.`,
      },
      {
        type: "bot",
        text: `Hello, thanks for bringing this up. I understand that an unusual email from finance can be alarming.  
      
Could you describe the email in detail?  
      
For instance, did it include any specific requests or use any language that seemed out of the ordinary?  
      
*Details such as these help us improve our internal safeguards.*`,
      },
      {
        type: "user",
        text: `The email was written in long, run-on sentences and lacked the formal tone I expect from our finance communications. It even had a couple of spelling mistakes and grammatical errors.`,
      },
      {
        type: "bot",
        text: `That definitely sounds off.  
      
Did the email request any immediate action, like clicking on a link to approve budgets or confirm transactions?  
      
Your careful observation is much appreciated.`,
      },
      {
        type: "user",
        text: `Yes, it asked me to click a link to confirm budget allocations immediately, which felt very rushed.`,
      },
      {
        type: "bot",
        text: `Thank you for sharing those details.  
      
It sounds like the email was designed to create a sense of urgency, which is a common phishing tactic.  
      
What would you suggest as a preventive measure to help employees identify these types of fraudulent emails in the future?`,
      },
      {
        type: "user",
        text: `Maybe regular training sessions with real-life examples would help improve our awareness.`,
      },
      {
        type: "bot",
        text: `That's a solid suggestion. Thank you for your thoughtful input.`,
      },

      // Conversation Sample 7
      {
        type: "user",
        text: `Hi, I just got an email that mentioned a new security protocol update, but it seemed very informal and oddly worded.`,
      },
      {
        type: "bot",
        text: `Hello! Thank you for reporting this. Could you describe the email in detail?  
      
For instance, did the email provide clear instructions or was it filled with ambiguous language and unusual formatting?  
      
*Your detailed description will help us identify any gaps in our security training.*`,
      },
      {
        type: "user",
        text: `The email was very conversational, almost as if it were a text message, but then it shifted into long paragraphs that sounded technical yet unprofessional.`,
      },
      {
        type: "bot",
        text: `That is indeed unusual.  
      
Did the email include any hyperlinks or attachments that you found suspicious?  
      
Also, what was your overall impression of the sender's email address?  
      
This extra detail would be extremely helpful.`,
      },
      {
        type: "user",
        text: `There was a hyperlink, but the domain didn't match our usual contacts, and the sender's address looked generic.`,
      },
      {
        type: "bot",
        text: `Thank you for clarifying. Your detailed feedback helps us pinpoint potential weaknesses in our communication channels.  
      
Do you have any recommendations on how we might improve our internal alerts or training to catch these anomalies early?`,
      },
      {
        type: "user",
        text: `I think an automated alert that flags emails with inconsistent domains or unusual language could be very effective.`,
      },
      {
        type: "bot",
        text: `That's a great idea. Thank you for your input and for helping us enhance our cybersecurity measures.`,
      },

      // Conversation Sample 8
      {
        type: "user",
        text: `Good afternoon, I received an email that seemed to be a mix of technical jargon and casual language, which made me suspicious.`,
      },
      {
        type: "bot",
        text: `Good afternoon! Thank you for sharing your experience.  
      
Could you describe the email in detail?  
      
For example, did it contain any bullet points or lists, and how was the overall tone?  
      
*Your comprehensive feedback will greatly assist our investigation.*`,
      },
      {
        type: "user",
        text: `The email was unusually verbose, with multiple paragraphs explaining what seemed like an urgent security update. However, the tone shifted abruptly between formal technical language and casual conversation.`,
      },
      {
        type: "bot",
        text: `That inconsistency is definitely a red flag.  
      
Did the email include any specific calls to action, like verifying your information or clicking on a particular link?  
      
Your detailed observations will help us identify phishing patterns more effectively.`,
      },
      {
        type: "user",
        text: `Yes, it demanded that I verify my credentials immediately, which felt very pushy.`,
      },
      {
        type: "bot",
        text: `Thank you for that insight. Your feedback is invaluable in refining our security protocols.  
      
Could you also mention if the email used any distinctive formatting—such as a mix of fonts or colors—that further contributed to your suspicion?`,
      },
      {
        type: "user",
        text: `It did; the formatting was very inconsistent and jarring.`,
      },
      {
        type: "bot",
        text: `I appreciate your thorough explanation. Your input will be relayed to our cybersecurity team for further analysis.`,
      },

      // Conversation Sample 9
      {
        type: "user",
        text: `Hi, I received an email that didn't seem to follow our usual style, and it raised several red flags for me.`,
      },
      {
        type: "bot",
        text: `Hello, thank you for reporting this. Could you please provide a detailed description of the email?  
      
For instance, did it have any unusual formatting, and what was the tone like?  
      
*Every detail helps us understand the context better.*`,
      },
      {
        type: "user",
        text: `The email was very long, with multiple sentences that felt like they were written in haste. It used a mix of technical terms and casual language, which made it seem unprofessional.`,
      },
      {
        type: "bot",
        text: `That sounds quite concerning.  
      
Did the email include any links or attachments that you found dubious?  
      
Also, how did the sender's email address appear—did it match our known contacts?`,
      },
      {
        type: "user",
        text: `There was a link, but it didn't look like it belonged to our company at all. The sender's email was unfamiliar, which further increased my suspicion.`,
      },
      {
        type: "bot",
        text: `Thank you for your detailed response.  
      
Your careful observations are very useful.  
      
Do you have any suggestions on how we might improve our email filtering to catch these kinds of discrepancies more effectively?`,
      },
      {
        type: "user",
        text: `Maybe we could implement a more robust sender verification process or integrate a third-party email filtering service.`,
      },
      {
        type: "bot",
        text: `That's a very thoughtful suggestion. Thank you for your input and for taking the time to share your experience.`,
      },

      // Conversation Sample 10
      {
        type: "user",
        text: `Hello, I received an email that didn't feel right and I'm concerned it might be a phishing attempt.`,
      },
      {
        type: "bot",
        text: `Hi there, thank you for reporting this. I’d like to get a detailed picture of what you experienced.  
      
Could you describe the email in detail? For example, what was the structure like?  
      
Did it include any lists, bullet points, or distinct sections?  
      
*Your detailed account will help us improve our detection methods.*`,
      },
      {
        type: "user",
        text: `The email was lengthy, consisting of several paragraphs. It started with a formal greeting, then shifted into a detailed explanation of a supposed account issue. The content was a mix of technical details and casual language, and it included several bullet points outlining next steps.`,
      },
      {
        type: "bot",
        text: `I appreciate your detailed description.  
      
Emails that change tone mid-message and include long lists of instructions can be particularly deceptive.  
      
Did the email include any indicators of authenticity, like a signature or official logo, or was it lacking these elements entirely?`,
      },
      {
        type: "user",
        text: `It had a logo, but the overall design and tone were inconsistent with our regular communications.`,
      },
      {
        type: "bot",
        text: `Thank you for the valuable feedback.  
      
Your observations about the design and tone are very important.  
      
Could you suggest any improvements for our internal processes to better flag such emails before they reach employees?`,
      },
      {
        type: "user",
        text: `I think a more sophisticated filtering system paired with regular staff training could really make a difference.`,
      },
      {
        type: "bot",
        text: `That's an excellent suggestion. Thank you for your detailed input and for helping us improve our cybersecurity measures.`,
      },
    ];

    // Pick a random number between 5 and 25.
    const count = Math.floor(Math.random() * (25 - 5 + 1)) + 5;
    // For this simulation, we'll simply return the first `count` messages.
    const messages = sampleMessages.slice(0, count);

    // Simulate network delay.
    setTimeout(() => {
      resolve(messages);
    }, 500);
  });
};

export const Route = createFileRoute("/chat/$chatId")({
  component: ChatView,
});

function ChatView() {
  const { chatId = "1" } = useParams({ from: "/chat/$chatId" });

  const { data: messages = [], isLoading } = useQuery({
    queryKey: ["activeChat", chatId],
    queryFn: () => fetchChatMessages(chatId),
    enabled: !!chatId,
    staleTime: Number.POSITIVE_INFINITY,
  });
  console.log("🚀 ~ ChatView ~ messages:", messages);

  return <Bubbles messages={messages} loading={isLoading} />;
}

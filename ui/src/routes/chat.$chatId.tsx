import Bubbles from "@components/chat/Bubbles";
import { useQuery } from "@tanstack/react-query";
import { createFileRoute, useParams } from "@tanstack/react-router";
import { getAllChatsForBaitMockAllBaitChatBaitIdGetOptions } from "src/client/@tanstack/react-query.gen";

// Define the chat message type.
export type ChatMessage = { type: "user" | "assistant"; text: string };

function ChatView() {
  const { chatId = "1" } = useParams({ from: "/chat/$chatId" });

  // Load initial conversation messages from your API.
  const { data, isLoading, isError } = useQuery({
    ...getAllChatsForBaitMockAllBaitChatBaitIdGetOptions({
      path: {
        bait_id: Number(chatId),
      },
    }),
  });

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (isError) {
    return <p>Error loading chat messages.</p>;
  }

  if (!data || !data.messages) {
    return <p>No messages found.</p>;
  }

  return (
    <Bubbles messages={data.messages} chatId={chatId} loading={isLoading} />
  );
}

export const Route = createFileRoute("/chat/$chatId")({
  component: ChatView,
});

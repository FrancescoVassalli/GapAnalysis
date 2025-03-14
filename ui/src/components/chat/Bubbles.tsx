import Message from "@components/chat/Message";
import Prompt from "@components/inputs/Prompt";
import LoadingSpinner from "@components/layout/LoadingSpinner";
import { useStreamAddChat } from "@hooks/useStreamAddChat";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { type FC, useEffect, useRef } from "react";
import {
  type AllBaitChatResponse,
  type AnaAllBaitChatResponseMessage,
  startChatMockStartChatBaitIdPost,
} from "src/client";
import { getAllChatsForBaitMockAllBaitChatBaitIdGetQueryKey } from "src/client/@tanstack/react-query.gen";

interface BubblesProps {
  messages: AnaAllBaitChatResponseMessage[];
  loading: boolean;
  chatId: string | number;
}

const Bubbles: FC<BubblesProps> = ({ messages, loading, chatId }) => {
  const chatContainerRef = useRef<HTMLDivElement>(null);
  const queryClient = useQueryClient();
  const lastAssistantMessageRef = useRef<string>("");

  useEffect(() => {
    if (messages.length > 0 && chatContainerRef.current) {
      chatContainerRef.current.scrollTo({
        top: chatContainerRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [messages]);

  const queryKey = getAllChatsForBaitMockAllBaitChatBaitIdGetQueryKey({
    path: { bait_id: Number(chatId) },
  });

  const { mutate: startChat } = useMutation({
    mutationFn: async () =>
      startChatMockStartChatBaitIdPost({
        path: {
          bait_id: Number(chatId),
        },
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey });
    },
  });

  useEffect(() => {
    if (messages.length === 0) {
      startChat();
    }
  }, [messages, startChat]);

  const { streamedMessage, sendMessage, isStreaming } = useStreamAddChat();

  const handleSend = (userMessage: string) => {
    const optimisticUserMessage: AnaAllBaitChatResponseMessage = {
      type: "user",
      message: userMessage,
    };

    // Optimistically update the chat messages cache.
    queryClient.setQueryData<AllBaitChatResponse>(queryKey, (oldData) => {
      const previousMessages = oldData ? oldData.messages : [];
      return { messages: [...previousMessages, optimisticUserMessage] };
    });

    sendMessage({
      path: { bait_id: Number(chatId) },
      body: { user_message: userMessage },
      headers: { accept: "text/event-stream" },
    });
  };

  // Only update the assistant message if streamedMessage has changed.
  useEffect(() => {
    if (
      streamedMessage &&
      streamedMessage !== lastAssistantMessageRef.current
    ) {
      queryClient.setQueryData<AllBaitChatResponse>(queryKey, (oldData) => {
        const oldMessages = oldData?.messages || [];
        // If last message is already an assistant, update it.
        if (
          oldMessages.length > 0 &&
          oldMessages[oldMessages.length - 1].type === "assistant"
        ) {
          const updatedMessages = [...oldMessages];
          updatedMessages[updatedMessages.length - 1] = {
            ...updatedMessages[updatedMessages.length - 1],
            message: streamedMessage,
          };
          return { messages: updatedMessages };
        }
        // Otherwise, add a new assistant message.
        return {
          messages: [
            ...oldMessages,
            { type: "assistant", message: streamedMessage },
          ],
        };
      });
      lastAssistantMessageRef.current = streamedMessage;
    }
  }, [streamedMessage, queryClient, queryKey]);

  return (
    <div className="flex flex-col h-full">
      {loading && (
        <div className="flex-1 flex items-start justify-start p-4">
          <p className="text-light-haze-500 dark:text-light-haze-400">
            Loading...
          </p>
        </div>
      )}

      {!loading && (
        <div
          ref={chatContainerRef}
          className="flex-1 overflow-y-auto p-4 text-sm leading-6 text-light-haze-900 dark:text-light-haze-100 sm:text-base sm:leading-7"
        >
          {messages.map((message, index) => (
            <Message key={index} type={message.type} text={message.message} />
          ))}

          {isStreaming && (
            <div className="flex items-center mt-4 justify-end mr-4 gap-4">
              <span className="ml-2">Loading...</span>
              <LoadingSpinner className="text-blue-800 dark:text-blue-300" />
            </div>
          )}
        </div>
      )}
      {!loading && (
        <div className="w-full p-4">
          <Prompt onSend={handleSend} />
        </div>
      )}
    </div>
  );
};

export default Bubbles;

import type { Options } from "@hey-api/client-fetch";
import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import {
  type StreamAddChatMockStreamAddChatBaitIdPostData,
  streamAddChatMockStreamAddChatBaitIdPost,
} from "src/client";

export function useStreamAddChat() {
  const [streamedMessage, setStreamedMessage] = useState("");
  const [finalResponse, setFinalResponse] = useState<string | null>(null);

  const mutation = useMutation({
    mutationFn: async (
      options: Options<StreamAddChatMockStreamAddChatBaitIdPostData>
    ) => await streamAddChatMockStreamAddChatBaitIdPost(options),
    onSuccess: async (response) => {
      if (response.data) {
        // The API returns a full string with all SSE lines.
        const streamData: string = response.data;
        const lines = streamData
          .split("\n")
          .map((line) => line.trim())
          .filter(Boolean);

        const tokens: string[] = [];
        // Extract tokens from each line.
        for (const line of lines) {
          if (line.startsWith("data:")) {
            let tokenStr = line.slice("data:".length).trim();

            // Check for the END STREAM marker.
            if (tokenStr.includes("END STREAM")) {
              tokenStr = tokenStr.replace("END STREAM", "").trim();
              if (tokenStr) {
                try {
                  const parsed = JSON.parse(tokenStr);
                  tokens.push(parsed.data);
                } catch (error) {
                  console.error("Error parsing final token JSON:", error);
                }
              }
              break;
            }

            try {
              const parsed = JSON.parse(tokenStr);
              tokens.push(parsed.data);
            } catch (error) {
              console.error("Error parsing token JSON:", error);
            }
          }
        }

        // Incrementally update the UI with each token.
        let accumulatedMessage = "";
        tokens.forEach((token, index) => {
          setTimeout(() => {
            accumulatedMessage += token;
            setStreamedMessage(accumulatedMessage);
            // When the last token is processed, set the final response.
            if (index === tokens.length - 1) {
              setFinalResponse(accumulatedMessage);
            }
          }, index * 10); // Adjust the delay (10ms) as needed.
        });
      }
    },
    onError: (error) => {
      console.error("Stream add chat error:", error);
    },
  });

  const isStreaming = mutation.status === "pending";

  const sendMessage = (
    options: Options<StreamAddChatMockStreamAddChatBaitIdPostData>
  ) => {
    // Reset state for each new request.
    setStreamedMessage("");
    setFinalResponse(null);
    mutation.mutate(options);
  };

  return {
    streamedMessage,
    finalResponse,
    sendMessage,
    isStreaming,
  };
}

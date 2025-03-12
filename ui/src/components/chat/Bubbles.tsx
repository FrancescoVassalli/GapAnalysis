import Message from '@components/chat/Message';
import Prompt from '@components/inputs/Prompt';
import { type FC, useEffect, useRef, useState } from 'react';

interface BubblesProps {
  messages: { type: 'user' | 'bot'; text: string }[];
  loading: boolean;
}

const Bubbles: FC<BubblesProps> = ({ messages: initialMessages, loading }) => {
  const [messages, setMessages] = useState(initialMessages);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setMessages(initialMessages);
  }, [initialMessages]);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTo({
        top: chatContainerRef.current.scrollHeight,
        behavior: 'smooth',
      });
    }
  }, [messages]);

  const handleSendMessage = (message: string) => {
    setMessages((prev) => [
      ...prev,
      { type: 'user', text: message },
      { type: 'bot', text: "That's an interesting question! Let me think..." },
    ]);
  };

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
            <Message key={index} type={message.type} text={message.text} />
          ))}
        </div>
      )}

      {!loading && (
        <div className="w-full p-4">
          <Prompt onSend={handleSendMessage} />
        </div>
      )}
    </div>
  );
};

export default Bubbles;

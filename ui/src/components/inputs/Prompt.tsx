import { type FC, useEffect, useRef, useState } from "react";

interface PromptProps {
  onSend: (message: string) => void;
}

const MAX_TEXTAREA_HEIGHT = 150;

const Prompt: FC<PromptProps> = ({ onSend }) => {
  const [input, setInput] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSend = () => {
    if (input.trim() !== "") {
      onSend(input.trim());
      setInput("");
    }
  };

  useEffect(() => {
    const ta = textareaRef.current;
    if (ta) {
      ta.style.height = "auto";
      const newHeight = Math.min(ta.scrollHeight, MAX_TEXTAREA_HEIGHT);
      ta.style.height = `${newHeight}px`;
    }
  }, [input]);

  return (
    <div className="mt-2 p-4 border-t border-light-haze-300 dark:border-dark-haze-700">
      <div className="relative flex rounded-xl bg-light-haze-50 dark:bg-dark-haze-700 focus:outline-none focus:ring-2 focus:ring-light-haze-300 transition-all duration-300">
        <textarea
          ref={textareaRef}
          id="chat-input"
          className="block w-full resize-none rounded-xl border-none p-4 mr-28 text-sm text-light-haze-900 focus:outline-none dark:text-dark-haze-100 dark:placeholder-dark-haze-400 sm:text-base overscroll-contain overflow-y-auto"
          placeholder="Type your message..."
          rows={1}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              handleSend();
            }
          }}
        ></textarea>
        <button
          type="button"
          onClick={handleSend}
          className="absolute bottom-2 right-2.5 rounded-lg cursor-pointer bg-light-haze-900 px-4 py-2 text-sm font-medium text-light-haze-50 hover:bg-light-haze-800 focus:outline-none focus:ring-4 focus:ring-light-haze-300 dark:bg-dark-haze-100 dark:text-dark-haze-900 dark:hover:bg-dark-haze-200 dark:focus:ring-dark-haze-800 sm:text-base"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Prompt;

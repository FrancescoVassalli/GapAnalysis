import type { FC } from "react";
import ReactMarkdown from "react-markdown";
import remarkBreaks from "remark-breaks";
import remarkGfm from "remark-gfm";

interface MessageProps {
  type: "user" | "bot";
  text: string;
  enableMarkdown?: boolean;
}

const Message: FC<MessageProps> = ({ type, text, enableMarkdown }) => {
  const isUser = type === "user";

  // Simple detection: if the text contains common markdown markers (headers, backticks, bold, etc.)
  const detectMarkdown = (text: string): boolean =>
    /(```|`|\*\*|\*|__|~~|^#+\s)/m.test(text);

  // Determine whether to render using markdown.
  // If enableMarkdown is undefined, then auto-detect based on the content.
  const shouldRenderMarkdown =
    enableMarkdown === undefined ? detectMarkdown(text) : enableMarkdown;

  // Styling classes.
  const containerClass = `flex items-start my-4 ${
    !isUser ? "flex-row-reverse" : ""
  }`;
  const avatarClass = `${isUser ? "mr-2" : "ml-2"} h-8 w-8 rounded-full`;
  const avatarSrc = isUser
    ? "https://dummyimage.com/128x128/363536/ffffff&text=J"
    : "https://dummyimage.com/128x128/354ea1/ffffff&text=G";
  const bubbleClass = `flex flex-col ${
    isUser ? "rounded-b-xl rounded-tr-xl" : "rounded-b-xl rounded-tl-xl"
  } bg-light-haze-50 dark:bg-dark-haze-800 p-4 sm:max-w-md md:max-w-2xl`;

  // If markdown rendering is not enabled, simply render the text in a paragraph.
  if (!shouldRenderMarkdown) {
    return (
      <div className={containerClass}>
        <img
          className={avatarClass}
          src={avatarSrc}
          alt={isUser ? "User Avatar" : "Bot Avatar"}
        />
        <div className={bubbleClass}>
          <p className="whitespace-pre-line break-words">{text}</p>
        </div>
      </div>
    );
  }

  // Otherwise, render using ReactMarkdown with GFM and line breaks support.
  return (
    <div className={containerClass}>
      <img
        className={avatarClass}
        src={avatarSrc}
        alt={isUser ? "User Avatar" : "Bot Avatar"}
      />
      <div className={bubbleClass}>
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkBreaks]}
          components={{
            // Render paragraphs preserving newlines and wrapping long words.
            p: ({ node, children, ...props }) => (
              <p className="whitespace-pre-line break-words" {...props}>
                {children}
              </p>
            ),
          }}
        >
          {text}
        </ReactMarkdown>
      </div>
    </div>
  );
};

export default Message;

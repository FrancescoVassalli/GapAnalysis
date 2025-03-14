import type { FC, ReactNode } from "react";
import React, { memo } from "react";
import ReactMarkdown from "react-markdown";
import remarkBreaks from "remark-breaks";
import remarkGfm from "remark-gfm";

interface MessageProps {
  type: string;
  text: string;
}

interface CodeProps extends React.HTMLAttributes<HTMLElement> {
  inline?: boolean;
  className?: string;
  children?: ReactNode;
}

const CodeBlock: FC<CodeProps> = memo(
  ({ inline, className, children, ...props }) => {
    const content = children?.toString() || "";
    if (inline) {
      return (
        <code className="bg-gray-100 p-1 rounded" {...props}>
          {content}
        </code>
      );
    }
    if (className?.includes("language-markdown")) {
      return (
        <div className="prose max-w-full bg-gray-50 p-2 rounded overflow-x-auto">
          <ReactMarkdown remarkPlugins={[remarkGfm, remarkBreaks]}>
            {content}
          </ReactMarkdown>
        </div>
      );
    }
    return (
      <pre className="bg-gray-100 p-2 rounded overflow-x-auto">
        <code className={className}>{content}</code>
      </pre>
    );
  }
);

const Message: FC<MessageProps> = memo(({ type, text }) => {
  const isUser = type === "user";

  const containerClass = `flex items-start my-4 ${
    !isUser ? "flex-row-reverse" : ""
  }`;
  const avatarClass = `${isUser ? "mr-2" : "ml-2"} h-8 w-8 rounded-full`;
  const avatarSrc = isUser
    ? "https://dummyimage.com/128x128/363536/ffffff&text=U"
    : "https://dummyimage.com/128x128/354ea1/ffffff&text=AI";
  const bubbleClass = `flex flex-col ${
    isUser ? "rounded-b-xl rounded-tr-xl" : "rounded-b-xl rounded-tl-xl"
  } bg-light-haze-50 dark:bg-dark-haze-800 p-4 sm:max-w-md md:max-w-2xl`;

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
            p: ({ node, children, ...props }) => {
              // Combine text nodes for analysis.
              const textContent = React.Children.toArray(children)
                .filter((child) => typeof child === "string")
                .join("");
              // Apply extra margin only if there's at least one newline character.
              const marginClass = textContent.includes("\n") ? "mb-6" : "mb-2";
              return (
                <p
                  className={`whitespace-pre-wrap break-words ${marginClass}`}
                  {...props}
                >
                  {children}
                </p>
              );
            },
            code: CodeBlock,
          }}
        >
          {text}
        </ReactMarkdown>
      </div>
    </div>
  );
});

export default Message;

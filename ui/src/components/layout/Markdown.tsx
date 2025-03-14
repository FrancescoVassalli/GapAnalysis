import { Children, type FC, memo, ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import remarkBreaks from "remark-breaks";
import remarkGfm from "remark-gfm";

interface CodeProps extends React.HTMLAttributes<HTMLElement> {
  inline?: boolean;
  className?: string;
  children?: ReactNode;
}

export const CodeBlock: FC<CodeProps> = memo(
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

type MarkdownProps = {
  text: string;
};

export const Markdown: FC<MarkdownProps> = ({ text }) => {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm, remarkBreaks]}
      components={{
        p: ({ node, children, ...props }) => {
          // Combine text nodes for analysis.
          const textContent = Children.toArray(children)
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
  );
};

export default Markdown;

import Markdown from "@components/layout/Markdown";
import type { FC } from "react";
import { memo } from "react";

interface MessageProps {
  type: string;
  text: string;
}

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
        <Markdown text={text} />
      </div>
    </div>
  );
});

export default Message;

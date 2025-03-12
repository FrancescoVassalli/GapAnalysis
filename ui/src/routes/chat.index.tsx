import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/chat/')({
  component: ChatList,
});

function ChatList() {
  return <div className="text-lg">Select a chat to start messaging.</div>;
}

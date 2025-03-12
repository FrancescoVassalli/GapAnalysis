import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/chat/new')({
  component: NewChatView,
});

function NewChatView() {
  return <div className="text-lg">Start a new chat</div>;
}

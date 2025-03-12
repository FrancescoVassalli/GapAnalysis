import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/bait')({
  component: RouteComponent,
});

function RouteComponent() {
  return <div>Hello "/bait"!</div>;
}

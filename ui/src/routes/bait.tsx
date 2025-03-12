import BaitOverview from '@components/bait/BaitOverview';
import CreateBait from '@components/bait/CreateBait';
import { createFileRoute } from '@tanstack/react-router';
export const Route = createFileRoute('/bait')({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-4xl font-bold text-center mb-6">Bait Summary</h1>
      <div className="space-y-4">
        <CreateBait />
        <BaitOverview/>
      </div>
    </div>
  );
}

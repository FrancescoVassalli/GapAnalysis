import { useQuery } from '@tanstack/react-query';
import { createFileRoute, useParams } from '@tanstack/react-router';
import { getActiveBaitMockActiveBaitBaitIdGetOptions } from 'src/client/@tanstack/react-query.gen';

export const Route = createFileRoute('/bait/$baitId')({
  component: BaitView,
});

function BaitView() {
  const { baitId = '1' } = useParams({ from: '/bait/$baitId' });
  const { data } = useQuery({
    ...getActiveBaitMockActiveBaitBaitIdGetOptions({
      path: { bait_id: baitId },
    }),
  });

  if (!data || !data.bait) {
    return <p>Loading...</p>;
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Modal content */}
      <div className="relative bg-white w-full h-full">
        <iframe
          srcDoc={data.bait}
          title="Bait Content"
          className="w-full h-full"
        />
      </div>
    </div>
  );
}

export default BaitView;

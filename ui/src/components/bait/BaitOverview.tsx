import { useQuery } from '@tanstack/react-query';
import type { FC } from 'react';
import { getActiveBaitsMockActiveBaitsGetOptions } from 'src/client/@tanstack/react-query.gen';
import BaitEntry from './BaitEntry';

const BaitOverview: FC = () => {
  const { data, isLoading, error } = useQuery({
    ...getActiveBaitsMockActiveBaitsGetOptions(),
  });

  if (isLoading) return <p>Loading...</p>;
  if (!data || error) return <p>Error fetching active baits</p>;

  if (data.active_baits?.length === 0) {
    return (
      <p className="text-center">
        No active baits available - Please add a new bait above
      </p>
    );
  }

  return (
    <div
      style={{
        maxHeight: '800px',
        overflowY: 'auto',
        border: '1px solid #ccc',
        padding: '10px',
      }}
    >
      {data.active_baits?.map((bait) => (
        <BaitEntry
          key={bait.id}
          id={bait.id}
          name={bait.name}
          isLoading={('isLoading' in bait ? bait.isLoading : false) as boolean}
        />
      ))}
    </div>
  );
};

export default BaitOverview;

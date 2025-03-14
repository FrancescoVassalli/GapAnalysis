import LoadingSpinner from '@components/layout/LoadingSpinner';
import { GhostMail } from '@scarlab-icons/react';
import { Link, useNavigate } from '@tanstack/react-router';
import type { FC } from 'react';
import type { Bait } from 'src/client';

interface BaitEntryProps {
  name: Bait['name'];
  id: Bait['id'];
  isLoading: boolean;
}

const BaitEntry: FC<BaitEntryProps> = ({ name, id, isLoading }) => {
  const navigate = useNavigate({ from: '/bait' });

  return (
    <div className="p-4 border rounded shadow-sm flex items-center my-2 hover:shadow-xl">
      <div className="flex flex-col w-full gap-2">
        <h2
          className="text-xl text-light-haze-950 hover:text-light-haze-600  font-semibold cursor-pointer dark:text-dark-haze-50 dark:hover:text-light-haze-200"
          onClick={() => id && navigate({ to: `/chat/${id}` })}
        >
          {name}
        </h2>
        {!isLoading && <p>ID: {id} </p>}
        {isLoading && (
          <p>
            ID:{' '}
            {
              <LoadingSpinner
                width={1}
                strokeWidth={2}
                className="inline-block"
              />
            }
          </p>
        )}
      </div>
      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <Link type="button" to={`/bait/${id}`}>
          <GhostMail className="w-5 h-5 text-light-haze-900 dark:text-light-haze-100 ml-auto" />
        </Link>
      )}
    </div>
  );
};

export default BaitEntry;

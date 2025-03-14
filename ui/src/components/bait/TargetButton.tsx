import { useMutation, useQueryClient } from '@tanstack/react-query';
import type { FC } from 'react';
import {
  type ActiveBaitsResponse,
  baitMockBaitTargetNameGet,
} from 'src/client';
import { getActiveBaitsMockActiveBaitsGetQueryKey } from 'src/client/@tanstack/react-query.gen';

interface TargetButtonProps {
  target_name: string;
}

const TargetButton: FC<TargetButtonProps> = ({ target_name }) => {
  const queryClient = useQueryClient();

  const queryKey = getActiveBaitsMockActiveBaitsGetQueryKey();

  const { mutate: handleSubmit } = useMutation({
    mutationFn: async () =>
      await baitMockBaitTargetNameGet({
        path: {
          target_name,
        },
      }),
    onMutate: async () => {
      // Cancel any outgoing refetches
      // (so they don't overwrite our optimistic update)
      await queryClient.cancelQueries({ queryKey: queryKey });

      // Snapshot the previous value
      const existingData = queryClient.getQueryData(queryKey);

      // Optimistically update to the new value
      queryClient.setQueryData(queryKey, (old: ActiveBaitsResponse) => {
        const optimisticData = {
          ...old,
          active_baits: [
            ...old.active_baits,
            { name: target_name, id: null, content: '', isLoading: true },
          ],
        };

        return optimisticData;
      });

      // Return a context object with the snapshotted value
      return { existingData };
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey });
    },
    onError: (error, _variables, context) => {
      console.error('Mutation error:', error);
      // Optionally rollback to previous data if needed
      if (context?.existingData) {
        queryClient.setQueryData(queryKey, context.existingData);
      }
    },
  });

  return (
    <button
      type="button"
      className="p-4 border rounded shadow-sm hover:bg-light-haze-200 dark:hover:bg-dark-haze-600 cursor-pointer"
      onClick={() => handleSubmit()}
    >
      {target_name}
    </button>
  );
};

export default TargetButton;

import { useMutation, useQueryClient } from "@tanstack/react-query";
import type { FC } from "react";
import {
  type SummaryResponse,
  getSummaryMockSummaryGet,
} from "src/client";
import { getSummaryMockSummaryGetQueryKey } from "src/client/@tanstack/react-query.gen";

const SummaryButton: FC = () => {
  const queryClient = useQueryClient();

  const summaryQueryKey = getSummaryMockSummaryGetQueryKey();
  

  const mutation = useMutation({
    mutationFn: async () =>
      await getSummaryMockSummaryGet(),
      onMutate: async () => {
      // Cancel any outgoing refetches
      // (so they don't overwrite our optimistic update)
      await queryClient.cancelQueries({ queryKey: summaryQueryKey });

      // Snapshot the previous value
      const existingData = queryClient.getQueryData(summaryQueryKey);

      // Optimistically update to the new value
      queryClient.setQueryData(summaryQueryKey, (old: SummaryResponse) => {
        const optimisticData = {
          ...old,
          summary: "",
        };

        return optimisticData;
      });

      return { existingData };
    },
    onSuccess: (summary_response) => {
      queryClient.setQueryData(summaryQueryKey, summary_response.data);
    },
    onError: (error, _variables, context) => {
      console.error("Mutation error:", error);
      // Optionally rollback to previous data if needed
      if (context?.existingData) {
        queryClient.setQueryData(summaryQueryKey, context.existingData);
      }
    },
  });

  return (
    <button
      type="button"
      onClick={() => mutation.mutate()}
      className="p-4 border border-solid border-gray-400 rounded cursor-pointer"
      disabled={mutation.isPending}
    >
      {mutation.isPending ? "Generating ..." : "Generate Summary"}
    </button>
  );
};

export default SummaryButton;

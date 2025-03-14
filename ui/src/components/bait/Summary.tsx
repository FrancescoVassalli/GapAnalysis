import SummaryButton from '@components/bait/SummaryButton';
import LoadingSpinner from "@components/layout/LoadingSpinner";
import Markdown from "@components/layout/Markdown";
import { useQuery } from "@tanstack/react-query";
import type { FC } from "react";
import { type SummaryResponse } from "src/client";
import { getSummaryMockSummaryGetQueryKey } from "src/client/@tanstack/react-query.gen";

function mockSummaryQueryFn(): SummaryResponse | undefined {
  return undefined;
}

const SummaryUI: FC = () => {
  const summaryQueryKey = getSummaryMockSummaryGetQueryKey();
  const {
    data: summaryData,
    isLoading,
    error,
  } = useQuery({
    queryKey: summaryQueryKey,
    queryFn: mockSummaryQueryFn,
    staleTime: Number.POSITIVE_INFINITY,
  });

  return (
    <div className="py-4">
      {isLoading && (
        <div className="flex items-center gap-2">
          <LoadingSpinner />
          Loading Summary...
        </div>
      )}

      {error && <div className="text-red-500">Error fetching summary</div>}

      {summaryData && summaryData.summary ? (
        <div className="p-4 w-full text-left shadow-xl rounded-2xl border border-gray-300 max-h-96 overflow-y-auto">
          <div className="flex flex-col items-center">
            <span className="text-m text-light-haze-800 dark:text-light-haze-200">
              <Markdown text={summaryData.summary} />
            </span>
          </div>
        </div>
      ) : (
        <SummaryButton />
      )}
    </div>
  );
};

export default SummaryUI;
import LoadingSpinner from '@components/layout/LoadingSpinner';
import Markdown from '@components/layout/Markdown';
import { useQuery } from '@tanstack/react-query';
import type { FC } from 'react';
import { getSummaryMockSummaryGetOptions } from 'src/client/@tanstack/react-query.gen';

const SummaryUI: FC = () => {
  const {
    data: summaryData,
    refetch,
    isLoading,
    error,
  } = useQuery({
    ...getSummaryMockSummaryGetOptions(),
    enabled: false,
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

      {!isLoading && summaryData && summaryData.summary && (
        <div className="p-4 w-full text-left shadow-xl rounded-2xl border border-gray-300 max-h-96 overflow-y-auto">
          <div className="flex flex-col items-center">
            <span className="w-full text-m text-light-haze-800 dark:text-light-haze-200">
              <Markdown text={summaryData.summary} />
            </span>
          </div>
        </div>
      )}

      {!isLoading && !summaryData && (
        <button
          type="button"
          onClick={() => refetch()}
          className="p-4 border border-solid border-gray-400 rounded cursor-pointer hover:bg-light-haze-200 dark:hover:bg-dark-haze-800 disabled:cursor-not-allowed"
          disabled={isLoading}
        >
          {isLoading ? "Generating ..." : "Generate Summary"}
        </button>
      )}
    </div>
  );
};

export default SummaryUI;

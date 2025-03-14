import SummaryButton from '@components/bait/SummaryButton';
import { useQuery } from "@tanstack/react-query";
import type { FC } from "react";
import ReactMarkdown from 'react-markdown';
import {
    type SummaryResponse,
} from "src/client";
import { getSummaryMockSummaryGetQueryKey } from "src/client/@tanstack/react-query.gen";
function mockSummaryQueryFn(): SummaryResponse| undefined{
    return undefined;
}

const SummaryUI: FC = () => {
    const summaryQueryKey = getSummaryMockSummaryGetQueryKey();
    const { data: summaryData, isLoading, error} = useQuery({
        queryKey: summaryQueryKey,
        queryFn: mockSummaryQueryFn,
        staleTime: Number.POSITIVE_INFINITY,
    });

    console.log(summaryData);

    return (
        <div>
            {summaryData && summaryData.summary? (
                <div className="p-4 w-full text-left shadow-lg rounded-2xl border border-gray-300 bg-white max-h-96 overflow-y-auto">
                    <div className="flex flex-col items-center">
                        <span className="text-m text-light-haze-800 dark:text-light-haze-200">
                            <ReactMarkdown>{summaryData.summary}</ReactMarkdown>
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
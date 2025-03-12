import { useQuery } from "@tanstack/react-query";
import { useState } from "react";
import { getSummaryMockSummaryGetOptions } from "src/client/@tanstack/react-query.gen";

export default function GenerateButton() {
  const [enabled, setEnabled] = useState(false);

  const queryOptions = getSummaryMockSummaryGetOptions();
  const { data, isFetching } = useQuery({
    ...queryOptions,
    enabled,
    onSuccess: () => setEnabled(false),
  });

  return (
    <button
        onClick={() => setEnabled(true)}
        disabled={isFetching}
        className={`flex items-center justify-center px-4 py-2 rounded-lg transition-colors duration-300
            ${isFetching ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700 text-white'}
            shadow-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50`}
    >
        {isFetching ? (
            <div>
            <svg className="animate-spin h-5 w-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 0115.657-2.343A8 8 0 1012 4v8h8a8 8 0 00-8 8z" />
            </svg>
            "Generating..."
            </div>) : ("Generate")
        }
    </button>
  );
}

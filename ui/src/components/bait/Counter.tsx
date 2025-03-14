import { useQuery } from "@tanstack/react-query";
import { FC } from "react";

interface CounterProps {
  label: string;
  queryMethod: Function;
}

const Counter: FC<CounterProps> = ({ label, queryMethod }) => {
  const { data, isLoading, error } = useQuery<any>({
    ...queryMethod(),
  });

  return (
    <div className="p-4 w-64 text-center shadow-lg rounded-2xl border border-gray-300 bg-light-haze-50 dark:bg-dark-haze-900">
      <div className="flex flex-col items-center">
        <span className="text-l font-semibold text-light-haze-800 dark:text-light-haze-200">
          {label}
        </span>

        {isLoading && <span className="text-lg font-bold">Loading...</span>}

        {error && <span className="text-red-500 text-lg">Error</span>}

        {data?.count && <span className="text-xl font-bold">{data.count}</span>}
      </div>
    </div>
  );
};

export default Counter;

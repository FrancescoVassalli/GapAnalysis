import { useQuery } from '@tanstack/react-query';
import { getTotalBaitsMockTotalBaitsGetOptions, getTotalChatSessionsMockTotalChatSessionsGetOptions } from 'src/client/@tanstack/react-query.gen';

function getQueryMethod(label:string){
    if(label==='Total Baits'){
        return getTotalBaitsMockTotalBaitsGetOptions
    }
    if(label==="Gap Analysis Interviews"){
        return getTotalChatSessionsMockTotalChatSessionsGetOptions;
    }
}


export default function CounterWidget({ label }: { label: string }) {
    const { data, isLoading, error } = useQuery({
        ...getQueryMethod(label)(),
      });

  return (
    <div className="p-4 w-64 text-center shadow-lg rounded-2xl border border-gray-300 bg-white">
      <div className="flex flex-col items-center">
        <span className="text-l font-semibold text-light-haze-800 dark:text-light-haze-200">{label}</span>
        {isLoading ? (
          <span className="text-lg font-bold">Loading...</span>
        ) : error ? (
          <span className="text-red-500 text-lg">Error</span>
        ) : (
          <span className="text-xl font-bold">{data.count}</span>
        )}
      </div>
    </div>
  );
}

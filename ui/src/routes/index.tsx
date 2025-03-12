import Counter from '@components/bait/Counter';
import SummaryButton from '@components/bait/SummaryButton';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/')({
  component: () => {
    return (
      <div className="p-6 space-y-8 min-h-screen bg-light-haze-50 dark:bg-dark-haze-950">
        <div
          className="bg-light-haze-100 dark:bg-dark-haze-800 p-6 rounded-lg 
          shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
          dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.1)]"
        >
          <h1 className="text-2xl font-bold text-light-haze-900 dark:text-light-haze-100">
            Advanced Gap Analysis Process (AGAP)
          </h1>
        </div>

        {/* Recent Lessons & Chats */}
        <div>
          <h2 className="text-xl font-semibold text-light-haze-800 dark:text-light-haze-200">
            Bait Campaign KPI
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
            <Counter label="Total Baits"/>
            <Counter label="Gap Analysis Interviews"/>
          </div>
        </div>

        <div>
          <h2 className="text-xl font-semibold text-light-haze-800 dark:text-light-haze-200">
            Gap Insights
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-4">
            <SummaryButton/>
          </div>
        </div>
      </div>
    );
  },
});

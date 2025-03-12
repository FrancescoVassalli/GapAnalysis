import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/')({
  component: () => {
    return (
      <div className="p-6 space-y-8 min-h-screen bg-light-haze-50 dark:bg-dark-haze-950">
        {/* Welcome Section */}
        <div
          className="bg-light-haze-100 dark:bg-dark-haze-800 p-6 rounded-lg 
          shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
          dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.1)]"
        >
          <h1 className="text-2xl font-bold text-light-haze-900 dark:text-light-haze-100">
            Welcome,{' '}
            <span className="text-blue-600 dark:text-blue-400">
              User! <i className="text-3xl">👋</i>
            </span>
          </h1>
          <p className="text-light-haze-600 dark:text-light-haze-300 mt-2">
            Your cybersecurity training dashboard
          </p>
        </div>

        {/* Recent Lessons & Chats */}
        <div>
          <h2 className="text-xl font-semibold text-light-haze-800 dark:text-light-haze-200">
            Recent Activity
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
            {Array.from({ length: 3 }).map((_, i) => (
              <div
                key={i}
                className="bg-light-haze-100 dark:bg-dark-haze-800 p-4 rounded-lg 
                shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
                dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.05)] animate-pulse"
              >
                <div className="h-6 w-3/4 bg-light-haze-300 dark:bg-dark-haze-600 rounded mb-2"></div>
                <div className="h-4 w-1/2 bg-light-haze-300 dark:bg-dark-haze-700 rounded"></div>
              </div>
            ))}
          </div>
        </div>

        {/* Performance Section */}
        <div>
          <h2 className="text-xl font-semibold text-light-haze-800 dark:text-light-haze-200">
            Your Performance
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-4">
            {/* Hours Spent */}
            <div
              className="bg-light-haze-100 dark:bg-dark-haze-800 p-4 rounded-lg 
              shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
              dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.05)] text-center animate-pulse"
            >
              <div className="h-8 w-1/2 bg-light-haze-300 dark:bg-dark-haze-600 mx-auto rounded"></div>
              <p className="text-light-haze-600 dark:text-light-haze-300 mt-2">
                Hours Spent
              </p>
            </div>

            {/* Training Score */}
            <div
              className="bg-light-haze-100 dark:bg-dark-haze-800 p-4 rounded-lg 
              shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
              dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.05)] text-center animate-pulse"
            >
              <div className="h-8 w-1/2 bg-light-haze-300 dark:bg-dark-haze-600 mx-auto rounded"></div>
              <p className="text-light-haze-600 dark:text-light-haze-300 mt-2">
                Training Score
              </p>
            </div>

            {/* Progress */}
            <div
              className="bg-light-haze-100 dark:bg-dark-haze-800 p-4 rounded-lg 
              shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
              dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.05)] text-center animate-pulse"
            >
              <div className="h-8 w-1/2 bg-light-haze-300 dark:bg-dark-haze-600 mx-auto rounded"></div>
              <p className="text-light-haze-600 dark:text-light-haze-300 mt-2">
                Progress
              </p>
            </div>
          </div>
        </div>

        {/* Leaderboard */}
        <div>
          <h2 className="text-xl font-semibold text-light-haze-800 dark:text-light-haze-200">
            Leaderboard
          </h2>
          <div
            className="bg-light-haze-100 dark:bg-dark-haze-800 p-4 rounded-lg 
            shadow-[0px_2px_6px_rgba(0,_0,_0,_0.1)] 
            dark:shadow-[0px_2px_6px_rgba(255,_255,_255,_0.05)] mt-4 animate-pulse"
          >
            <div className="h-8 w-3/4 bg-light-haze-300 dark:bg-dark-haze-600 rounded mb-2"></div>
            <div className="h-6 w-1/2 bg-light-haze-300 dark:bg-dark-haze-700 rounded mb-2"></div>
            <div className="h-6 w-1/3 bg-light-haze-300 dark:bg-dark-haze-700 rounded"></div>
          </div>
        </div>
      </div>
    );
  },
});

import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/')({
  component: () => {
    return (
      <div className="p-6 space-y-8 min-h-screen">
        {/* Welcome Section */}
        <div className="bg-white p-6 rounded-lg ">
          <h1 className="text-2xl font-bold text-gray-900">
            Welcome,{' '}
            <span className="text-blue-600">
              User! <i className="text-3xl">👋</i>
            </span>
          </h1>
          <p className="text-gray-600 mt-2">
            Your cybersecurity training dashboard
          </p>
        </div>

        {/* Recent Lessons & Chats */}
        <div>
          <h2 className="text-xl font-semibold text-gray-800">
            Recent Activity
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
            {Array.from({ length: 3 }).map((_, i) => (
              <div
                key={i}
                className="bg-white p-4 rounded-lg shadow-md animate-pulse"
              >
                <div className="h-6 w-3/4 bg-gray-300 rounded mb-2"></div>
                <div className="h-4 w-1/2 bg-gray-300 rounded"></div>
              </div>
            ))}
          </div>
        </div>

        {/* Performance Section */}
        <div>
          <h2 className="text-xl font-semibold text-gray-800">
            Your Performance
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-4">
            {/* Hours Spent */}
            <div className="bg-white p-4 rounded-lg shadow-md text-center animate-pulse">
              <div className="h-8 w-1/2 bg-gray-300 mx-auto rounded"></div>
              <p className="text-gray-600 mt-2">Hours Spent</p>
            </div>

            {/* Training Score */}
            <div className="bg-white p-4 rounded-lg shadow-md text-center animate-pulse">
              <div className="h-8 w-1/2 bg-gray-300 mx-auto rounded"></div>
              <p className="text-gray-600 mt-2">Training Score</p>
            </div>

            {/* Progress */}
            <div className="bg-white p-4 rounded-lg shadow-md text-center animate-pulse">
              <div className="h-8 w-1/2 bg-gray-300 mx-auto rounded"></div>
              <p className="text-gray-600 mt-2">Progress</p>
            </div>
          </div>
        </div>

        {/* Leaderboard */}
        <div>
          <h2 className="text-xl font-semibold text-gray-800">Leaderboard</h2>
          <div className="bg-white p-4 rounded-lg shadow-md mt-4 animate-pulse">
            <div className="h-8 w-3/4 bg-gray-300 rounded mb-2"></div>
            <div className="h-6 w-1/2 bg-gray-300 rounded mb-2"></div>
            <div className="h-6 w-1/3 bg-gray-300 rounded"></div>
          </div>
        </div>
      </div>
    );
  },
});

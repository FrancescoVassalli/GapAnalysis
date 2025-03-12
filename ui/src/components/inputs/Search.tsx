import { OutlineSearchSquare } from '@scarlab-icons/react';

const Search = () => {
  return (
    <div className="relative">
      <OutlineSearchSquare
        className="absolute left-4 top-1/2 transform -translate-y-1/2 w-6 h-6 
          text-light-haze-800 dark:text-light-haze-300 pointer-events-none"
      />
      <input
        type="search"
        placeholder="Search..."
        className="w-full p-2 pl-12 pr-4 rounded-xl text-lg
          bg-light-haze-200 dark:bg-dark-haze-900 
          text-light-haze-900 dark:text-dark-haze-50 
          outline-2 outline-light-haze-400 dark:outline-dark-haze-600 
          focus:outline-none focus:ring-2 focus:ring-light-haze-600 dark:focus:ring-dark-haze-400"
      />
    </div>
  );
};

export default Search;

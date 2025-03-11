import { OutlineSearchSquare } from '@scarlab-icons/react';

const Search = () => {
  return (
    <div className="relative">
      <OutlineSearchSquare className="absolute left-4 top-1/2 transform -translate-y-1/2 w-6 h-6 text-gray-800 pointer-events-none" />
      <input
        type="search"
        placeholder="Search..."
        className="w-full p-2 pl-12 pr-4 rounded-xl bg-gray-100 text-black outline-2 outline-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-600"
      />
    </div>
  );
};

export default Search;

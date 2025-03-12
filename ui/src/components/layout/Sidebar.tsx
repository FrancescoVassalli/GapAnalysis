import {
  GhostPlusSquare,
  OutlinePlusSquare,
  OutlineSparkles,
} from "@scarlab-icons/react";
import { Link, useLocation } from "@tanstack/react-router";
import type { FC, ReactNode } from "react";

type SidebarProps = {
  title?: string;
  icon?: ReactNode;
  items:
    | { id: string | number; name: string; path: string; isActive?: boolean }[]
    | [];
};

const Sidebar: FC<SidebarProps> = ({ title = "", icon, items }) => {
  const { pathname } = useLocation();
  const sidebarTitle = title || pathname.split("/")[1].replace("/", "");

  return (
    <aside className="w-64 h-full bg-light-haze-100 dark:bg-dark-haze-900 text-light-haze-900 dark:text-light-haze-100 flex flex-col">
      {/* Header */}
      <div className="flex items-center justify-between p-4 border-b-2 border-light-haze-200 dark:border-dark-haze-700">
        <div className="flex flex-row items-center space-x-4">
          {icon && (
            <span className="p-2 bg-light-haze-300 dark:bg-dark-haze-700 rounded-lg">
              {icon}
            </span>
          )}
          <h1 className="text-lg font-bold capitalize">{sidebarTitle}</h1>
        </div>
        <button type="button" className="w-5 h-5 cursor-pointer group">
          <OutlinePlusSquare className="group-hover:hidden text-light-haze-900 dark:text-light-haze-100" />
          <GhostPlusSquare className="hidden group-hover:block text-light-haze-900 dark:text-light-haze-100" />
        </button>
      </div>

      {/* Sidebar Items */}
      <div className="flex-1 overflow-y-auto p-2 space-y-2 scrollbar-thin scrollbar-thumb-light-haze-400 scrollbar-track-light-haze-200 dark:scrollbar-thumb-dark-haze-600 dark:scrollbar-track-dark-haze-800">
        {items.map(({ id, name, path, isActive }) => (
          <Link
            key={id}
            to={path}
            className={`flex items-center p-2 rounded-lg cursor-pointer transition ${
              isActive
                ? "bg-blue-500 text-white"
                : "text-light-haze-600 dark:text-light-haze-300 hover:bg-light-haze-200 dark:hover:bg-dark-haze-800 hover:text-light-haze-900 dark:hover:text-light-haze-100"
            }`}
          >
            {isActive && (
              <OutlineSparkles className="w-5 h-auto mx-2 text-white" />
            )}
            <span className="truncate">{name}</span>
          </Link>
        ))}
      </div>
    </aside>
  );
};

export default Sidebar;

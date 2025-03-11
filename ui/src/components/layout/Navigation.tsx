import {
  GhostChat,
  GhostHomeAlt,
  GhostMail,
  OutlineChat,
  OutlineHomeAlt,
  OutlineMail,
} from '@scarlab-icons/react';
import { Link, useMatchRoute } from '@tanstack/react-router';
import type { FC } from 'react';

const links = [
  { name: 'Home', path: '/', icon: OutlineHomeAlt, activeIcon: GhostHomeAlt },
  { name: 'Chat', path: '/chat', icon: OutlineChat, activeIcon: GhostChat },
  { name: 'Bait', path: '/bait', icon: OutlineMail, activeIcon: GhostMail },
];

const Navigation: FC = () => {
  const matchRoute = useMatchRoute();

  return (
    <nav className="flex flex-col items-center p-4 text-white">
      {/* Logo or Header */}
      <div className="flex items-center justify-center mb-8 w-full h-12 animate-pulse bg-gray-300 rounded-sm">
        <svg
          className="w-10 h-10 text-gray-600"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 20 18"
        >
          <path d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z" />
        </svg>
      </div>

      {/* Navigation Links */}
      <ul className="space-y-6">
        {links.map((link) => {
          const isActive = matchRoute({ to: link.path, fuzzy: true });

          return (
            <li key={link.name}>
              <Link
                to={link.path}
                className={`group flex flex-col items-center p-2 transition-colors duration-300 
                  ${isActive ? 'text-black font-bold' : 'text-gray-500 hover:text-gray-900 font-medium'}`}
              >
                <div className="relative flex items-center justify-center">
                  {/* Background box with hover effect */}
                  <div
                    className={`absolute w-10 h-10 rounded-lg bg-gray-300 transition-all duration-300 
                    ${isActive ? 'opacity-100 scale-110 bg-gradient-to-br from-gray-100 to-gray-300' : 'opacity-0'} 
                    group-hover:opacity-100 group-hover:scale-110 
                    group-hover:bg-gradient-to-tr from-gray-200 to-gray-300`}
                  ></div>

                  {/* Icon (changes on active state) */}
                  {isActive ? (
                    <link.activeIcon className="w-6 h-6 relative z-10" />
                  ) : (
                    <link.icon className="w-6 h-6 relative z-10" />
                  )}
                </div>

                <span className="mt-2 relative z-10">{link.name}</span>
              </Link>
            </li>
          );
        })}
      </ul>
    </nav>
  );
};

export default Navigation;

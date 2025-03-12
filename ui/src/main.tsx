import { RouterProvider, createRouter } from '@tanstack/react-router';
import ReactDOM from 'react-dom/client';
import { routeTree } from './routeTree.gen.ts';
import './style/index.css';
;

// Ensure correct theme on load
function applyTheme(theme: string) {
  document.documentElement.classList.toggle('dark', theme === 'dark');
  localStorage.setItem('theme', theme);
}

// Load saved theme or apply system preference
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  applyTheme(savedTheme);
} else {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  applyTheme(prefersDark ? 'dark' : 'light');
}

// Set up the router
const router = createRouter({
  routeTree,
  defaultPreload: 'intent',
});

const rootElement = document.getElementById('app');

if (rootElement) {
  if (!rootElement.innerHTML) {
    const root = ReactDOM.createRoot(rootElement);
    root.render(<RouterProvider router={router} />);
  }
} else {
  console.error("Root element with ID 'app' not found.");
}

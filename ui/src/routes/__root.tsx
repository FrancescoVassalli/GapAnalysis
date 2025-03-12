import Skeleton from '@components/layout/Skeleton';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import * as reactRouter from '@tanstack/react-router';
import { TanStackRouterDevtools } from "@tanstack/router-devtools";
import { client } from "src/client/client.gen";

// Initialize the global query client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60000,
    },
  },
});

// configure internal service client
client.setConfig({
  baseUrl: (process.env.API_URL || "http://localhost:8000").replace(/\/+$/, ""),
});

export const Route = reactRouter.createRootRoute({
  component: RootComponent,
  head: () => ({
    meta: [
      {
        name: 'description',
        content: 'My App is a web application',
      },
      {
        title: 'My App',
      },
    ],
    links: [
      {
        rel: 'icon',
        href: '/favicon.ico',
      },
    ],
  }),
});

function RootComponent() {
  return (
    <QueryClientProvider client={queryClient}>
      <Skeleton>
        <reactRouter.Outlet />
      </Skeleton>
      <TanStackRouterDevtools position="bottom-right" />
      <ReactQueryDevtools buttonPosition="bottom-left" />
    </QueryClientProvider>
  );
}

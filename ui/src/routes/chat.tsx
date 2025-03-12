import Sidebar from "@components/layout/Sidebar";
import Wrapper from "@components/layout/Wrapper";
import { SolidChat } from "@scarlab-icons/react";
import { useQueryClient } from "@tanstack/react-query";
import { Outlet, createFileRoute } from "@tanstack/react-router";
import { useEffect, useState } from "react";

// Define chat list for Sidebar
const chatItems = Array.from({ length: 10 }, (_, i) => ({
  id: (i + 1).toString(),
  name: `Chat ${i + 1}`,
  path: `/chat/${i + 1}`,
}));

export const Route = createFileRoute("/chat")({
  component: ChatLayout,
});

function ChatLayout() {
  const queryClient = useQueryClient();
  const [activeChatId, setActiveChatId] = useState<string | null>(null);

  useEffect(() => {
    const unsubscribe = queryClient.getQueryCache().subscribe(() => {
      // Get all queries from the cache
      const allQueries = queryClient.getQueryCache().getAll();
      // Filter queries with key starting with "activeChat" and at least one observer
      const activeQueries = allQueries.filter((query) => {
        if (
          Array.isArray(query.queryKey) &&
          query.queryKey[0] === "activeChat"
        ) {
          return query.getObserversCount() > 0;
        }
        return false;
      });

      // Update the activeChatId state (assuming only one active chat at a time)
      if (activeQueries.length > 0) {
        setActiveChatId(activeQueries[0].queryKey[1] as string);
      } else {
        setActiveChatId(null);
      }
    });

    return () => {
      unsubscribe();
    };
  }, [queryClient]);

  // Add isActive flag to each sidebar item based on the activeChatId
  const itemsWithActive = chatItems.map((item) => ({
    ...item,
    isActive: item.id === activeChatId,
  }));

  // get active chat name
  const activeItem = itemsWithActive.find((item) => item.id === activeChatId);
  console.log("🚀 ~ ChatLayout ~ activeItem:", activeItem);

  return (
    <div className="flex h-full">
      <Sidebar icon={<SolidChat className="h-6" />} items={itemsWithActive} />
      <div className="w-full border-l-2 border-light-haze-200 dark:border-dark-haze-700">
        <Wrapper title={activeItem?.name}>
          <Outlet />
        </Wrapper>
      </div>
    </div>
  );
}

export default ChatLayout;

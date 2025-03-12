import Sidebar from "@components/layout/Sidebar";
import Wrapper from "@components/layout/Wrapper";
import { SolidChat } from "@scarlab-icons/react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { createFileRoute, Outlet } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { getChatsMockChatsGetOptions } from "src/client/@tanstack/react-query.gen";

export const Route = createFileRoute("/chat")({
  component: ChatLayout,
});

const fetchChatList = async () => {
  const response = await fetch("http://0.0.0.0:8000/mock/chats");
  const data = await response.json();
  const chats = Object.entries(data).map(([id, name]) => ({
    id,
    name,
    path: `/chat/${id}`,
  }));
  return chats;
};

function ChatLayout() {
  const queryClient = useQueryClient();
  const [activeChatId, setActiveChatId] = useState<string | null>(null);


  const { data = [] } = useQuery({
    ...getChatsMockChatsGetOptions(),
  });

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
  const itemsWithActive = data.map((item) => ({
    ...item,
    isActive: Number(item.id) === Number(activeChatId),
  }));

  // get active chat name
  const activeItem = itemsWithActive.find((item) => item.isActive);
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

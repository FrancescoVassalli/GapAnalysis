import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/bait')({
  component: RouteComponent,
});

function RouteComponent() {
  // Example bait data; in a real app this might come from state or props.
  const baitData = [
    { id: 1, name: "Bait Five", random: "abc123" },
    { id: 2, name: "Bait Two", random: "def456" },
    { id: 3, name: "Bait Three", random: "ghi789" },
  ];

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-4xl font-bold text-center mb-6">Bait Summary</h1>
      <div className="space-y-4">
        <CreateBait />
        {baitData.map(bait => (
          <BaitOverview 
            key={bait.id} 
            id={bait.id} 
            name={bait.name} 
            random={bait.random} 
          />
        ))}
      </div>
    </div>
  );
}

function CreateBait() {
  return (
    <div className="p-4 border border-dashed border-gray-400 rounded hover:bg-gray-100 cursor-pointer">
      <p className="text-center text-blue-500">+ Create New Bait</p>
    </div>
  );
}

function BaitOverview({ id, name, chat_link}) {
  // this should be swapped to a button that takes you to the chat
  return (
    <div className="p-4 border rounded shadow-sm">
      <h2 className="text-xl font-semibold">{name}</h2>
      <p>ID: {id}</p>
    </div>
  );
}
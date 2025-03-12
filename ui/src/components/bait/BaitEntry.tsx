import { useNavigate } from "@tanstack/react-router";
import type { FC } from "react";
interface BaitEntryProps {
  name: string;
  id: number | null | undefined;
}

const BaitEntry: FC<BaitEntryProps> = ({ name, id }) => {
  const navigate = useNavigate();
  return (
    <div  className="p-4 border rounded shadow-sm">
      <button
        onClick={() => navigate({to: `/chat/${id}`})}
      >
        <h2 className="text-xl font-semibold">{name}</h2>
        <p>ID: {id}</p>
      </button>
    </div>
  );
};

export default BaitEntry;

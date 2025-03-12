import type { FC } from "react";

interface BaitEntryProps {
  name: string;
  id: number | null | undefined;
}

const BaitEntry: FC<BaitEntryProps> = ({ name, id }) => {
  return (
    <div className="p-4 border rounded shadow-sm">
      <h2 className="text-xl font-semibold">{name}</h2>
      <p>ID: {id}</p>
    </div>
  );
};

export default BaitEntry;

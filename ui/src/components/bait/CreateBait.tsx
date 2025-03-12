import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { FC, useState } from "react";
import TargetButton from "./TargetButton";

const fetchValidTargets = async (): Promise<string[]> => {
    const { data } = await axios.get("http://localhost:8000/mock/valid-targets");
    return data;
  };

const CreateBait: FC = ()=>{
    const [showTargets, setShowTargets] = useState(false);
    const toggleShowTargets = () => {
        setShowTargets((prev) => !prev);
      };
    const { data: validTargets, isLoading, error } = useQuery({
        queryKey: ["validTargets"],
        queryFn: fetchValidTargets,
      });
    if (isLoading) return <p>Loading...</p>;
    if (error) return <p>Error fetching valid targets</p>;
    return (
        <div
            className="p-4 border border-dashed border-gray-400 rounded hover:bg-gray-100 cursor-pointer"
            onClick={toggleShowTargets}
        >
            <p className="text-center text-blue-500">+ Create New Bait</p>
            {showTargets && (
                <ul>
                    {validTargets?.map((target, index) => (
                      <li key={index}><TargetButton target_name={target}/></li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default CreateBait;
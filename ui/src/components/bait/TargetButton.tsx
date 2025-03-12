import { useQueryClient } from '@tanstack/react-query';
import axios from "axios";
import { FC } from "react";
const submitTarget = async (target_name:string): Promise<string[]> => {
    const { data } = await axios.get(`http://localhost:8000/mock/bait/${target_name}/`);
    console.log(data);
    const queryClient = useQueryClient();
    queryClient.invalidateQueries({ queryKey: ['activeBaits'] });
    return data;
  };

interface TargetButtonProps {
    target_name: string;
}

const TargetButton: FC<TargetButtonProps> = ({target_name})=>{
    const handleClick = () => {
        submitTarget(target_name).catch(console.error);
    };
    return (
        <button onClick={handleClick}>{target_name}</button>
    );
}

export default TargetButton;
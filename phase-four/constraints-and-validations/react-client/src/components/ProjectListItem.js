import React, {useState} from "react"
import { useNavigate } from "react-router-dom";
// import { FaPencilAlt, FaTrash } from "react-icons/fa";
const ProjectListItem = ({ id, about, image, link, name, phase }) => {
  const [count, setCount] = useState(0)
  const navigate = useNavigate()

  function handleClick(){
    setCount(count + 1)
  }

  function handleNavigate() {
    navigate(`/projects/${id}`)
  }
  
  return (
    <li className="card" onClick={handleNavigate}>
      <figure className="image">
        <img src={image} alt={name} />
        <button className="claps" onClick={handleClick}>👏{count}</button>
      </figure>
    </li>
  );
};

export default ProjectListItem;
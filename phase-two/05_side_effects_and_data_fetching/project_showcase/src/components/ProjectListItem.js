import React, {useState} from "react"
import { FaPencilAlt, FaTrash } from "react-icons/fa";
const ProjectListItem = ({ id, about, image, link, name, phase }) => {
  const [count, setCount] = useState(0)

  function handleClick(){
    // setCount((claps) => claps + 1)
    setCount(count + 1)
  }
  return (
    <li className="card">
      <figure className="image">
        <img src={image} alt={name} />
        <button className="claps" onClick={handleClick}>👏{count}</button>
      </figure>

      <section className="details">
        <h4>{name}</h4>
        <p>{about}</p>
        {link ? (
          <p>
            <a href={link}>Link</a>
          </p>
        ) : null}
      </section>

      <footer className="extra">
        <span className="badge blue">Phase {phase}</span>
      </footer>
    </li>
  );
};

export default ProjectListItem;
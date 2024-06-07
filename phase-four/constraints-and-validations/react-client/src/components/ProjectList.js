import { useOutletContext } from "react-router-dom";

import ProjectListItem from "./ProjectListItem";

const ProjectList = () => {

  const {projects, searchQuery, handleSearch} = useOutletContext()

  const results = projects.filter((project) => (
    project.name.toLowerCase().includes(searchQuery.toLowerCase())
  ))

  const projectListItems = results.map((project) => (
    <ProjectListItem key={project.id} id = {project.id} about = {project.about} image ={project.image} link = {project.link} name = {project.name} phase = {project.phase}/>
  ));


  return (
    <section>
      <h2>Projects</h2>

      <div className="filter">
        <button>All</button>
        <button>Phase 5</button>
        <button>Phase 4</button>
        <button>Phase 3</button>
        <button>Phase 2</button>
        <button>Phase 1</button>
      </div>
      <input type="text" placeholder="Search..." onChange={(e) => handleSearch(e.target.value)} value={searchQuery}/>

      <ul className="cards">{projectListItems}</ul>
    </section>
  );
};

export default ProjectList;

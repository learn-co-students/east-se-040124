import ProjectListItem from "./ProjectListItem";
function ProjectList({projects}){
    console.log(projects)

    const projectListItems = projects.map((project) => (
        <ProjectListItem key={project.id} project={project}/>     
    ));
    
    return (
        <section>
            <div className="filter">
                <button>All</button>
                <button>Phase 5</button>
                <button>Phase 4</button>
                <button>Phase 3</button>
                <button>Phase 2</button>
                <button>Phase 1</button>
            </div>
            <input type="text" placeholder="Search..."></input>
            <ul className="cards">{projectListItems}</ul>
        </section>
    )
}
export default ProjectList;
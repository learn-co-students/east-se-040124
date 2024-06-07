import {useState, useEffect} from "react"
import { Outlet } from "react-router-dom"

import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";

const App = () => {
  const [projects, setProjects] = useState([])
  const [isDarkMode, setIsDarkMode] = useState(true)
  const [searchQuery, setSearchQuery] = useState("")

  useEffect(() => {
    fetch("http://localhost:4000/projects")
    .then((res) => res.json())
    .then((proj) => setProjects(proj))
  }, [])

  const onToggleDarkMode = () => setIsDarkMode(!isDarkMode)

  function handleSearch(newsearch){
    setSearchQuery(newsearch)
  }

  const onAddProject = (newProject) => {
    setProjects([...projects, newProject])
  }

  const className = isDarkMode ? "App" : "App light"

  const context = {
    searchQuery,
    projects: projects,
    handleSearch,
    onAddProject
  }

  return (
    <div className={className}>
      <Header isDarkMode = {isDarkMode} onToggleDarkMode = {onToggleDarkMode}/>
      {/* <ProjectForm projects = {projects} onAddProject = {onAddProject}/>
      <ProjectList searchQuery = {searchQuery} projects={projects} handleSearch={handleSearch} setProjects = {setProjects}/> */}
      <Outlet context={context} />
    </div>
  );
};

export default App;
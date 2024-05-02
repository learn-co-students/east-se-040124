import { NavLink } from "react-router-dom";

const Header = ({isDarkMode, onToggleDarkMode}) => {
  
  function handleClick(){
    //Callback Function to update the parent state
    onToggleDarkMode()
  }
  return (
    <header>
      <h1>
        <span className="logo">{"//"}</span>
        Project Showcase
      </h1>
      <nav>
        <NavLink to="/projects">
          Projects
        </NavLink>
        <NavLink to="/projects/new">
          New Project
        </NavLink>
      </nav>
      <button onClick={handleClick}>{isDarkMode ? "Light Mode" : "Dark Mode"}</button>
    </header>
  );
}

export default Header;
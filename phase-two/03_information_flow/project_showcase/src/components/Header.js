import React, {useState} from "react";

const Header = () => {
  const [isDarkMode, setIsDarkMode] = useState(true)

  //Update state when button is clicked
  // const handleClick = () => {
  //   setIsDarkMode(!isDarkMode)
  // }
  
  function handleClick(){
    setIsDarkMode(!isDarkMode)
  }
  return (
    <header>
      <h1>
        <span className="logo">{"//"}</span>
        Project Showcase
      </h1>
      <button onClick={handleClick}>{isDarkMode ? "Light Mode" : "Dark Mode"}</button>
    </header>
  );
}

export default Header;
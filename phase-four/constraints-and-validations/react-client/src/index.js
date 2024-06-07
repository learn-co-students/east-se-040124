import React from "react";
import ReactDOM from "react-dom";
import { RouterProvider, createBrowserRouter } from "react-router-dom"

import "./index.css";
import App from "./App";
import About from "./components/About";
import ProjectList from "./components/ProjectList";
import ProjectForm from "./components/ProjectForm";
import ProjectDetails from "./components/ProjectDetails";

const routes = [
  {
    path: '/',
    element: <App />,
    children: [
      {
        index: true,
        element: <About />
      },
      {
        path: 'projects',
        element: <ProjectList />
      },
      {
        path: 'projects/new',
        element: <ProjectForm />
      },
      {
        path: 'projects/:id',
        element: <ProjectDetails />
      }
    ]
  },
  {
    path: '/about',
    element: <About />
  }
]

const router = createBrowserRouter(routes)

ReactDOM.render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
  document.getElementById("root")
);

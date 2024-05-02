import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"

function ProjectDetails() {
    const [ project, setProject ] = useState({})
    const { id } = useParams() 
    const { name, image, link, about, phase } = project

    useEffect(() => {
        fetch(`http://localhost:4000/projects/${id}`)
        .then(resp => {
            if (resp.ok) {
                resp.json().then(data => setProject(data))
            }
        })
    }, [id])

    return (
        <div>
            Project Details
            <h2>{name}</h2>
            <p>{about}</p>
            <img src={image} alt={name}/>
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
        </div>
    )
}

export default ProjectDetails
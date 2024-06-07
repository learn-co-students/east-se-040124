import { useOutletContext, useNavigate } from "react-router-dom";
import { Formik } from 'formik'
import * as yup from 'yup'

const ProjectForm = () => {
  // const [name, setName] = useState("")
  // const [about, setAbout] = useState("")
  // const [phase, setPhase] = useState("")
  // const [link, setLink] = useState("")
  // const [image, setImage] = useState("")

  const { projects, onAddProject} = useOutletContext()
  const navigate = useNavigate()

  // function handleName(e){
  //   setName(e.target.value)
  // }

  // function handleAbout(e){
  //   setAbout(e.target.value)
  // }

  // function handlePhase(e){
  //   setPhase(e.target.value)
  // }

  // function handleLink(e){
  //   setLink(e.target.value)
  // }

  // function handleImage(e){
  //   setImage(e.target.value)
  // }

  function handleSaveProject(values){
    console.log(values)
    // const newProject = {
    //   id: projects.length+1,
    //   name: name,
    //   about: about,
    //   phase: phase,
    //   link: link,
    //   image: image
    // }
    // onAddProject(newProject)

    // navigate(`/projects/${newProject.id}`)

  }

  let ProjectSchema = yup.object().shape({
    name: yup.string().required().min(5),
    phase: yup.string().required(),
    link: yup.string().required(),
    image: yup.string().required(),
    about: yup.string().required()
  })

  return (
    <section>
      <Formik
        initialValues={{
          name: '',
          about: '',
          phase: '',
          link: '',
          image: ''
        }}
        validationSchema={ProjectSchema}
        onSubmit={handleSaveProject}
      >
        {(props) => {
          const { values: {name, about, phase, link, image}, handleChange, handleSubmit, errors} = props
          return (
            <form className="form" autoComplete="off" onSubmit = {handleSubmit}>
              <h3>Add New Project</h3>

              <label htmlFor="name">Name</label>
              <input type="text" id="name" name="name" onChange={handleChange} value={name}/>
              {errors.name}
              <label htmlFor="about">About</label>
              <textarea id="about" name="about" value={about} onChange={handleChange}/>
              <label htmlFor="phase">Phase</label>
              <select name="phase" id="phase" onChange={handleChange} value={phase}>
                <option>Select One</option>
                <option value="1">Phase 1</option>
                <option value="2">Phase 2</option>
                <option value="3">Phase 3</option>
                <option value="4">Phase 4</option>
              <option value="5">Phase 5</option>
              </select>

              <label htmlFor="link">Project Homepage</label>
              <input type="text" id="link" name="link" onChange={handleChange} value={link}/>

              <label htmlFor="image">Screenshot</label>
              <input type="text" id="image" name="image" onChange={handleChange} value={image}/>

              <button type="submit">Add Project</button>
            </form>
          )
        }}
      </Formik>
    </section>
  );
};

export default ProjectForm;

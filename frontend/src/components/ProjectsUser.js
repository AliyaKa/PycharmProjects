import React from 'react'
import {useParams} from 'react-router-dom'
const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.title}</td>
        </tr>
    )
}

const ProjectsUser = ({projects}) => {
    let {userId} = useParams()
    console.log(userId)
    let filter_projects = projects.filter((project)=>project.users.includes(parseInt(userId)))
    return (
        <table>
            <th>Projects</th>
                {filter_projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default ProjectsUser

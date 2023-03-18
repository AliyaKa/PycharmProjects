import React from 'react'
import {useParams} from 'react-router-dom'
const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.title}</td>
            <td>{project.repository}</td>
            <td>{project.users}</td>

        </tr>
    )
}

const ProjectDetails = ({projects}) => {
    let {projectId} = useParams()
    let filter_projects = projects.filter((project)=>project.title.includes(parseInt(projectId)))

    return (
        <table>
            <th>Projects</th>
            <th>Repository</th>
            <th>Users</th>
                {filter_projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default ProjectDetails

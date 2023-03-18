import React from 'react'
import {Link} from 'react-router-dom'
const ProjectItem = ({item, delete_project}) => {
    return (
        <tr>
            <td><Link to={`/projects/${item.id}`}>{item.title}</Link></td>
            <td>{item.users}</td>
            <td>{item.repository}</td>
            <td><button onClick={()=>delete_project(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {
    return (
    <div>
        <table>
            <th>Title</th>
            <th>Users</th>
            <th>Repository</th>
            <th></th>
                {projects.map((item) => <ProjectItem item={item} delete_project={delete_project}/>)}
        </table>
        <Link to='/projects/create'>Create</Link>
    </div>
    )
}
export default ProjectList
import React from 'react'
import {Link} from 'react-router-dom'
const UserItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`/users/${item.id}`}>{item.username}</Link></td>
            <td>{item.firstname}</td>
            <td>{item.email}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>UserName</th>
            <th>First Name</th>

            <th>E-mail</th>
                {users.map((item) => <UserItem item={item} />)}
        </table>
    )
}
export default UserList
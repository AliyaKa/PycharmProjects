import React from 'react'
import {Link} from 'react-router-dom'


const TodoItem = ({item, deleteToDo}) => {
    return (
        <tr>
            <td>{item.body}</td>
            <td>{item.user}</td>
            <td>{String(item.is_complete)}</td>

            <td>
                <button onClick={()=>deleteToDo(item.id)} type='button'>
                    Delete
                </button></td>
        </tr>
    )
}

const TodoList = ({todo, deleteToDo}) => {
    return (
        <div>
            <table>
                <th>Body</th>
                <th>UserName</th>
                <th>Is complete</th>
                <th></th>
                    {todo.map((item) => <TodoItem item={item} deleteToDo={deleteToDo} />)}
            </table>
            <Link to='/todo/create'>Create</Link>
        </div>
    )
}
export default TodoList
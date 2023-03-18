import axios from 'axios'
import React from 'react';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import ProjectsUser from './components/ProjectsUser.js';
import ProjectsDetails from './components/ProjectDetails.js';
import TodoList from './components/ToDo.js';
import ToDoForm from './components/ToDoForm.js';
import ProjectForm from './components/ProjectForm.js';
import Menu from "./components/Menu.js";
import Footer from "./components/Footer.js";
import NotFound404 from "./components/NotFound404.js";
import LoginForm from "./components/Auth.js";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";
import Cookies from 'universal-cookie';

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todo': [],
            'token': ''
        }
   }


    create_todo(body, user, proj) {
        const headers = this.get_headers()
        const data = {body: body, user: user, proj: proj}
        axios.post('http://127.0.0.1:8000/api/todo/'
        , data, {headers})
        .then(response => {
            console.log(response.data)
            this.load_data()
        }).catch(error => {
            console.log(error.response.data)
            this.setState({todo: []})
            })
        }

   create_project(title, users) {
        const headers = this.get_headers()
        const data = {title: title, users: users}
        axios.post('http://127.0.0.1:8000/api/projects/', data, {headers})
        .then(response => {
            console.log(response.data)
            this.load_data()
        }).catch(error => {
            console.log(error.response.data)
            this.setState({projects: []})
            })
        }


   deleteToDo(id) {
            const headers = this.get_headers()
            axios.delete(`http://127.0.0.1:8000/api/todo/${id}`
                ,{headers}).then(
                    response => {
                        console.log(response)
                        this.load_data()
                    }).catch(error => {
                            console.log(error)
                            this.setState({todo:[]})
                        })
   }
   delete_project(id) {
            const headers = this.get_headers()
            console.log(headers)
            console.log(id)
            axios.delete(`http://127.0.0.1:8000/api/projects/${id}`
                ,{headers}).then(
                    response => {
                        console.log(response)
                        this.load_data()
                    }).catch(error => {
                            console.log(error)
                            this.setState({projects:[]})
                        })
   }



    logout(){
        this.set_token('')
        this.setState({'users':[]})
        this.setState({'projects':[]})
        this.setState({'todo':[]})
    }

    is_auth(){
        return !!this.state.token
    }

    set_token(token){
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    get_token_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password){
        const data = {username: username, password: password}
        axios.post('http://127.0.0.1:8000/api-token/', data).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))

    }

    get_headers(){
        let headers = {
            'Content-Type': 'application/json',
        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token '+this.state.token
        }
        return headers
    }

    load_data(){
            const headers = this.get_headers()
            axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
               this.setState({'users': response.data})
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
               this.setState({'projects': response.data})
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                  this.setState({'todo': response.data})
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_storage()
    }
    render () {
        return (
            <div>
                <Menu />
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todo'>ToDo</Link>
                        </li>
                        <li>
                            {this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> :
                            <Link to='/login'>Login</Link>}
                        </li>

                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users'/>}/>
                        <Route path='/users'>
                                <Route index element={<UserList users={this.state.users}/>}/>
                                <Route path=':userId' element={<ProjectsUser projects={this.state.projects}/>}/>
                        </Route>

                         <Route exact path='/projects/create'
                                    element={<ProjectForm users={this.state.users}
                                                        create_project={(title, users)=>this.create_project(title, users)} />}/>

                        <Route path='/projects'>
                                <Route index element={<ProjectList projects={this.state.projects} delete_project={(id) => this.delete_project(id)}/>}/>
                                <Route path=':projectId' element={<ProjectsDetails projects={this.state.projects}/>}/>
                        </Route>



                        <Route exact path='/todo/create' element={<ToDoForm
                                                        create_todo={(body, user, proj)=>this.create_todo(body, user, proj)} />}/>


                        <Route exact path='/todo' element={<TodoList todo={this.state.todo}
                                                                     deleteToDo={(id) => this.deleteToDo(id)}/>}/>



                        <Route exact path='/login' element={<LoginForm get_token={(username, password) =>
                        this.get_token(username, password)} />}/>

                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
                <Footer />
            </div>
        )
    }
}

export default App;

import React from 'react';

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            title: '',
            users: []
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleUsersChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'users': []
            })
            return;
        }
        let users = []
        for(let i = 0; i < event.target.selectedOptions.length; i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState(
        {'users': users})
    }


    handleSubmit(event) {
        this.props.create_project(this.state.title, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor="title">title</label>
                    <input type="text" className="form-control" name="title" placeholder="title"
                           value={this.state.title}
                           onChange={(event)=>this.handleChange(event)} />
                </div>

                <select name="users" multiple onChange={(event) => this.handleUsersChange(event)}>
                       {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                </select>

                <input type="submit" value="Save" />
            </form>
        );
    }
}

export default ProjectForm
import React from 'react';

class ToDoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            body: '',
            user: 0,
            proj: 0}
    }

    handleChange(event){
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )

    }



    handleSubmit(event){
        this.props.create_todo(this.state.body, this.state.user, this.state.proj)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label htmlFor="body">Todo name</label>
                <input type="text" className="form-control" name="body" placeholder="body"
                    value={this.state.body} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
                <label htmlFor="user">Username</label>
                <input type="number" className="form-control" name="user" placeholder="user"
                    value={this.state.user} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
                <label htmlFor="proj">Project</label>
                <input type="number" className="form-control" name="proj" placeholder="proj"
                    value={this.state.proj} onChange={(event)=>this.handleChange(event)} />
            </div>


                <input type="submit" value="Save" />
            </form>
        );
    }

}

export default ToDoForm
